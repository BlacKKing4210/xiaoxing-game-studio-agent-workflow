[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$python = if ($env:CODEX_BUNDLED_PYTHON) { $env:CODEX_BUNDLED_PYTHON } else { 'python' }
$skillValidator = Join-Path $env:USERPROFILE '.codex\skills\.system\skill-creator\scripts\quick_validate.py'
$pluginValidator = Join-Path $env:USERPROFILE '.codex\skills\.system\plugin-creator\scripts\validate_plugin.py'

& (Join-Path $root 'scripts\check-sanitization.ps1') -Root $root

foreach ($skill in @('game-studio-orchestrator', 'game-pm-execution-ops')) {
    & $python $skillValidator (Join-Path $root "skills\$skill")
    if ($LASTEXITCODE -ne 0) { throw "Skill validation failed: $skill" }
}

& $python $pluginValidator $root
if ($LASTEXITCODE -ne 0) { throw 'Plugin validation failed.' }

$required = @(
    '.codex-plugin\plugin.json',
    'templates\project\AGENTS.md',
    'templates\project\docs\active_scope.yaml',
    'templates\project\PM\feature_progress.xlsx'
)
foreach ($relative in $required) {
    if (-not (Test-Path -LiteralPath (Join-Path $root $relative))) { throw "Missing required file: $relative" }
}

Write-Host 'Repository validation passed.'
