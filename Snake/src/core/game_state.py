"""
Archivo: game_state.py
Descripción:
    Este archivo define los estados principales del juego mediante una enumeración.

    Un estado representa la situación actual del programa. En un videojuego,
    no siempre ocurre lo mismo: a veces el usuario está en la pantalla inicial,
    a veces la partida está activa, a veces el jugador perdió y a veces el
    programa debe cerrarse.

    Usar estados permite controlar el flujo del juego de una forma ordenada.
    En lugar de depender de muchas variables sueltas, se usa una sola variable
    llamada state, que puede tomar valores definidos en esta enumeración.
"""

# Enum permite crear un conjunto cerrado de valores.
# Esto significa que GameState solo podrá tener los valores definidos aquí.
from enum import Enum


class GameState(Enum):
    """
    Enumeración que representa los estados posibles del juego.

    Cada estado permite que el controlador principal del juego decida qué hacer:
    - Mostrar la pantalla inicial.
    - Ejecutar la partida.
    - Mostrar Game Over.
    - Cerrar el programa.
    """

    # Estado inicial del juego.
    # El programa se abre mostrando instrucciones y esperando que el usuario
    # presione ENTER para comenzar.
    START_SCREEN = "start_screen"

    # Estado de partida activa.
    # Mientras el juego está en RUNNING:
    # - Se mueve la serpiente.
    # - Se procesan las teclas de dirección.
    # - Se detecta comida.
    # - Se actualiza el puntaje.
    # - Se revisan colisiones.
    RUNNING = "running"

    # Estado de partida finalizada.
    # Se activa cuando la serpiente choca contra una pared o contra su cuerpo.
    GAME_OVER = "game_over"

    # Estado de salida.
    # Se activa cuando el usuario presiona ESC o cierra la ventana.
    EXIT = "exit"