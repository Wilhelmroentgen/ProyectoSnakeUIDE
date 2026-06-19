"""
Archivo: game_state.py
Descripción:
    Este archivo define los estados principales del juego.

    Un estado representa la situación actual en la que se encuentra el programa.
    Por ejemplo, el juego puede estar ejecutándose, puede haber terminado o puede
    estar listo para cerrarse.

    Utilizar estados permite controlar el flujo del juego de una forma más clara,
    ordenada y mantenible.
"""

# Se importa Enum para crear una enumeración.
# Una enumeración permite definir un conjunto cerrado de valores constantes.
from enum import Enum


class GameState(Enum):
    """
    Enumeración que representa los posibles estados del juego.

    Cada valor indica una condición general del programa y permite que el
    controlador principal sepa qué acciones debe ejecutar.
    """

    # Estado que indica que la partida está activa.
    # Mientras el juego esté en RUNNING, la serpiente se mueve,
    # se leen los controles y se verifican las colisiones.
    RUNNING = "running"

    # Estado que indica que la partida terminó.
    # Se activa cuando la serpiente choca contra una pared o contra su cuerpo.
    GAME_OVER = "game_over"

    # Estado que indica que el programa debe cerrarse.
    # Se activa cuando el usuario presiona ESC o cierra la ventana.
    EXIT = "exit"