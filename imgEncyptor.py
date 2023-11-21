# Image encryptor

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    # Leer la imagen
    image = Image.open(input_path)

    # Convertir la imagen a bytes
    image_data = image.tobytes()

    # Inicializar el cifrador AES
    cipher = AES.new(key, AES.MODE_ECB)

    # Cifrar los datos de la imagen
    encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))

    # Crear una nueva imagen a partir de los datos cifrados
    encrypted_image = Image.frombytes(image.mode, image.size, encrypted_data)

    # Guardar la imagen cifrada
    encrypted_image.save(output_path)

def decrypt_image(input_path, output_path, key):
    # Leer la imagen cifrada
    encrypted_image = Image.open(input_path)

    # Convertir la imagen cifrada a bytes
    encrypted_data = encrypted_image.tobytes()

    # Inicializar el cifrador AES
    cipher = AES.new(key, AES.MODE_ECB)

    # Descifrar los datos de la imagen
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    # Crear una nueva imagen a partir de los datos descifrados
    decrypted_image = Image.frombytes(encrypted_image.mode, encrypted_image.size, decrypted_data)

    # Guardar la imagen descifrada
    decrypted_image.save(output_path)

# Ejemplo de uso

encrypted_image_path = "Encrypted"
decrypted_image_path = "Decrypted"

input = input('1. Cifrar imagen \n2. Descifrar imagen \n')
if input == '1':
    input_image_path = input('Path de imagen')
    key = input('Clave')
    encrypt_image(input_image_path, encrypted_image_path, key)


elif input == '2':
    input_image_path = input('Path de imagen cifrada')
    key = input('Clave')
    decrypt_image(encrypted_image_path, decrypted_image_path, key)






# Cifrar la imagen

# Descifrar la imagen


