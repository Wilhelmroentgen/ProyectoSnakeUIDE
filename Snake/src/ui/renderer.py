"""
Archivo: renderer.py
Descripción:
    Este archivo contiene la clase Renderer, encargada de dibujar los elementos
    principales del juego.

    Se separa el renderizado en una clase propia para mantener la lógica visual
    fuera del controlador principal. Esto permite que game.py se encargue de
    coordinar el juego, mientras renderer.py se encarga de dibujar.

    Este módulo dibuja:
    - Fondo.
    - Cuadrícula.
    - Serpiente.
    - Comida.
    - Puntaje actual.
    - Puntaje máximo.
"""

import pygame

from src.config.settings import (
    BACKGROUND_COLOR,
    GRID_COLOR,
    SNAKE_COLOR,
    SNAKE_HEAD_COLOR,
    FOOD_COLOR,
    TEXT_COLOR,
    HIGHLIGHT_COLOR,
    CELL_SIZE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)


class Renderer:
    """
    Clase encargada de renderizar los elementos visuales del juego.

    Renderizar significa dibujar en pantalla los elementos que forman parte
    de la partida.
    """

    def __init__(self, screen):
        """
        Constructor del renderizador.

        Parámetros:
            screen:
                Superficie principal de Pygame donde se dibuja todo el juego.

        Decisión de diseño:
            El objeto screen se crea en game.py porque allí se inicializa la ventana.
            Renderer recibe esa pantalla y la utiliza para dibujar.
        """

        # Guarda la pantalla principal.
        self.screen = screen

        # Fuente utilizada para mostrar puntaje y récord.
        # Se usa Arial tamaño 22 para que quepa bien en una ventana de 400x400.
        self.font = pygame.font.SysFont("Arial", 22)

    def clear_screen(self):
        """
        Limpia la pantalla antes de dibujar el siguiente frame.

        En videojuegos, la pantalla se redibuja muchas veces por segundo.
        Si no se limpia antes de dibujar, los elementos anteriores quedarían
        marcados y se produciría un efecto visual incorrecto.
        """

        # Rellena toda la superficie con el color de fondo.
        self.screen.fill(BACKGROUND_COLOR)

    def draw_grid(self):
        """
        Dibuja la cuadrícula del tablero.

        La cuadrícula ayuda a visualizar las celdas por donde se mueve la serpiente.
        Cada línea se dibuja separada por CELL_SIZE píxeles.
        """

        # Dibuja líneas verticales.
        # range(0, SCREEN_WIDTH, CELL_SIZE) genera posiciones:
        # 0, 20, 40, 60, etc.
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(
                self.screen,       # Superficie donde se dibuja.
                GRID_COLOR,        # Color de la línea.
                (x, 0),            # Punto inicial de la línea.
                (x, SCREEN_HEIGHT) # Punto final de la línea.
            )

        # Dibuja líneas horizontales.
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (0, y),
                (SCREEN_WIDTH, y)
            )

    def draw_snake(self, snake):
        """
        Dibuja la serpiente.

        Parámetros:
            snake:
                Objeto Snake que contiene la lista de coordenadas del cuerpo.

        Funcionamiento:
            La serpiente se representa como una lista de segmentos.
            Cada segmento se dibuja como un rectángulo de tamaño CELL_SIZE.
            El primer segmento es la cabeza.
        """

        # enumerate permite recorrer la lista y obtener:
        # - index: posición del segmento en la lista.
        # - segment: coordenada del segmento.
        for index, segment in enumerate(snake.body):

            # Si index es 0, se trata de la cabeza.
            # La cabeza se dibuja con un color distinto.
            color = SNAKE_HEAD_COLOR if index == 0 else SNAKE_COLOR

            # Crea un rectángulo en la posición del segmento.
            # segment[0] es la coordenada X.
            # segment[1] es la coordenada Y.
            rect = pygame.Rect(
                segment[0],
                segment[1],
                CELL_SIZE,
                CELL_SIZE
            )

            # Dibuja el rectángulo.
            # border_radius=4 redondea ligeramente las esquinas para mejorar
            # la apariencia visual.
            pygame.draw.rect(self.screen, color, rect, border_radius=4)

    def draw_food(self, food):
        """
        Dibuja la comida.

        Parámetros:
            food:
                Objeto Food que contiene la posición actual de la comida.

        La comida también se dibuja como un rectángulo, pero con color rojo
        y bordes más redondeados.
        """

        # Crea el rectángulo de la comida.
        rect = pygame.Rect(
            food.position[0],
            food.position[1],
            CELL_SIZE,
            CELL_SIZE
        )

        # Dibuja la comida en pantalla.
        pygame.draw.rect(self.screen, FOOD_COLOR, rect, border_radius=8)

    def draw_score(self, score, high_score):
        """
        Dibuja el puntaje actual y el puntaje máximo.

        Parámetros:
            score:
                Puntaje actual de la partida.

            high_score:
                Puntaje máximo guardado.

        Decisión de diseño:
            Se muestran ambos valores en la parte superior izquierda porque es
            una ubicación visible, pero no interfiere demasiado con el tablero.
        """

        # Crea la superficie de texto para el puntaje actual.
        score_text = self.font.render(
            f"Puntaje: {score}",
            True,
            TEXT_COLOR
        )

        # Crea la superficie de texto para el récord.
        high_score_text = self.font.render(
            f"Récord: {high_score}",
            True,
            HIGHLIGHT_COLOR
        )

        # Dibuja el puntaje en la posición (10, 8).
        self.screen.blit(score_text, (10, 8))

        # Dibuja el récord debajo del puntaje.
        self.screen.blit(high_score_text, (10, 32))

    def update_display(self):
        """
        Actualiza la pantalla.

        En Pygame, dibujar elementos sobre la superficie no siempre los muestra
        inmediatamente. pygame.display.flip() actualiza la ventana completa para
        que el usuario vea el frame actual.
        """

        pygame.display.flip()