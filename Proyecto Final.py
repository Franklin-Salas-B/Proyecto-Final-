import secrets # Se utiliza para generar valores seguros y aleatoreos
import string # Proporciona acceso a conjuntos de caracteres comunes como letras y digitos

def generar_contraseña(longitud: int = 12) -> str:
    """
    Genera una contraseña segura de la longitud especificada.

    Args:
        longitud (int): longitud de la contraseña.

    Returns:
        str: La contraseña generada.
    """
    # Combina letras (mayusculas y minusculas), digitos y caracteres especiales
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Genera una contraseña seleccionando aleatoriamente caracteres del conjunto
    contraseña = "".join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    """
    Función principal para interactuar con el usuario.
    Permite ingresar la longitud deseada de la contraseña y la genera.
    """
    while True:
        try:
            # Solicita al usuario la longitud deseada para la contraseña.
            longitud = int(input(" Ingrese la longitud de la contraseña:  "))
            if longitud < 8: # Verifica si la longitud cumple con el mínimo requerido.
                print("La longitud mínima es 8 caracteres.")
            else:
                break # Sale del bucle si la longitud es válida.
        except ValueError:
             # Maneja errores si el usuario no ingresa un número válido.
            print(" Ingrese un valor numérico ")

 # Genera la contraseña con la longitud proporcionada.
    contraseña = generar_contraseña(longitud)
    print(" Contraseña generada:",   contraseña)

# Punto de entrada del programa.
if __name__ == "__main__":
    main()
