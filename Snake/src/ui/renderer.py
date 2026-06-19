"""
Archivo: renderer.py
Descripción:
    Este archivo contiene la clase Renderer, encargada de dibujar los elementos
    principales del Juego de la Serpiente.

    La función de este módulo es separar la lógica visual de la lógica del juego.
    Esto significa que la serpiente, la comida y el puntaje se calculan en otros
    módulos, pero se dibujan en pantalla desde esta clase.

    Este módulo se encarga de:
    - Limpiar la pantalla.
    - Dibujar la cuadrícula.
    - Dibujar la serpiente.
    - Dibujar la comida.
    - Dibujar el puntaje.
    - Actualizar la ventana del juego.
"""


# Se importa Pygame para utilizar funciones de dibujo, fuentes y rectángulos.
import pygame


# Se importan los colores, tamaños y dimensiones definidos en settings.py.
# Esto permite centralizar la configuración visual del juego.
from src.config.settings import (
    BACKGROUND_COLOR,
    GRID_COLOR,
    SNAKE_COLOR,
    SNAKE_HEAD_COLOR,
    FOOD_COLOR,
    TEXT_COLOR,
    CELL_SIZE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)


class Renderer:
    """
    Clase encargada de dibujar los elementos principales del juego.

    Esta clase recibe la pantalla principal de Pygame y utiliza métodos gráficos
    para representar visualmente el estado actual del juego.
    """

    def __init__(self, screen):
        """
        Constructor de la clase Renderer.

        Parámetros:
            screen:
                Superficie principal de Pygame donde se dibujan todos los
                elementos visuales del juego.
        """

        # Guarda la referencia a la pantalla principal.
        self.screen = screen

        # Crea una fuente de texto para mostrar el puntaje.
        # Se utiliza Arial con tamaño 24.
        self.font = pygame.font.SysFont("Arial", 24)

    def clear_screen(self):
        """
        Limpia la pantalla con el color de fondo.

        Este método se ejecuta en cada ciclo del juego para borrar el dibujo
        anterior antes de dibujar la nueva posición de los elementos.
        """

        # Rellena toda la pantalla con el color de fondo.
        self.screen.fill(BACKGROUND_COLOR)

    def draw_grid(self):
        """
        Dibuja una cuadrícula de apoyo visual.

        La cuadrícula permite visualizar claramente las celdas por donde se
        mueve la serpiente. Cada línea se dibuja de acuerdo con el tamaño
        definido por CELL_SIZE.
        """

        # Dibuja líneas verticales desde el borde superior hasta el borde inferior.
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (x, 0),
                (x, SCREEN_HEIGHT)
            )

        # Dibuja líneas horizontales desde el borde izquierdo hasta el borde derecho.
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (0, y),
                (SCREEN_WIDTH, y)
            )

    def draw_snake(self, snake):
        """
        Dibuja la serpiente en pantalla.

        Parámetros:
            snake:
                Objeto Snake que contiene la lista de segmentos del cuerpo.

        Funcionamiento:
            Cada segmento de la serpiente se dibuja como un rectángulo.
            El primer segmento corresponde a la cabeza y se representa con
            un color diferente para distinguirla del cuerpo.
        """

        # Recorre todos los segmentos del cuerpo de la serpiente.
        for index, segment in enumerate(snake.body):

            # Si el índice es 0, significa que el segmento es la cabeza.
            # La cabeza se dibuja con un color más brillante.
            color = SNAKE_HEAD_COLOR if index == 0 else SNAKE_COLOR

            # Crea un rectángulo en la posición del segmento.
            # Cada segmento tiene el tamaño de una celda.
            rect = pygame.Rect(
                segment[0],
                segment[1],
                CELL_SIZE,
                CELL_SIZE
            )

            # Dibuja el rectángulo en la pantalla.
            # border_radius suaviza las esquinas para que se vea mejor.
            pygame.draw.rect(self.screen, color, rect, border_radius=4)

    def draw_food(self, food):
        """
        Dibuja la comida en pantalla.

        Parámetros:
            food:
                Objeto Food que contiene la posición actual de la comida.
        """

        # Crea un rectángulo usando la posición actual de la comida.
        rect = pygame.Rect(
            food.position[0],
            food.position[1],
            CELL_SIZE,
            CELL_SIZE
        )

        # Dibuja la comida con color rojo y bordes redondeados.
        # Esto permite diferenciarla visualmente de la serpiente.
        pygame.draw.rect(self.screen, FOOD_COLOR, rect, border_radius=8)

    def draw_score(self, score):
        """
        Dibuja el puntaje actual en pantalla.

        Parámetros:
            score:
                Puntaje actual del jugador.
        """

        # Crea el texto del puntaje usando la fuente definida en el constructor.
        score_text = self.font.render(f"Puntaje: {score}", True, TEXT_COLOR)

        # Dibuja el texto en la esquina superior izquierda de la pantalla.
        self.screen.blit(score_text, (10, 10))

    def update_display(self):
        """
        Actualiza la pantalla del juego.

        En Pygame, los dibujos realizados no aparecen visualmente hasta que
        se actualiza la pantalla. Este método muestra todos los cambios hechos
        durante el ciclo actual.
        """

        # Actualiza completamente la ventana del juego.
        pygame.display.flip()