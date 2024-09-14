import binascii


mensaje_cifrado = """08296632232822342f27356637332366252f2034273466252928661e09146a66252e236866162334296624332328296a662a2766202a272166222366233532236634233229662335660f053d092c7619257628193e7634676767737e7f737f73737f192527352f192e27252d232334343b"""

print(type(mensaje_cifrado))

mensaje_cifrado = binascii.unhexlify(mensaje_cifrado)

print(type(mensaje_cifrado))

def descifrar_xor(mensaje, clave):
    return ''.join(chr(byte ^ clave) for byte in mensaje)

for clave in range(256):
    mensaje_descifrado = descifrar_xor(mensaje_cifrado, clave)
    print(type(mensaje_descifrado))
    if("IC{" in mensaje_descifrado):
        print( mensaje_descifrado)

