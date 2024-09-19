import subprocess

# Ruta al archivo de la clave privada cifrada
private_key_path = 'private.pem'
# Ruta al diccionario de contraseñas
wordlist_path = '/home/caru/Escritorio/entornoci/ejercicios/practica1/Desafio_practica1/rockyou.txt'
# Archivo temporal para guardar la clave descifrada
temp_key_path = 'private_unlocked.pem'

def attempt_password(password):
    # Ejecuta el comando openssl para intentar descifrar la clave privada con la contraseña proporcionada
    command = [
        'openssl', 'rsa', '-in', private_key_path,
        '-outform', 'PEM', '-out', temp_key_path,
        '-passin', f'pass:{password}'
    ]
    
    try:
        # Ejecuta el comando y captura la salida
        result = subprocess.run(command, capture_output=True, text=True)
        # Si no hay errores, la contraseña es correcta
        if result.returncode == 0:
            print(f'Contraseña encontrada: {password}')
            return True
        else:
            return False
    except Exception as e:
        print(f'Error: {e}')
        return False

def crack_password(wordlist):
    with open(wordlist, 'r', encoding='latin1') as file:
        for line in file:
            password = line.strip()
            print(f'Probando contraseña: {password}')
            if attempt_password(password):
                print('Contraseña descifrada exitosamente.')
                return
    print('No se encontró la contraseña en el diccionario.')

# Ejecuta el script
crack_password(wordlist_path)

