[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectRoot,
    [Parameter(Mandatory = $true)]
    [string]$ProjectName,
    [ValidateSet('Godot', 'Unity', 'Unreal', 'Web', 'Unknown')]
    [string]$Engine = 'Unknown',
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$templateRoot = Join-Path $repoRoot 'templates\project'
$resolvedRoot = [System.IO.Path]::GetFullPath($ProjectRoot)
$date = Get-Date -Format 'yyyy-MM-dd'

New-Item -ItemType Directory -Force -Path $resolvedRoot | Out-Null

function Write-TemplateFile {
    param([string]$Source, [string]$Destination)
    if ((Test-Path -LiteralPath $Destination) -and -not $Force) {
        Write-Host "SKIP existing: $Destination"
        return
    }
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Destination) | Out-Null
    if ([System.IO.Path]::GetExtension($Source) -eq '.xlsx') {
        Copy-Item -LiteralPath $Source -Destination $Destination -Force
        return
    }
    $content = Get-Content -LiteralPath $Source -Raw -Encoding UTF8
    $content = $content.Replace('{{PROJECT_NAME}}', $ProjectName)
    $content = $content.Replace('{{PROJECT_ROOT}}', $resolvedRoot)
    $content = $content.Replace('{{ENGINE}}', $Engine)
    $content = $content.Replace('{{DATE}}', $date)
    [System.IO.File]::WriteAllText($Destination, $content, [System.Text.UTF8Encoding]::new($false))
}

Get-ChildItem -LiteralPath $templateRoot -Recurse -File -Force | ForEach-Object {
    $relative = $_.FullName.Substring($templateRoot.Length).TrimStart('\')
    Write-TemplateFile -Source $_.FullName -Destination (Join-Path $resolvedRoot $relative)
}

foreach ($directory in @('docs\features', 'config', 'assets', 'PM', 'QA', 'tmp')) {
    New-Item -ItemType Directory -Force -Path (Join-Path $resolvedRoot $directory) | Out-Null
}

Write-Host "Initialized $ProjectName at $resolvedRoot"
Write-Host "Next: assign roles in docs/project_profile.yaml and docs/PM_HANDOFF.md."
