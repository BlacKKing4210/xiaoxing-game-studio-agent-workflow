[CmdletBinding()]
param([string]$Root = (Split-Path -Parent $PSScriptRoot))

$ErrorActionPreference = 'Stop'
$patterns = @(
    '[A-Za-z]:\\Users\\',
    '019f[0-9a-f-]{20,}',
    '\b[A-F0-9]{64}\b',
    'BEGIN (RSA|OPENSSH|EC) PRIVATE KEY',
    'ghp_[A-Za-z0-9]+',
    'github_pat_[A-Za-z0-9_]+'
)
$allowed = @('scripts\check-sanitization.ps1')
$violations = New-Object System.Collections.Generic.List[string]

Get-ChildItem -LiteralPath $Root -Recurse -File -Force |
    Where-Object { $_.FullName -notmatch '\\.git\\' -and $_.Extension -notin @('.xlsx', '.png', '.jpg', '.gif') } |
    ForEach-Object {
        $relative = $_.FullName.Substring($Root.Length).TrimStart('\')
        if ($allowed -contains $relative) { return }
        $text = Get-Content -LiteralPath $_.FullName -Raw -Encoding UTF8 -ErrorAction SilentlyContinue
        foreach ($pattern in $patterns) {
            if ($text -match $pattern) { $violations.Add("$relative :: $pattern") }
        }
    }

if ($violations.Count -gt 0) {
    $violations | ForEach-Object { Write-Error $_ }
    exit 1
}
Write-Host 'Sanitization scan passed.'
