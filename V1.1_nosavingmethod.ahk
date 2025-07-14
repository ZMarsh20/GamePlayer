#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
#Persistent
#SingleInstance
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
SetKeyDelay 0
SetWinDelay 0
SetBatchLines 0
SetControlDelay 0
SetTitleMatchMode, 2
if not A_IsAdmin
	Run *RunAs "%A_ScriptFullPath%"
OnExit("AppExit")
!+f4::ExitApp
^Numpad0::
	RunWait netsh advfirewall firewall add rule name="BATCH GTA 5 BLOCK" dir=out action=block ,,hide
	RunWait  netsh advfirewall firewall add rule name="BATCH GTA 5 BLOCK" dir=in action=block ,,hide
	ToolTip, GTA5 NETWORK BLOCK ON, 0, 0
	Sleep 3000
	Tooltip, , 0, 0
	return



^Numpad1::
	RunWait  netsh advfirewall firewall delete rule name="BATCH GTA 5 BLOCK" ,,hide
	ToolTip, GTA5 NETWORK BLOCK OFF, 0, 0
	Sleep 3000
	Tooltip, , 0, 0
	return



^f9::
	RunWait netsh advfirewall firewall add rule name="123456" dir=out action=block remoteip="192.81.241.171" ,,hide
	ToolTip, NO SAVING MODE ON, 10, 10
	Sleep 3000
	ToolTip, NO SAVING MODE ON, 10, 10
return



^f12::
	RunWait netsh advfirewall firewall delete rule name="123456" ,,hide
	ToolTip, NO SAVING MODE OFF, 10, 10
	Sleep 3000
	Tooltip, , 0, 0
return



^f8::
	Tooltip,
(Ctrl and F5 - block connection for the game
Ctrl and F6 - restore connection for the game
Ctrl and Num0 - Disable saving mode
Ctrl and Num1 - Enable/Restore saving mode
Ctrl and Num2 - Display this help text
	), 0, 0
Sleep 5000
Tooltip, , 0, 0
return



;scripts
AppExit()
{
	RunWait netsh advfirewall firewall delete rule name="BATCH GTA 5 BLOCK" ,,hide
	RunWait netsh advfirewall firewall delete rule name="123456" ,,hide
}
