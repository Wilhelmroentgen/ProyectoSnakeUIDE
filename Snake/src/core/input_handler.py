"""
Archivo: input_handler.py
Descripción:
    Este archivo contiene la clase InputHandler, encargada de interpretar
    las entradas del teclado realizadas por el jugador.

    Su función principal es separar la lectura del teclado de la lógica principal
    del juego. De esta forma, el controlador principal no necesita conocer
    directamente las teclas de Pygame, sino que recibe valores más simples como
    "UP", "DOWN", "LEFT" o "RIGHT".

    Esta separación permite mantener el código más ordenado y facilita futuras
    modificaciones en los controles.
"""


# Se importa Pygame para poder acceder a las constantes de teclado,
# como pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT y pygame.K_RIGHT.
import pygame


class InputHandler:
    """
    Clase encargada de procesar las entradas del teclado.

    Esta clase no necesita guardar información interna, por eso sus métodos
    son estáticos. Un método estático puede ser utilizado sin crear un objeto
    de la clase.
    """

    @staticmethod
    def get_direction(event):
        """
        Convierte una tecla presionada en una dirección del juego.

        Parámetros:
            event:
                Evento capturado por Pygame. Puede representar una tecla,
                cierre de ventana u otra acción del usuario.

        Retorna:
            str:
                "UP", "DOWN", "LEFT" o "RIGHT" si el usuario presionó
                una tecla de dirección.
            None:
                Si el evento no corresponde a una tecla de dirección.

        Nota:
            Este método solo interpreta la tecla presionada.
            La validación de movimientos opuestos o repetidos se realiza
            dentro de la clase Snake, específicamente en el buffer de entrada.
        """

        # Si el evento no es una tecla presionada, no se procesa.
        if event.type != pygame.KEYDOWN:
            return None

        # Si el usuario presiona la flecha hacia arriba,
        # se devuelve la dirección lógica "UP".
        if event.key == pygame.K_UP:
            return "UP"

        # Si el usuario presiona la flecha hacia abajo,
        # se devuelve la dirección lógica "DOWN".
        if event.key == pygame.K_DOWN:
            return "DOWN"

        # Si el usuario presiona la flecha hacia la izquierda,
        # se devuelve la dirección lógica "LEFT".
        if event.key == pygame.K_LEFT:
            return "LEFT"

        # Si el usuario presiona la flecha hacia la derecha,
        # se devuelve la dirección lógica "RIGHT".
        if event.key == pygame.K_RIGHT:
            return "RIGHT"

        # Si se presiona cualquier otra tecla, este método no genera dirección.
        return None

    @staticmethod
    def is_restart_key(event):
        """
        Verifica si el usuario presionó la tecla de reinicio.

        Parámetros:
            event:
                Evento capturado por Pygame.

        Retorna:
            bool:
                True si el usuario presionó la tecla R.
                False en cualquier otro caso.
        """

        # La partida se reinicia únicamente cuando el evento corresponde
        # a una tecla presionada y esa tecla es la letra R.
        return event.type == pygame.KEYDOWN and event.key == pygame.K_r

    @staticmethod
    def is_exit_key(event):
        """
        Verifica si el usuario presionó la tecla de salida.

        Parámetros:
            event:
                Evento capturado por Pygame.

        Retorna:
            bool:
                True si el usuario presionó la tecla ESC.
                False en cualquier otro caso.
        """

        # El juego se cierra cuando el usuario presiona ESC.
        return event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE