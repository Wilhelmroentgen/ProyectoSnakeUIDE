"""
Archivo: main.py
Descripción:
    Este archivo es el punto de entrada principal del proyecto.

    Punto de entrada significa que este es el primer archivo que se ejecuta
    cuando el usuario inicia el programa.

    Este archivo no contiene la lógica completa del juego, porque esa lógica
    está organizada dentro de la clase Game. Su responsabilidad es:
    - Validar la versión de Python.
    - Crear el objeto principal del juego.
    - Ejecutar el ciclo principal.
"""

import sys

from src.core.game import Game


def validate_python_version():
    """
    Valida que el programa se ejecute con Python 3.13.

    Motivo:
        El proyecto fue probado con Python 3.13 y Pygame.
        En algunas versiones más nuevas, como Python 3.14, puede haber problemas
        de compatibilidad o instalación con ciertas librerías.

    Si la versión no es Python 3.13, el programa muestra un mensaje y se detiene.
    """

    # Versión principal de Python.
    # En Python 3.13, major es 3.
    major = sys.version_info.major

    # Versión secundaria de Python.
    # En Python 3.13, minor es 13.
    minor = sys.version_info.minor

    # Verifica que sea exactamente Python 3.13.
    if major != 3 or minor != 13:

        # Mensajes explicativos para el usuario.
        print("Este proyecto debe ejecutarse con Python 3.13.")
        print(f"Versión actual detectada: Python {major}.{minor}")
        print("Ejecuta el programa usando:")
        print("py -3.13 main.py")

        # Finaliza el programa con código de error.
        sys.exit(1)


def main():
    """
    Función principal del programa.

    Esta función organiza el inicio del juego.
    """

    # Primero se valida la versión de Python.
    validate_python_version()

    # Se crea el objeto Game.
    # Este objeto inicializa Pygame, la ventana y todos los módulos internos.
    game = Game()

    # Se ejecuta el ciclo principal del juego.
    game.run()


# Esta condición permite que main() se ejecute solo cuando este archivo
# se ejecuta directamente.
#
# Si main.py fuera importado desde otro archivo, esta parte no se ejecutaría
# automáticamente.
if __name__ == "__main__":
    main()