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


def cifrar_xor(mensaje, clave):
    return bytes(byte ^ clave for byte in mensaje)

def hex_to_bytes(hex_string):
    return binascii.unhexlify(hex_string)

io = start()


io.readuntil("es:\n")


palabra_inicial = io.readline().strip()  
texto_cifrado = io.readline().strip()

print(type(palabra_inicial))
print(type(texto_cifrado))


texto_cifrado = texto_cifrado.decode()

print(type(texto_cifrado))


texto_cifrado_bytes = binascii.unhexlify(texto_cifrado)

print(type(texto_cifrado_bytes))

print((texto_cifrado_bytes))

key_buscada = b''

for key in range(2**32):
    key_usada = key % 256
    resultado = cifrar_xor(texto_cifrado_bytes,key_usada)
    if (key == 1):
        print(type(resultado))
    if(binascii.hexlify(palabra_inicial) in binascii.hexlify(texto_cifrado_bytes)):
        key_buscada = key_usada
        print(f"Encontre la key es:{key_buscada}")
        break

io.interactive()

