# Method basis

Use this reference to support tool choices and QA. It states general principles; it does not prescribe a project, engine, dimensions, file names, or output count.

## Alpha and compositing

- The W3C compositing model defines normal source-over alpha compositing and distinguishes premultiplied values from non-premultiplied color. Use it as the mathematical basis for preserving ordered transparent layers. In practice, keep alpha handling explicit across tools and inspect semi-transparent edges after transformations.
- Pillow documents `alpha_composite` as an RGBA/LA operation; use it only with compatible image modes and sizes or use the instance API with deliberate placement. This is an example of validating a tool's mode constraints rather than assuming alpha survives every API path.
- ImageMagick documents source-over as the default alpha composite method and exposes explicit alpha-channel and compose options. State the selected operation in task evidence; do not rely on a tool default that the next operator cannot reproduce.

## Geometry and repeat seams

- OpenCV documents that geometric transforms use reverse mapping and configurable border extrapolation. Treat a transform's border mode and resampling as visible image decisions: they can introduce empty pixels, copied edge pixels, or color fringes at a loop seam.
- A layer can pass a pixel or seam metric while still looking wrong in motion, after alpha blending, or when paired with a differently scrolling layer. Use side-by-side, offset, and full-composite inspection, followed by human visual acceptance.

## Sources

- W3C, [Compositing and Blending Level 1](https://www.w3.org/TR/compositing-1/): source-over equations, alpha, and premultiplied representation.
- Pillow, [Image module documentation](https://pillow.readthedocs.io/en/stable/reference/Image.html): RGBA alpha-composite API behavior.
- ImageMagick, [Alpha Compositing](https://imagemagick.org/compose/): compose operators and source-over behavior.
- OpenCV, [Geometric Image Transformations](https://docs.opencv.org/master/da/d54/group__imgproc__transform.html): reverse mapping and border handling.

Sources are method references, not production approval. A task contract and visual owner remain authoritative for each scene.
