"""
Archivo: food.py
Descripción:
    Este archivo contiene la clase Food, encargada de representar la comida
    dentro del Juego de la Serpiente.

    La comida es uno de los elementos principales del juego, ya que permite
    aumentar el puntaje y hacer crecer a la serpiente cuando esta la alcanza.

    Este módulo se encarga de:
    - Generar una posición aleatoria para la comida.
    - Evitar que la comida aparezca encima del cuerpo de la serpiente.
    - Reubicar la comida cada vez que la serpiente la consume.

    La posición de la comida se maneja mediante coordenadas (x, y), alineadas
    al tamaño de celda definido en la configuración general del juego.
"""


# Se importa el módulo random para generar posiciones aleatorias dentro del tablero.
import random


# Se importan las constantes necesarias desde el archivo de configuración.
# CELL_SIZE define el tamaño de cada celda del tablero.
# SCREEN_WIDTH y SCREEN_HEIGHT definen los límites de la ventana del juego.
from src.config.settings import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT


class Food:
    """
    Representa la comida que debe comer la serpiente.

    La comida tiene una posición dentro del tablero. Cuando la serpiente
    alcanza esa posición, se considera que la comida fue consumida y debe
    generarse una nueva en otra ubicación válida.
    """

    def __init__(self, snake_body):
        """
        Constructor de la clase Food.

        Parámetros:
            snake_body:
                Lista de coordenadas que representan el cuerpo actual de la
                serpiente. Se utiliza para evitar que la comida se genere
                sobre una posición ocupada por la serpiente.

        Al crear un objeto Food, se genera inmediatamente una posición válida
        para la comida.
        """

        # Se asigna a la comida una posición inicial aleatoria.
        # La posición se genera verificando que no coincida con el cuerpo
        # de la serpiente.
        self.position = self.generate_position(snake_body)

    def generate_position(self, snake_body):
        """
        Genera una posición aleatoria válida para la comida.

        Parámetros:
            snake_body:
                Lista de posiciones ocupadas por la serpiente.

        Retorna:
            tuple:
                Una coordenada en formato (x, y), donde x representa la posición
                horizontal y y representa la posición vertical dentro del tablero.

        Restricción:
            La comida no puede aparecer encima de ninguna parte del cuerpo
            de la serpiente.
        """

        # Calcula el valor máximo de X en unidades de celda.
        # Se resta CELL_SIZE para asegurar que la comida no salga del área visible.
        max_x = (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE

        # Calcula el valor máximo de Y en unidades de celda.
        # Esto asegura que la posición generada esté dentro del tablero.
        max_y = (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE

        # Se utiliza un ciclo infinito controlado.
        # El ciclo se repetirá hasta encontrar una posición que no esté ocupada
        # por el cuerpo de la serpiente.
        while True:

            # Genera una coordenada X aleatoria alineada a la cuadrícula.
            # Primero se genera un número de celda y luego se multiplica
            # por CELL_SIZE para convertirlo a píxeles.
            x = random.randint(0, max_x) * CELL_SIZE

            # Genera una coordenada Y aleatoria alineada a la cuadrícula.
            y = random.randint(0, max_y) * CELL_SIZE

            # Verifica que la posición generada no esté ocupada por la serpiente.
            # Si la posición está libre, se devuelve como ubicación válida
            # para la comida.
            if (x, y) not in snake_body:
                return (x, y)

    def respawn(self, snake_body):
        """
        Genera una nueva posición para la comida.

        Este método se llama cuando la serpiente consume la comida actual.
        En lugar de crear un nuevo objeto Food, simplemente se actualiza
        la posición del objeto existente.

        Parámetros:
            snake_body:
                Lista de posiciones ocupadas por la serpiente. Se usa para
                evitar que la nueva comida aparezca sobre la serpiente.
        """

        # Actualiza la posición de la comida usando el mismo método de generación
        # aleatoria validada.
        self.position = self.generate_position(snake_body)