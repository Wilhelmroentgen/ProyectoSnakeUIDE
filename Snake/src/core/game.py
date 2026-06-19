"""
Archivo: game.py
Descripción:
    Este archivo contiene la clase Game, que funciona como el controlador principal
    del Juego de la Serpiente.

    El controlador principal se encarga de coordinar todos los módulos del sistema:
    - Inicializa la ventana del juego.
    - Crea los objetos principales, como la serpiente y la comida.
    - Procesa los eventos del teclado.
    - Actualiza la lógica del juego.
    - Dibuja los elementos en pantalla.
    - Controla el ciclo principal del programa.

    En términos de arquitectura, este archivo representa el núcleo del sistema.
"""


# Importa la librería Pygame, utilizada para crear la ventana,
# manejar eventos del teclado, dibujar elementos y controlar el tiempo.
import pygame


# Importación de constantes generales del juego.
# Estas constantes se encuentran separadas en settings.py para mantener
# una configuración centralizada y fácil de modificar.
from src.config.settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    WINDOW_TITLE
)


# Importación de los estados del juego.
# Permite saber si el juego está corriendo, finalizado o si debe cerrarse.
from src.core.game_state import GameState

# Importación del módulo encargado de procesar las entradas del teclado.
from src.core.input_handler import InputHandler


# Importación de las entidades principales del juego.
# Snake representa a la serpiente y Food representa la comida.
from src.entities.snake import Snake
from src.entities.food import Food


# Importación de los sistemas de lógica.
# CollisionSystem verifica colisiones.
# ScoreSystem administra el puntaje.
from src.systems.collision_system import CollisionSystem
from src.systems.score_system import ScoreSystem


# Importación de los módulos visuales.
# Renderer dibuja los elementos del juego.
# Screens muestra pantallas o mensajes especiales, como Game Over.
from src.ui.renderer import Renderer
from src.ui.screens import Screens


class Game:
    """
    Controlador principal del Juego de la Serpiente.

    Esta clase integra todos los componentes del programa y administra el ciclo
    principal del juego. Su función no es representar directamente a la serpiente,
    la comida o el puntaje, sino coordinar los módulos responsables de cada tarea.
    """

    def __init__(self):
        """
        Constructor de la clase Game.

        Este método se ejecuta automáticamente cuando se crea una instancia del juego.
        Aquí se inicializa Pygame, se crea la ventana y se instancian todos los
        objetos principales necesarios para que el juego funcione.
        """

        # Inicializa todos los módulos internos de Pygame.
        # Esto es obligatorio antes de crear ventanas, usar fuentes o manejar eventos.
        pygame.init()

        # Crea la ventana principal del juego con el tamaño definido en settings.py.
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Define el título de la ventana.
        pygame.display.set_caption(WINDOW_TITLE)

        # Crea un reloj de Pygame.
        # Este reloj se utiliza para controlar la velocidad del ciclo principal
        # y evitar que el juego corra demasiado rápido.
        self.clock = pygame.time.Clock()

        # Crea la serpiente inicial.
        self.snake = Snake()

        # Crea la comida inicial.
        # Se envía el cuerpo de la serpiente para evitar que la comida aparezca
        # encima de ella.
        self.food = Food(self.snake.body)

        # Crea el sistema de puntaje.
        self.score_system = ScoreSystem()

        # Crea el módulo encargado de dibujar los elementos visuales del juego.
        self.renderer = Renderer(self.screen)

        # Crea el módulo encargado de mostrar pantallas especiales.
        self.screens = Screens(self.screen)

        # Define el estado inicial del juego.
        # En esta versión parcial, el juego inicia directamente en ejecución.
        self.state = GameState.RUNNING

    def reset_game(self):
        """
        Reinicia todos los elementos principales del juego.

        Este método se utiliza cuando el jugador pierde y decide iniciar
        una nueva partida. Restablece la serpiente, la comida, el puntaje
        y el estado general del juego.
        """

        # Reinicia la serpiente a su posición y tamaño inicial.
        self.snake.reset()

        # Genera una nueva comida en una posición válida.
        # Se toma en cuenta el cuerpo de la serpiente para evitar superposición.
        self.food.respawn(self.snake.body)

        # Reinicia el puntaje a cero.
        self.score_system.reset()

        # Cambia el estado del juego a RUNNING para comenzar una nueva partida.
        self.state = GameState.RUNNING

    def handle_events(self):
        """
        Procesa los eventos generados por el usuario.

        En Pygame, los eventos representan acciones externas, como presionar
        teclas, cerrar la ventana o mover el mouse. En este juego se utilizan
        principalmente eventos de teclado y cierre de ventana.
        """

        # Recorre todos los eventos pendientes registrados por Pygame.
        for event in pygame.event.get():

            # Si el usuario presiona el botón de cerrar la ventana,
            # se cambia el estado a EXIT para terminar el ciclo principal.
            if event.type == pygame.QUIT:
                self.state = GameState.EXIT

            # Si el usuario presiona ESC, también se solicita salir del juego.
            if InputHandler.is_exit_key(event):
                self.state = GameState.EXIT

            # Si el juego se encuentra en ejecución, se procesan las teclas
            # de movimiento de la serpiente.
            if self.state == GameState.RUNNING:

                # Convierte la tecla presionada en una dirección lógica:
                # UP, DOWN, LEFT o RIGHT.
                new_direction = InputHandler.get_direction(event)

                # Envía la dirección a la serpiente.
                # La serpiente se encargará de validar si el movimiento es permitido
                # y de guardarlo en su buffer de entrada.
                self.snake.queue_direction(new_direction)

            # Si la partida ya terminó, solo se permite reiniciar.
            elif self.state == GameState.GAME_OVER:

                # Si el jugador presiona la tecla R, se reinicia la partida.
                if InputHandler.is_restart_key(event):
                    self.reset_game()

    def update(self):
        """
        Actualiza la lógica interna del juego.

        Este método se ejecuta en cada iteración del ciclo principal.
        Aquí se mueve la serpiente, se verifica si comió la comida,
        se actualiza el puntaje y se comprueba si ocurrió una colisión.
        """

        # Si el juego no está en estado RUNNING, no debe actualizarse la lógica.
        # Por ejemplo, durante Game Over la serpiente ya no debe moverse.
        if self.state != GameState.RUNNING:
            return

        # Mueve la serpiente una celda en la dirección actual.
        self.snake.move()

        # Verifica si la cabeza de la serpiente coincide con la posición de la comida.
        if CollisionSystem.check_food_collision(self.snake, self.food):

            # Indica que la serpiente debe crecer.
            self.snake.grow()

            # Aumenta el puntaje del jugador en 10 puntos.
            self.score_system.increase(10)

            # Genera una nueva comida en una posición libre del tablero.
            self.food.respawn(self.snake.body)

        # Verifica si ocurrió una condición de fin de juego.
        # Esto incluye colisión con las paredes o con el propio cuerpo.
        if CollisionSystem.check_game_over(self.snake):

            # Si existe una colisión, el estado cambia a GAME_OVER.
            self.state = GameState.GAME_OVER

    def draw(self):
        """
        Dibuja los elementos del juego en pantalla.

        Este método se encarga de actualizar visualmente la ventana.
        Primero limpia la pantalla, luego dibuja los elementos correspondientes
        según el estado actual del juego.
        """

        # Limpia la pantalla con el color de fondo.
        self.renderer.clear_screen()

        # Dibuja la cuadrícula del tablero.
        self.renderer.draw_grid()

        # Si el juego está en ejecución, se dibujan los elementos normales:
        # serpiente, comida y puntaje.
        if self.state == GameState.RUNNING:
            self.renderer.draw_snake(self.snake)
            self.renderer.draw_food(self.food)
            self.renderer.draw_score(self.score_system.get_score())

        # Si el juego terminó, se siguen dibujando los elementos del juego,
        # pero además se muestra la pantalla de Game Over.
        elif self.state == GameState.GAME_OVER:
            self.renderer.draw_snake(self.snake)
            self.renderer.draw_food(self.food)
            self.renderer.draw_score(self.score_system.get_score())
            self.screens.draw_game_over(self.score_system.get_score())

        # Actualiza la ventana para que todos los dibujos se muestren en pantalla.
        self.renderer.update_display()

    def run(self):
        """
        Ejecuta el ciclo principal del juego.

        El ciclo principal mantiene el programa funcionando mientras el estado
        no sea EXIT. En cada vuelta del ciclo se procesan eventos, se actualiza
        la lógica, se dibuja la pantalla y se controla la velocidad del juego.
        """

        # El juego se mantiene activo hasta que el estado cambie a EXIT.
        while self.state != GameState.EXIT:

            # Procesa entradas del usuario y eventos de ventana.
            self.handle_events()

            # Actualiza la lógica interna del juego.
            self.update()

            # Dibuja los elementos visuales en pantalla.
            self.draw()

            # Limita la velocidad del ciclo principal.
            # FPS define cuántas veces por segundo se ejecutará el juego.
            self.clock.tick(FPS)

        # Cierra correctamente los módulos de Pygame al salir del juego.
        pygame.quit()