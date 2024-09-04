#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host ic.catedras.linti.unlp.edu.ar --port 11015
from pwn import *

# Set up pwntools for the correct architecture
context.update(arch='i386')
exe = './path/to/binary'

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141 EXE=/tmp/executable
host = args.HOST or 'ic.catedras.linti.unlp.edu.ar'
port = int(args.PORT or 11015)


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

import binascii


def descifrar_xor(mensaje, clave):
    return ''.join(chr(byte ^ clave) for byte in mensaje)

def hex_to_bytes(hex_string):
    return binascii.unhexlify(hex_string)

io = start()


io.readuntil("es:\n")


palabra_inicial = io.readline().strip()  
texto_cifrado = io.readline().strip()

print(palabra_inicial)
print(texto_cifrado)


texto_cifrado = texto_cifrado.decode()

print(texto_cifrado)

key_correcta = b''

for i in range(4**8):
    
    
    primera_parte = (descifrar_xor(palabra_inicial,i)).encode().hex()
    
    if (texto_cifrado.startswith(primera_parte)):
        key_correcta = i
        print("ENCONTRE")
        break

texto_descencriptado = descifrar_xor(binascii.unhexlify(texto_cifrado.encode()),key_correcta)



io.interactive()

