"""
Archivo: game.py
Descripción:
    Este archivo contiene la clase Game, que funciona como controlador principal
    del Juego de la Serpiente.

    El controlador principal es responsable de coordinar todos los módulos:
    - Inicialización de Pygame.
    - Creación de ventana.
    - Creación de serpiente y comida.
    - Procesamiento de eventos.
    - Actualización de lógica.
    - Renderizado.
    - Control de estados.
    - Sonidos.
    - Dificultad progresiva.

    Este archivo no debe encargarse de todos los detalles internos.
    Por eso delega responsabilidades a otras clases como Snake, Food,
    ScoreSystem, SoundSystem, Renderer y Screens.
"""

import pygame

from src.config.settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    MAX_FPS,
    SPEED_INCREASE_EVERY,
    WINDOW_TITLE
)

from src.core.game_state import GameState
from src.core.input_handler import InputHandler

from src.entities.snake import Snake
from src.entities.food import Food

from src.systems.collision_system import CollisionSystem
from src.systems.score_system import ScoreSystem
from src.systems.sound_system import SoundSystem

from src.ui.renderer import Renderer
from src.ui.screens import Screens


class Game:
    """
    Controlador principal del Juego de la Serpiente.

    Esta clase une todos los módulos del juego y administra el ciclo principal.
    """

    def __init__(self):
        """
        Inicializa el juego, sus módulos principales y el estado inicial.

        Este método se ejecuta automáticamente cuando se crea un objeto Game.
        """

        # Inicializa todos los módulos de Pygame.
        pygame.init()

        # Crea la ventana principal del juego.
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Establece el título de la ventana.
        pygame.display.set_caption(WINDOW_TITLE)

        # Crea el reloj del juego.
        # Se usa para controlar la velocidad de ejecución del ciclo principal.
        self.clock = pygame.time.Clock()

        # Crea la serpiente inicial.
        self.snake = Snake()

        # Crea la comida inicial.
        # Se envía el cuerpo de la serpiente para evitar que la comida
        # aparezca encima de ella.
        self.food = Food(self.snake.body)

        # Crea el sistema de puntaje.
        self.score_system = ScoreSystem()

        # Crea el sistema de sonidos.
        self.sound_system = SoundSystem()

        # Crea el renderizador de elementos del juego.
        self.renderer = Renderer(self.screen)

        # Crea el administrador de pantallas especiales.
        self.screens = Screens(self.screen)

        # Estado inicial del programa.
        # Ahora el juego no inicia directamente corriendo, sino mostrando
        # una pantalla inicial.
        self.state = GameState.START_SCREEN

        # Variable para evitar que el sonido de Game Over se reproduzca muchas veces.
        #
        # Sin esta variable, como el ciclo principal sigue ejecutándose mientras
        # el estado es GAME_OVER, el sonido podría repetirse en cada frame.
        self.game_over_sound_played = False

    def get_current_fps(self):
        """
        Calcula la velocidad actual del juego según el puntaje.

        Retorna:
            int:
                FPS actual que debe usar el ciclo principal.

        Lógica:
            Se parte de una velocidad inicial definida por FPS.
            Luego se calcula un bono de velocidad en función del puntaje.

        Ejemplo:
            Si SPEED_INCREASE_EVERY = 100:
            - 0 puntos   -> FPS base.
            - 100 puntos -> FPS + 1.
            - 200 puntos -> FPS + 2.

        La función min() impide superar MAX_FPS.
        """

        # Obtiene el puntaje actual.
        score = self.score_system.get_score()

        # Calcula cuántas veces el puntaje ha alcanzado el intervalo de aumento.
        # La división entera // devuelve solo la parte entera.
        speed_bonus = score // SPEED_INCREASE_EVERY

        # Suma el bono a la velocidad inicial.
        current_fps = FPS + speed_bonus

        # Devuelve la velocidad calculada sin permitir superar MAX_FPS.
        return min(current_fps, MAX_FPS)

    def reset_game(self):
        """
        Reinicia todos los elementos principales del juego.

        Este método se usa:
        - Cuando el jugador presiona ENTER desde la pantalla inicial.
        - Cuando el jugador presiona R después de perder.

        Reinicia:
        - Serpiente.
        - Comida.
        - Puntaje.
        - Estado del juego.
        - Bandera del sonido Game Over.
        """

        # Reinicia la serpiente a su tamaño y posición inicial.
        self.snake.reset()

        # Genera comida en una nueva posición válida.
        self.food.respawn(self.snake.body)

        # Reinicia el puntaje actual.
        # No reinicia el high score.
        self.score_system.reset()

        # Permite que el sonido de Game Over pueda reproducirse nuevamente
        # cuando ocurra una nueva pérdida.
        self.game_over_sound_played = False

        # Cambia el estado a RUNNING para iniciar la partida.
        self.state = GameState.RUNNING

        # Reproduce sonido de inicio o reinicio.
        self.sound_system.play_start()

    def handle_events(self):
        """
        Procesa todos los eventos del usuario.

        En cada ciclo del juego, Pygame guarda eventos pendientes.
        Este método los revisa y responde según el estado actual del juego.
        """

        # Recorre la lista de eventos generados por Pygame.
        for event in pygame.event.get():

            # Si el usuario cierra la ventana con la X,
            # se cambia el estado a EXIT.
            if event.type == pygame.QUIT:
                self.state = GameState.EXIT

            # Si el usuario presiona ESC, también se cambia a EXIT.
            if InputHandler.is_exit_key(event):
                self.state = GameState.EXIT

            # Si el juego está en la pantalla inicial:
            if self.state == GameState.START_SCREEN:

                # ENTER inicia la partida.
                if InputHandler.is_start_key(event):
                    self.reset_game()

            # Si la partida está activa:
            elif self.state == GameState.RUNNING:

                # Se obtiene la dirección ingresada por teclado.
                new_direction = InputHandler.get_direction(event)

                # La dirección se envía a la serpiente.
                # La serpiente decide si la dirección es válida y la agrega
                # al buffer de entrada.
                self.snake.queue_direction(new_direction)

            # Si la partida terminó:
            elif self.state == GameState.GAME_OVER:

                # R reinicia la partida.
                if InputHandler.is_restart_key(event):
                    self.reset_game()

    def update(self):
        """
        Actualiza la lógica interna del juego.

        Este método se ejecuta en cada ciclo, pero solo actualiza la partida
        si el estado actual es RUNNING.

        Aquí ocurre la lógica principal:
        - Mover la serpiente.
        - Revisar si comió.
        - Aumentar puntaje.
        - Generar nueva comida.
        - Revisar colisiones.
        - Cambiar a Game Over si corresponde.
        """

        # Si el juego no está corriendo, no se actualiza la lógica.
        # Esto evita que la serpiente se mueva en la pantalla inicial o Game Over.
        if self.state != GameState.RUNNING:
            return

        # Mueve la serpiente una celda.
        self.snake.move()

        # Verifica si la cabeza de la serpiente coincide con la comida.
        if CollisionSystem.check_food_collision(self.snake, self.food):

            # Activa el crecimiento de la serpiente.
            self.snake.grow()

            # Aumenta el puntaje.
            self.score_system.increase(10)

            # Genera nueva comida.
            self.food.respawn(self.snake.body)

            # Reproduce sonido de comida.
            self.sound_system.play_eat()

        # Verifica condiciones de fin de juego.
        if CollisionSystem.check_game_over(self.snake):

            # Cambia el estado a Game Over.
            self.state = GameState.GAME_OVER

            # Reproduce el sonido de Game Over solo una vez.
            if not self.game_over_sound_played:
                self.sound_system.play_game_over()
                self.game_over_sound_played = True

    def draw(self):
        """
        Dibuja los elementos del juego según el estado actual.

        La pantalla se limpia en cada frame y luego se dibuja lo que corresponde:
        - Pantalla inicial.
        - Partida activa.
        - Pantalla de Game Over.
        """

        # Limpia la pantalla antes de dibujar.
        self.renderer.clear_screen()

        # Si el estado es START_SCREEN, se muestra la pantalla inicial.
        if self.state == GameState.START_SCREEN:
            self.screens.draw_start_screen(
                self.score_system.get_high_score()
            )

        # Si el estado es RUNNING, se dibuja la partida normal.
        elif self.state == GameState.RUNNING:
            self.renderer.draw_grid()
            self.renderer.draw_snake(self.snake)
            self.renderer.draw_food(self.food)
            self.renderer.draw_score(
                self.score_system.get_score(),
                self.score_system.get_high_score()
            )

        # Si el estado es GAME_OVER, se dibuja el tablero congelado
        # y encima se muestra la pantalla de Game Over.
        elif self.state == GameState.GAME_OVER:
            self.renderer.draw_grid()
            self.renderer.draw_snake(self.snake)
            self.renderer.draw_food(self.food)
            self.renderer.draw_score(
                self.score_system.get_score(),
                self.score_system.get_high_score()
            )
            self.screens.draw_game_over(
                self.score_system.get_score(),
                self.score_system.get_high_score()
            )

        # Actualiza la ventana para mostrar todo lo dibujado.
        self.renderer.update_display()

    def run(self):
        """
        Ejecuta el ciclo principal del juego.

        Este ciclo se mantiene activo mientras el estado no sea EXIT.

        En cada vuelta:
        1. Procesa eventos.
        2. Actualiza la lógica.
        3. Dibuja la pantalla.
        4. Controla la velocidad.
        """

        while self.state != GameState.EXIT:

            # Procesa teclado y cierre de ventana.
            self.handle_events()

            # Actualiza lógica de juego.
            self.update()

            # Dibuja pantalla.
            self.draw()

            # Controla la velocidad usando dificultad progresiva.
            self.clock.tick(self.get_current_fps())

        # Cuando se sale del ciclo, se cierra Pygame correctamente.
        pygame.quit()
