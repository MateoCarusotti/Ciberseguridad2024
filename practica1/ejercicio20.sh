#!/bin/bash

# Ruta al archivo cifrado y al diccionario
encrypted_file="flag.txt.gpg"
dictionary_file="dic2"

# Directorio temporal para guardar archivos descomprimidos
temp_dir=$(mktemp -d)

# Intentar cada contraseña en el diccionario
while IFS= read -r password; do
  echo "Probando: $password"
  echo "$password" | gpg --batch --yes --passphrase-fd 0 --decrypt "$encrypted_file" > "$temp_dir/decrypted.txt" 2>/dev/null
  
  if [ -s "$temp_dir/decrypted.txt" ]; then
    echo "¡Contraseña encontrada!"
    cat "$temp_dir/decrypted.txt"
    break
  fi
done < "$dictionary_file"

# Limpiar el directorio temporal
rm -rf "$temp_dir"
