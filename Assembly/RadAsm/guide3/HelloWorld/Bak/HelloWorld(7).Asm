
.386
.model flat, stdcall  ;32 bit memory model
option casemap :none  ;case sensitive

include HelloWorld.inc

.data
cap	DB "Naked celbrities!!!",0
text1 DB "You're sick, man. Get help.",0
text2 DB "She's old enough to be your mother!!!",0


.code

start:

	invoke GetModuleHandle,NULL
	mov		hInstance,eax

    invoke InitCommonControls
	invoke DialogBoxParam,hInstance,IDD_DIALOG1,NULL,addr DlgProc,NULL
	invoke ExitProcess,0

;########################################################################

DlgProc proc hWin:HWND,uMsg:UINT,wParam:WPARAM,lParam:LPARAM

	mov		eax,uMsg
	.if eax==WM_INITDIALOG

	.elseif eax==WM_COMMAND
		MOV EAX,wParam
		MOV EDX,EAX
		SHR EDX,16
		.If DX==BN_CLICKED
			.If EAX==IDC_BTN1
				Invoke MessageBox, hWin, text1, cap, MB_OK
			.ElseIf EAX==IDC_BTN2
				Invoke MessageBox, hWin, text2, cap, MB_OK
			.EndIf
		.EndIf
	.elseif eax==WM_CLOSE
		invoke EndDialog,hWin,0
	.else
		mov		eax,FALSE
		ret
	.endif
	mov		eax,TRUE
	ret

DlgProc endp

end start
