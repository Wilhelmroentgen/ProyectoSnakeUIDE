"""
Archivo: snake.py
Descripción:
    Este archivo contiene la clase Snake, encargada de representar y controlar
    la serpiente dentro del juego.

    La serpiente es la entidad principal controlada por el jugador. Su lógica
    incluye:
    - Posición inicial.
    - Movimiento por celdas.
    - Dirección actual.
    - Crecimiento al comer.
    - Buffer de entrada para mejorar la respuesta del control.
    - Obtención de la posición de la cabeza para detectar colisiones.

    La serpiente se representa como una lista de coordenadas. Cada coordenada
    corresponde a una parte del cuerpo. El primer elemento de la lista representa
    la cabeza, y los demás elementos representan el cuerpo.
"""


# Se importa deque desde collections.
# deque permite manejar una cola eficiente de direcciones pendientes.
# En este juego se usa como buffer de entrada para guardar comandos rápidos
# del jugador sin causar giros inválidos.
from collections import deque


# Se importan constantes generales del juego.
# CELL_SIZE define cuánto avanza la serpiente en cada movimiento.
# SCREEN_WIDTH y SCREEN_HEIGHT se usan para calcular la posición inicial.
from src.config.settings import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT


class Snake:
    """
    Representa a la serpiente del juego.

    Esta clase administra la información y comportamiento principal de la
    serpiente, incluyendo su cuerpo, dirección, movimiento y crecimiento.
    """

    def __init__(self):
        """
        Constructor de la clase Snake.

        Al crear una serpiente, se llama al método reset para inicializarla
        con su tamaño, posición y dirección inicial.
        """

        # Inicializa la serpiente en su estado inicial.
        self.reset()

    def reset(self):
        """
        Reinicia la serpiente a su estado inicial.

        Este método se utiliza al comenzar una partida nueva o al reiniciar
        después de un Game Over.
        """

        # Calcula la posición horizontal inicial en el centro de la pantalla.
        start_x = SCREEN_WIDTH // 2

        # Calcula la posición vertical inicial en el centro de la pantalla.
        start_y = SCREEN_HEIGHT // 2

        # Define el cuerpo inicial de la serpiente.
        # La serpiente inicia con tres segmentos:
        # - La cabeza en el centro.
        # - Dos segmentos hacia la izquierda.
        #
        # Esto hace que la serpiente pueda comenzar moviéndose hacia la derecha
        # sin chocar inmediatamente consigo misma.
        self.body = [
            (start_x, start_y),
            (start_x - CELL_SIZE, start_y),
            (start_x - (CELL_SIZE * 2), start_y)
        ]

        # Dirección actual de movimiento de la serpiente.
        # Al iniciar, la serpiente se mueve hacia la derecha.
        self.direction = "RIGHT"

        # Buffer de direcciones pendientes.
        # Permite guardar hasta 2 direcciones ingresadas rápidamente por el jugador.
        #
        # Esto mejora la fluidez del control y evita errores cuando el usuario
        # presiona varias teclas en muy poco tiempo.
        self.direction_buffer = deque(maxlen=2)

        # Bandera que indica si la serpiente debe crecer en el siguiente movimiento.
        # Inicialmente es False porque la serpiente no ha comido todavía.
        self.grow_next_move = False

    def move(self):
        """
        Mueve la serpiente una celda en la dirección actual.

        Antes de realizar el movimiento, se verifica si existe una dirección
        pendiente en el buffer de entrada. Si existe, se aplica esa dirección.

        La lógica del movimiento consiste en:
        1. Calcular la nueva posición de la cabeza.
        2. Insertar esa nueva cabeza al inicio del cuerpo.
        3. Eliminar el último segmento si la serpiente no debe crecer.
        """

        # Si existen direcciones pendientes en el buffer, se toma la primera.
        # popleft() extrae el elemento más antiguo, manteniendo el orden en que
        # el jugador presionó las teclas.
        if self.direction_buffer:
            self.direction = self.direction_buffer.popleft()

        # Obtiene la posición actual de la cabeza de la serpiente.
        # La cabeza siempre corresponde al primer elemento de la lista body.
        head_x, head_y = self.body[0]

        # Calcula la nueva posición de la cabeza según la dirección actual.
        # La serpiente se mueve exactamente una celda por actualización.
        if self.direction == "UP":
            new_head = (head_x, head_y - CELL_SIZE)

        elif self.direction == "DOWN":
            new_head = (head_x, head_y + CELL_SIZE)

        elif self.direction == "LEFT":
            new_head = (head_x - CELL_SIZE, head_y)

        else:
            # Si no es UP, DOWN o LEFT, se asume que la dirección es RIGHT.
            new_head = (head_x + CELL_SIZE, head_y)

        # Inserta la nueva cabeza al inicio de la lista del cuerpo.
        # Esto representa el avance de la serpiente.
        self.body.insert(0, new_head)

        # Si la serpiente debe crecer, no se elimina el último segmento.
        # De esta manera, el cuerpo queda con una unidad adicional de longitud.
        if self.grow_next_move:
            self.grow_next_move = False

        else:
            # Si la serpiente no debe crecer, se elimina el último segmento.
            # Esto mantiene el mismo tamaño y genera la ilusión de movimiento.
            self.body.pop()

    def queue_direction(self, new_direction):
        """
        Agrega una nueva dirección al buffer de entrada si es válida.

        Parámetros:
            new_direction:
                Dirección solicitada por el jugador. Puede ser:
                "UP", "DOWN", "LEFT", "RIGHT" o None.

        Funcionamiento:
            Este método permite que el jugador presione teclas rápidamente
            sin que el juego produzca colisiones falsas o giros imposibles.

            Por ejemplo, si la serpiente va hacia la derecha y el jugador presiona
            rápidamente abajo e izquierda, el buffer puede guardar ambos movimientos
            y ejecutarlos en orden:
                RIGHT -> DOWN -> LEFT

            Sin buffer, el juego podría interpretar cambios demasiado rápidos y
            provocar una colisión no deseada.
        """

        # Si no se recibió una dirección válida, no se realiza ninguna acción.
        # Esto ocurre cuando el usuario presiona una tecla que no corresponde
        # a las flechas de movimiento.
        if new_direction is None:
            return

        # Diccionario que define las direcciones opuestas.
        # Se utiliza para evitar que la serpiente gire directamente hacia atrás.
        opposite_directions = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }

        # La dirección de referencia será:
        # - La última dirección pendiente si el buffer tiene elementos.
        # - La dirección actual si el buffer está vacío.
        #
        # Esto es importante porque permite validar correctamente una secuencia
        # rápida de movimientos.
        last_direction = (
            self.direction_buffer[-1]
            if self.direction_buffer
            else self.direction
        )

        # Evita guardar la misma dirección repetida.
        # Por ejemplo, si la serpiente ya va hacia la derecha, no tiene sentido
        # agregar varias veces la dirección RIGHT al buffer.
        if new_direction == last_direction:
            return

        # Evita giros directos hacia la dirección opuesta.
        # Por ejemplo:
        # - Si va hacia RIGHT, no puede ir directamente a LEFT.
        # - Si va hacia UP, no puede ir directamente a DOWN.
        #
        # Esta regla evita que la serpiente choque inmediatamente consigo misma
        # por un movimiento imposible.
        if new_direction == opposite_directions[last_direction]:
            return

        # Si la dirección pasó todas las validaciones, se agrega al buffer.
        # La cola tiene un tamaño máximo de 2, por lo que no se acumulan demasiados
        # movimientos pendientes.
        self.direction_buffer.append(new_direction)

    def grow(self):
        """
        Indica que la serpiente debe crecer en el siguiente movimiento.

        Este método se llama cuando la serpiente come la comida. En lugar de
        aumentar el tamaño inmediatamente, se activa una bandera para que el
        crecimiento ocurra durante el siguiente movimiento.
        """

        # Activa la bandera de crecimiento.
        # En el siguiente move(), la serpiente no eliminará su último segmento.
        self.grow_next_move = True

    def get_head_position(self):
        """
        Devuelve la posición actual de la cabeza de la serpiente.

        Retorna:
            tuple:
                Coordenada (x, y) correspondiente a la cabeza de la serpiente.

        Este método es utilizado por otros sistemas, especialmente por el sistema
        de colisiones, para saber si la serpiente tocó una pared, su cuerpo
        o la comida.
        """

        # La cabeza siempre es el primer elemento de la lista body.
        return self.body[0]