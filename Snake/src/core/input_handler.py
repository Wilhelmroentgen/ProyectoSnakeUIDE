"""
Archivo: input_handler.py
Descripción:
    Este archivo contiene la clase InputHandler, encargada de interpretar
    las entradas del teclado.

    En Pygame, cuando el usuario presiona una tecla, se genera un evento.
    Estos eventos usan constantes propias de Pygame, como pygame.K_UP,
    pygame.K_DOWN, pygame.K_RETURN, etc.

    Para evitar que el controlador principal del juego tenga que trabajar
    directamente con todas esas constantes, esta clase traduce los eventos
    del teclado a valores más simples y entendibles.

    Por ejemplo:
    - pygame.K_UP se convierte en "UP".
    - pygame.K_DOWN se convierte en "DOWN".
    - pygame.K_RETURN se interpreta como inicio de partida.
    - pygame.K_ESCAPE se interpreta como salida del juego.
"""

import pygame


class InputHandler:
    """
    Clase encargada de interpretar los eventos del teclado.

    Sus métodos son estáticos porque no necesitan almacenar información interna.
    Es decir, no hace falta crear un objeto InputHandler para utilizarlos.

    Se puede llamar directamente:
        InputHandler.get_direction(event)
    """

    @staticmethod
    def get_direction(event):
        """
        Convierte una tecla de dirección en una dirección lógica del juego.

        Parámetros:
            event:
                Evento recibido desde Pygame.

        Retorna:
            str:
                "UP", "DOWN", "LEFT" o "RIGHT" si el usuario presionó
                una flecha de dirección.
            None:
                Si el evento no corresponde a una tecla de dirección.

        Decisión de diseño:
            Este método solo detecta qué tecla fue presionada.
            No valida si el movimiento es permitido o no.

            La validación de direcciones opuestas se realiza dentro de la clase
            Snake, porque la serpiente es quien conoce su dirección actual y
            su buffer de movimientos.
        """

        # Si el evento no corresponde a una tecla presionada, no se procesa.
        if event.type != pygame.KEYDOWN:
            return None

        # Flecha arriba.
        # Se devuelve una cadena simple para representar la dirección.
        if event.key == pygame.K_UP:
            return "UP"

        # Flecha abajo.
        if event.key == pygame.K_DOWN:
            return "DOWN"

        # Flecha izquierda.
        if event.key == pygame.K_LEFT:
            return "LEFT"

        # Flecha derecha.
        if event.key == pygame.K_RIGHT:
            return "RIGHT"

        # Si la tecla presionada no es una flecha, no se devuelve dirección.
        return None

    @staticmethod
    def is_start_key(event):
        """
        Verifica si el usuario presionó ENTER para iniciar la partida.

        Este método se utiliza en la pantalla inicial. Mientras el juego está
        en estado START_SCREEN, la tecla ENTER permite comenzar.

        Retorna:
            bool:
                True si el usuario presionó ENTER.
                False en caso contrario.
        """

        return event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN

    @staticmethod
    def is_restart_key(event):
        """
        Verifica si el usuario presionó R para reiniciar la partida.

        Este método se usa principalmente cuando el juego está en GAME_OVER.
        Al presionar R, el programa reinicia la serpiente, la comida y el puntaje.

        Retorna:
            bool:
                True si el usuario presionó la tecla R.
                False en caso contrario.
        """

        return event.type == pygame.KEYDOWN and event.key == pygame.K_r

    @staticmethod
    def is_exit_key(event):
        """
        Verifica si el usuario presionó ESC para salir del juego.

        Esta tecla se puede utilizar desde la pantalla inicial, durante la partida
        o en la pantalla de Game Over.

        Retorna:
            bool:
                True si el usuario presionó ESC.
                False en caso contrario.
        """

        return event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE