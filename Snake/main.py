"""
Archivo: main.py
Descripción:
    Este archivo es el punto de entrada principal del programa.

    Su responsabilidad es iniciar el Juego de la Serpiente de forma ordenada.
    No contiene la lógica completa del juego, ya que esa responsabilidad está
    delegada a la clase Game ubicada en src/core/game.py.

    Además, este archivo valida que el programa se ejecute con Python 3.13,
    debido a que esta versión es la utilizada para instalar y ejecutar Pygame
    correctamente en este proyecto.
"""


# Se importa sys para consultar información sobre la versión de Python
# que está ejecutando el programa.
import sys


# Se importa la clase Game, que contiene el controlador principal del juego.
from src.core.game import Game


def validate_python_version():
    """
    Valida que el programa se ejecute con Python 3.13.

    Esta validación evita problemas de compatibilidad con librerías externas,
    especialmente con Pygame. Si el usuario ejecuta el programa con otra versión
    de Python, se muestra un mensaje explicativo y el programa se detiene.
    """

    # Obtiene la versión mayor de Python.
    # Por ejemplo, en Python 3.13, major sería 3.
    major = sys.version_info.major

    # Obtiene la versión menor de Python.
    # Por ejemplo, en Python 3.13, minor sería 13.
    minor = sys.version_info.minor

    # Verifica que la versión sea exactamente Python 3.13.
    if major != 3 or minor != 13:

        # Muestra un mensaje indicando la versión requerida.
        print("Este proyecto debe ejecutarse con Python 3.13.")

        # Muestra la versión detectada en el sistema actual.
        print(f"Versión actual detectada: Python {major}.{minor}")

        # Indica el comando correcto para ejecutar el programa.
        print("Ejecuta el programa usando:")
        print("py -3.13 main.py")

        # Finaliza el programa con código de error.
        sys.exit(1)


def main():
    """
    Función principal del programa.

    Esta función primero valida la versión de Python y luego crea una instancia
    del juego. Finalmente, ejecuta el ciclo principal mediante el método run().
    """

    # Valida que se esté usando la versión correcta de Python.
    validate_python_version()

    # Crea una instancia del controlador principal del juego.
    game = Game()

    # Ejecuta el ciclo principal del juego.
    game.run()


# Esta condición permite que el programa se ejecute únicamente cuando
# main.py se llama directamente, y no cuando se importa desde otro archivo.
if __name__ == "__main__":
    main()