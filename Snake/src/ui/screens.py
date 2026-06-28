"""
Archivo: screens.py
Descripción:
    Este archivo contiene la clase Screens, encargada de mostrar pantallas
    especiales del juego.

    A diferencia de Renderer, que dibuja elementos durante la partida, esta clase
    dibuja pantallas con mensajes más generales, como:
    - Pantalla inicial.
    - Pantalla de Game Over.

    Separar estas pantallas permite que el código visual sea más claro y ordenado.
"""

import pygame

from src.config.settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TEXT_COLOR,
    GAME_OVER_COLOR,
    HIGHLIGHT_COLOR
)


class Screens:
    """
    Clase encargada de mostrar pantallas especiales del juego.

    Esta clase ayuda a evitar que game.py se llene de instrucciones para dibujar
    textos. En su lugar, game.py simplemente llama:
        self.screens.draw_start_screen(...)
        self.screens.draw_game_over(...)
    """

    def __init__(self, screen):
        """
        Constructor de Screens.

        Parámetros:
            screen:
                Superficie principal donde se dibujarán los textos.
        """

        self.screen = screen

        # Fuente grande para títulos principales.
        # Se usa tamaño 40 para que el título se vea bien en una ventana de 600x500.
        self.title_font = pygame.font.SysFont("Arial", 40)

        # Fuente mediana para subtítulos, puntaje final y récord.
        self.subtitle_font = pygame.font.SysFont("Arial", 28)

        # Fuente normal para instrucciones.
        self.text_font = pygame.font.SysFont("Arial", 23)

        # Fuente pequeña para mensajes secundarios.
        self.small_font = pygame.font.SysFont("Arial", 20)

    def draw_centered_text(self, text, font, color, y_position):
        """
        Dibuja un texto centrado horizontalmente.

        Parámetros:
            text:
                Texto que se desea mostrar.

            font:
                Fuente que se utilizará.

            color:
                Color del texto.

            y_position:
                Posición vertical del texto.
        """

        rendered_text = font.render(text, True, color)

        text_rect = rendered_text.get_rect(
            center=(SCREEN_WIDTH // 2, y_position)
        )

        self.screen.blit(rendered_text, text_rect)

    def draw_start_screen(self, high_score):
        """
        Muestra la pantalla inicial del juego.

        Parámetros:
            high_score:
                Puntaje máximo guardado.

        Esta pantalla aparece cuando el programa inicia. Su objetivo es explicar
        al usuario cómo jugar antes de comenzar la partida.
        """

        # Título principal.
        # Ahora hay más espacio porque la ventana mide 600x500.
        self.draw_centered_text(
            "JUEGO DE LA SERPIENTE",
            self.title_font,
            HIGHLIGHT_COLOR,
            SCREEN_HEIGHT // 2 - 155
        )

        # Línea decorativa simple.
        self.draw_centered_text(
            "────────────────────",
            self.small_font,
            TEXT_COLOR,
            SCREEN_HEIGHT // 2 - 115
        )

        # Instrucciones principales.
        self.draw_centered_text(
            "Usa las flechas del teclado para moverte",
            self.text_font,
            TEXT_COLOR,
            SCREEN_HEIGHT // 2 - 65
        )

        self.draw_centered_text(
            "Come la comida roja para ganar puntos",
            self.text_font,
            TEXT_COLOR,
            SCREEN_HEIGHT // 2 - 30
        )

        self.draw_centered_text(
            "Evita chocar contra las paredes o tu cuerpo",
            self.text_font,
            TEXT_COLOR,
            SCREEN_HEIGHT // 2 + 5
        )

        # Récord actual.
        self.draw_centered_text(
            f"Récord actual: {high_score}",
            self.subtitle_font,
            HIGHLIGHT_COLOR,
            SCREEN_HEIGHT // 2 + 60
        )

        # Instrucciones de inicio y salida.
        self.draw_centered_text(
            "Presiona ENTER para iniciar",
            self.text_font,
            TEXT_COLOR,
            SCREEN_HEIGHT // 2 + 125
        )

        self.draw_centered_text(
            "Presiona ESC para salir",
            self.text_font,
            TEXT_COLOR,
            SCREEN_HEIGHT // 2 + 160
        )

    def draw_game_over(self, score, high_score):
        """
        Muestra la pantalla de Game Over.

        Parámetros:
            score:
                Puntaje final obtenido en la partida.

            high_score:
                Puntaje máximo guardado.
        """

        self.draw_centered_text(
            "GAME OVER",
            self.title_font,
            GAME_OVER_COLOR,
            SCREEN_HEIGHT // 2 - 120
        )

        self.draw_centered_text(
            f"Puntaje final: {score}",
            self.subtitle_font,
            TEXT_COLOR,
            SCREEN_HEIGHT // 2 - 55
        )

        self.draw_centered_text(
            f"Récord: {high_score}",
            self.subtitle_font,
            HIGHLIGHT_COLOR,
            SCREEN_HEIGHT // 2 - 15
        )

        self.draw_centered_text(
            "Presiona R para reiniciar",
            self.text_font,
            TEXT_COLOR,
            SCREEN_HEIGHT // 2 + 65
        )

        # Aquí estaba el error.
        # Antes faltaba TEXT_COLOR, por eso Python decía que faltaba y_position.
        self.draw_centered_text(
            "Presiona ESC para salir",
            self.text_font,
            TEXT_COLOR,
            SCREEN_HEIGHT // 2 + 100
        )