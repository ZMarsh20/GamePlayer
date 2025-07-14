# List of programs to check with their corresponding core counts
$programsAndPcores = @(
    "GTA5",
    "HogwartsLegacy",
    "Borderlands*",
    "Minecraft",
    "OverWatch",
    "Valorant*",
    "Fortnite*"
)

$programsAndEcores = @(
    "Azeron Software", 
    "powershell", 
    "PhoneExperienceHost", 
    "OneDrive", 
    "SteelSeries*", 
    "sunshine", 
    "UsbMonitorL",
    "PowerPanel Personal",
    "Discord",
    "YourPhoneAppProxy",
    "MSIAfterburner",
    "GameOverlayUI"
)

function Set-ProcessAffinity {
    param(
        [string]$processName,
        [long]$desiredAffinity
    )
    $process = Get-Process -Name $processName
    if ($process) {
        $currentAffinity = $process.ProcessorAffinity
        ForEach($PROCESS in GET-PROCESS $processName) { 
            if ($currentAffinity -ne $desiredAffinity) {
                $PROCESS.ProcessorAffinity=$desiredAffinity
            }
        }
    }
}

while ($true) {
    foreach ($program in $programsAndPcores) {
        Set-ProcessAffinity -processName $program -desiredAffinity 65535
    }
    foreach ($program in $programsAndEcores) {
        Set-ProcessAffinity -processName $program -desiredAffinity 268369920
    }
    Set-ProcessAffinity -processName "Cyberpunk2077" -desiredAffinity (1 -shl 18) - 1
    Start-Sleep -Seconds 600
}
