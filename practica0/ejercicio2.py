#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host ic.catedras.linti.unlp.edu.ar --port 10002
from pwn import *

# Set up pwntools for the correct architecture
context.update(arch='i386')
exe = 'ejercicio1.py'

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141 EXE=/tmp/executable
host = args.HOST or 'ic.catedras.linti.unlp.edu.ar'
port = int(args.PORT or 10002)


def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
"""def hacer_cuenta(cuenta):
    resultado = 0
    op1 = int (cuenta[0])
    op2 = int (cuenta[2])

 
    if cuenta[1] == "+":
        resultado = op1 + op2
    elif cuenta[1] == "-":
        resultado = op1 - op2
    else:
        resultado = op1 * op2
    return resultado
"""
io = start()

io.readuntil('flag!:\n')

cuenta = io.readline()

cuenta = cuenta.decode()
print(cuenta)


cuenta = cuenta.split()


op1 = int (cuenta[0])
op2 = int (cuenta[2])


if cuenta[1] == "+":
    resultado = op1 + op2
elif cuenta[1] == "-":
    resultado = op1 - op2
else:
    resultado = op1 * op2


print(resultado)
io.send((str(resultado) + "\n").encode())

respuesta = io.readline().decode()


print(respuesta)

while(respuesta == "Correcto! A resolver!:\n"):
    

    cuenta = io.readline()

    cuenta = cuenta.decode()

    print(cuenta)
    cuenta = cuenta.split()


    op1 = int (cuenta[0])
    op2 = int (cuenta[2])


    if cuenta[1] == "+":
        resultado = op1 + op2
    elif cuenta[1] == "-":
        resultado = op1 - op2
    else:
        resultado = op1 * op2

    print(resultado)
    io.send((str(resultado) + "\n").encode())

    respuesta = io.readline().decode()
    
    print(respuesta)
    

# shellcode = asm(shellcraft.sh())
# payload = fit({
#     32: 0xdeadbeef,
#     'iaaa': [1, 2, 'Hello', 3]
# }, length=128)
# io.send(payload)
# flag = io.recv(...)
# log.success(flag)

io.interactive()

