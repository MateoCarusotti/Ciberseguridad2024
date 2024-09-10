import subprocess
from multiprocessing import Process, Value

def decriptar(comienzo, fin, contraseñas, encontrado):
    for i in contraseñas[comienzo:fin]:
        if encontrado.value:
            break
        resultado = subprocess.run(
            ['gpg', '--batch', '--passphrase', i, '--decrypt', 'flag.txt.gpg'],
            capture_output=True,
            text=True
        )
        print(f'intento: {i}')
        if 'descifrado fallido:' not in resultado.stderr:
            print(resultado.stdout)
            encontrado.value = True 
            break

with open('diccionario', 'r') as dic:
    contraseñas = dic.readlines()

with open('diccionarioreves', 'r') as dicr:
    contraseñas2 = dicr.readlines()

mitad = len(contraseñas) // 2


encontrado = Value('b', False) 

p1 = Process(target=decriptar, args=(0, mitad, contraseñas, encontrado))
p2 = Process(target=decriptar, args=(0, mitad, contraseñas2, encontrado))

p1.start()
p2.start()

p1.join()
p2.join()

print('Terminaron los procesos')
