"""
Archivo: collision_system.py
Descripción:
    Este archivo contiene la clase CollisionSystem, encargada de verificar
    las colisiones dentro del Juego de la Serpiente.

    En este juego existen tres tipos principales de validación:
    - Colisión con las paredes.
    - Colisión con el propio cuerpo de la serpiente.
    - Colisión con la comida.

    El sistema de colisiones es fundamental porque determina cuándo termina
    una partida y cuándo la serpiente debe crecer o aumentar el puntaje.
"""


# Se importan las dimensiones de la pantalla.
# Estos valores permiten verificar si la serpiente salió de los límites
# visibles del tablero.
from src.config.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class CollisionSystem:
    """
    Sistema encargado de detectar colisiones.

    Esta clase agrupa métodos relacionados con la verificación de contactos
    entre la serpiente, los bordes del tablero, su propio cuerpo y la comida.

    Sus métodos son estáticos porque no necesitan guardar información interna.
    Solo reciben objetos como parámetros, realizan validaciones y devuelven
    resultados booleanos.
    """

    @staticmethod
    def check_wall_collision(snake):
        """
        Verifica si la cabeza de la serpiente chocó contra los bordes de la pantalla.

        Parámetros:
            snake:
                Objeto de tipo Snake que contiene la posición actual de la serpiente.

        Retorna:
            bool:
                True si la cabeza de la serpiente está fuera de los límites
                de la pantalla.
                False si la serpiente continúa dentro del área válida.
        """

        # Obtiene la posición actual de la cabeza de la serpiente.
        head_x, head_y = snake.get_head_position()

        # Verifica si la serpiente salió por el borde izquierdo o derecho.
        # Si head_x es menor que 0, salió por la izquierda.
        # Si head_x es mayor o igual que SCREEN_WIDTH, salió por la derecha.
        if head_x < 0 or head_x >= SCREEN_WIDTH:
            return True

        # Verifica si la serpiente salió por el borde superior o inferior.
        # Si head_y es menor que 0, salió por arriba.
        # Si head_y es mayor o igual que SCREEN_HEIGHT, salió por abajo.
        if head_y < 0 or head_y >= SCREEN_HEIGHT:
            return True

        # Si no se cumple ninguna condición anterior, no existe colisión con pared.
        return False

    @staticmethod
    def check_self_collision(snake):
        """
        Verifica si la cabeza de la serpiente chocó contra su propio cuerpo.

        Parámetros:
            snake:
                Objeto de tipo Snake que contiene la lista de segmentos del cuerpo.

        Retorna:
            bool:
                True si la cabeza de la serpiente ocupa la misma posición que
                algún segmento de su cuerpo.
                False si no existe colisión consigo misma.
        """

        # Obtiene la posición de la cabeza.
        head = snake.get_head_position()

        # Obtiene el cuerpo sin incluir la cabeza.
        # Esto es necesario porque la cabeza siempre coincide con ella misma,
        # por lo que no debe incluirse en la comparación.
        body_without_head = snake.body[1:]

        # Si la cabeza aparece dentro del cuerpo, significa que la serpiente
        # chocó consigo misma.
        return head in body_without_head

    @staticmethod
    def check_food_collision(snake, food):
        """
        Verifica si la serpiente comió la comida.

        Parámetros:
            snake:
                Objeto de tipo Snake.
            food:
                Objeto de tipo Food.

        Retorna:
            bool:
                True si la posición de la cabeza de la serpiente coincide con
                la posición de la comida.
                False en caso contrario.
        """

        # La serpiente come la comida cuando la cabeza ocupa exactamente
        # la misma coordenada que la comida.
        return snake.get_head_position() == food.position

    @staticmethod
    def check_game_over(snake):
        """
        Verifica si existe alguna condición de fin de juego.

        Parámetros:
            snake:
                Objeto de tipo Snake.

        Retorna:
            bool:
                True si la serpiente chocó con una pared o consigo misma.
                False si el juego puede continuar.

        Condiciones de fin de juego:
            - Colisión con los bordes del tablero.
            - Colisión con el propio cuerpo de la serpiente.
        """

        # El juego termina si se cumple cualquiera de las dos condiciones:
        # 1. La serpiente choca contra una pared.
        # 2. La serpiente choca contra su propio cuerpo.
        return (
            CollisionSystem.check_wall_collision(snake)
            or CollisionSystem.check_self_collision(snake)
        )