#!/usr/bin/env python3
"""Remove a flat background and normalize a transparent side-view unit."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--canvas-width", required=True, type=int)
    parser.add_argument("--canvas-height", required=True, type=int)
    parser.add_argument("--subject-height", required=True, type=int)
    parser.add_argument("--foot-y", required=True, type=int)
    parser.add_argument("--center-x", required=True, type=float)
    parser.add_argument("--alpha-threshold", type=int, default=16)
    parser.add_argument("--chroma-helper", type=Path)
    return parser.parse_args()


def has_transparent_canvas(image: Image.Image) -> bool:
    alpha = image.convert("RGBA").getchannel("A")
    corners = (
        alpha.getpixel((0, 0)),
        alpha.getpixel((alpha.width - 1, 0)),
        alpha.getpixel((0, alpha.height - 1)),
        alpha.getpixel((alpha.width - 1, alpha.height - 1)),
    )
    return min(corners) == 0 and alpha.getextrema()[0] == 0


def resolve_chroma_helper(explicit: Path | None) -> Path:
    if explicit:
        return explicit
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    return codex_home / "skills" / ".system" / "imagegen" / "scripts" / "remove_chroma_key.py"


def remove_chroma(source: Path, destination: Path, helper: Path) -> None:
    if not helper.is_file():
        raise FileNotFoundError(f"Chroma-key helper not found: {helper}")
    subprocess.run(
        [
            sys.executable,
            str(helper),
            "--input",
            str(source),
            "--out",
            str(destination),
            "--auto-key",
            "border",
            "--soft-matte",
            "--transparent-threshold",
            "12",
            "--opaque-threshold",
            "220",
            "--despill",
        ],
        check=True,
    )


def threshold_alpha(image: Image.Image, threshold: int) -> Image.Image:
    rgba = image.convert("RGBA")
    rgba.putalpha(rgba.getchannel("A").point(lambda value: 0 if value < threshold else value))
    return rgba


def normalize(
    image: Image.Image,
    canvas_width: int,
    canvas_height: int,
    subject_height: int,
    foot_y: int,
    center_x: float,
    threshold: int,
) -> Image.Image:
    rgba = threshold_alpha(image, threshold)
    bbox = rgba.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError("No visible subject found after alpha cleanup.")
    subject = rgba.crop(bbox)
    target_width = round(subject.width * subject_height / subject.height)
    subject = subject.resize((target_width, subject_height), Image.Resampling.LANCZOS)
    x = round(center_x - (target_width - 1) / 2)
    y = foot_y - subject_height
    if x < 0 or y < 0 or x + target_width > canvas_width or foot_y > canvas_height:
        raise ValueError("Normalized subject does not fit the requested canvas.")
    output = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))
    output.alpha_composite(subject, (x, y))
    return output


def validate(
    image: Image.Image,
    canvas_width: int,
    canvas_height: int,
    subject_height: int,
    foot_y: int,
    center_x: float,
) -> dict:
    rgba = image.convert("RGBA")
    alpha = rgba.getchannel("A")
    bbox = alpha.point(lambda value: 255 if value else 0).getbbox()
    errors: list[str] = []
    if rgba.size != (canvas_width, canvas_height):
        errors.append(f"size={rgba.size}")
    if bbox is None:
        errors.append("empty-alpha")
        bbox = (0, 0, 0, 0)
    actual_height = bbox[3] - bbox[1]
    actual_center = (bbox[0] + bbox[2] - 1) / 2
    expected_top = foot_y - subject_height
    corners = [
        alpha.getpixel((0, 0)),
        alpha.getpixel((canvas_width - 1, 0)),
        alpha.getpixel((0, canvas_height - 1)),
        alpha.getpixel((canvas_width - 1, canvas_height - 1)),
    ]
    if abs(actual_height - subject_height) > 2:
        errors.append(f"subject-height={actual_height}")
    if abs(bbox[1] - expected_top) > 2:
        errors.append(f"top={bbox[1]}")
    if abs(bbox[3] - foot_y) > 2:
        errors.append(f"foot-y={bbox[3]}")
    if abs(actual_center - center_x) > 1:
        errors.append(f"center-x={actual_center}")
    if any(corners):
        errors.append(f"corner-alpha={corners}")
    return {
        "size": rgba.size,
        "bbox": bbox,
        "subject_height": actual_height,
        "center_x": actual_center,
        "top": bbox[1],
        "foot_y": bbox[3],
        "corner_alpha": corners,
        "passed": not errors,
        "errors": errors,
    }


def main() -> int:
    args = parse_args()
    if not args.input.is_file():
        raise FileNotFoundError(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    source = Image.open(args.input)
    with tempfile.TemporaryDirectory(prefix="sideview-") as temp_dir:
        if has_transparent_canvas(source):
            transparent = source.convert("RGBA")
        else:
            keyed = Path(temp_dir) / "transparent.png"
            remove_chroma(args.input, keyed, resolve_chroma_helper(args.chroma_helper))
            transparent = Image.open(keyed).convert("RGBA")
        final = normalize(
            transparent,
            args.canvas_width,
            args.canvas_height,
            args.subject_height,
            args.foot_y,
            args.center_x,
            args.alpha_threshold,
        )
        final.save(args.output, optimize=True)
    report = validate(
        final,
        args.canvas_width,
        args.canvas_height,
        args.subject_height,
        args.foot_y,
        args.center_x,
    )
    print(json.dumps(report, ensure_ascii=False))
    return 0 if report["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
