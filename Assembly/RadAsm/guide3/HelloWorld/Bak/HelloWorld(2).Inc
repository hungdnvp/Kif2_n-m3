
include windows.inc
include kernel32.inc
include user32.inc
include Comctl32.inc
include shell32.inc

includelib kernel32.lib
includelib user32.lib
includelib Comctl32.lib
includelib shell32.lib

DlgProc			PROTO	:HWND,:UINT,:WPARAM,:LPARAM

.const

IDD_DIALOG1			equ 101
IDC_BTN1			equ 1001
IDC_BTN2			equ 1002

;#########################################################################

.data?

hInstance			dd ?
hIcon 				dd ?

;#########################################################################
