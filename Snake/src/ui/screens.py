"""
Archivo: screens.py
Descripción:
    Este archivo contiene la clase Screens, encargada de mostrar pantallas
    o mensajes especiales dentro del Juego de la Serpiente.

    A diferencia de Renderer, que dibuja elementos normales del juego como la
    serpiente, la comida y el puntaje, esta clase se enfoca en mensajes más
    generales, como la pantalla de Game Over.

    Este módulo permite:
    - Dibujar textos centrados.
    - Mostrar el mensaje de fin de partida.
    - Mostrar instrucciones para reiniciar o salir del juego.
"""


# Se importa Pygame para crear fuentes y dibujar texto en pantalla.
import pygame


# Se importan dimensiones y colores definidos en settings.py.
from src.config.settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TEXT_COLOR,
    GAME_OVER_COLOR
)


class Screens:
    """
    Clase encargada de mostrar pantallas o mensajes especiales.

    Esta clase ayuda a separar la presentación de mensajes importantes
    del resto de la lógica visual del juego.
    """

    def __init__(self, screen):
        """
        Constructor de la clase Screens.

        Parámetros:
            screen:
                Superficie principal de Pygame donde se dibujarán los textos.
        """

        # Guarda la pantalla principal donde se dibujarán los mensajes.
        self.screen = screen

        # Fuente grande para títulos importantes, como GAME OVER.
        self.title_font = pygame.font.SysFont("Arial", 48)

        # Fuente más pequeña para mensajes secundarios e instrucciones.
        self.text_font = pygame.font.SysFont("Arial", 26)

    def draw_centered_text(self, text, font, color, y_position):
        """
        Dibuja un texto centrado horizontalmente.

        Parámetros:
            text:
                Texto que se desea mostrar en pantalla.

            font:
                Fuente que se utilizará para renderizar el texto.

            color:
                Color del texto en formato RGB.

            y_position:
                Posición vertical donde se ubicará el texto.

        Este método evita repetir código cada vez que se necesita dibujar
        un texto centrado.
        """

        # Convierte el texto en una superficie gráfica que Pygame puede dibujar.
        rendered_text = font.render(text, True, color)

        # Obtiene el rectángulo del texto y lo centra horizontalmente.
        # La coordenada X se ubica en la mitad de la pantalla.
        text_rect = rendered_text.get_rect(
            center=(SCREEN_WIDTH // 2, y_position)
        )

        # Dibuja el texto renderizado en la pantalla.
        self.screen.blit(rendered_text, text_rect)

    def draw_game_over(self, score):
        """
        Muestra la pantalla de Game Over.

        Parámetros:
            score:
                Puntaje final alcanzado por el jugador.

        Esta pantalla aparece cuando la serpiente choca contra una pared
        o contra su propio cuerpo.
        """

        # Dibuja el título principal de fin de juego.
        self.draw_centered_text(
            "GAME OVER",
            self.title_font,
            GAME_OVER_COLOR,
            SCREEN_HEIGHT // 2 - 80
        )

        # Dibuja el puntaje final obtenido por el jugador.
        self.draw_centered_text(
            f"Puntaje final: {score}",
            self.text_font,
            TEXT_COLOR,
            SCREEN_HEIGHT // 2
        )

        # Dibuja la instrucción para reiniciar la partida.
        self.draw_centered_text(
            "Presiona R para reiniciar",
            self.text_font,
            TEXT_COLOR,
            SCREEN_HEIGHT // 2 + 50
        )

        # Dibuja la instrucción para salir del juego.
        self.draw_centered_text(
            "Presiona ESC para salir",
            self.text_font,
            TEXT_COLOR,
            SCREEN_HEIGHT // 2 + 90
        )