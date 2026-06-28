"""
Archivo: sound_system.py
Descripción:
    Este archivo contiene la clase SoundSystem, encargada de manejar los sonidos
    del Juego de la Serpiente.

    Los sonidos son una mejora de experiencia de usuario. No son indispensables
    para que el juego funcione, pero permiten que el usuario reciba retroalimentación
    auditiva cuando:
    - Inicia una partida.
    - La serpiente come.
    - La partida termina.

    Este sistema está diseñado para ser tolerante a errores. Es decir, si faltan
    los archivos de sonido o si Pygame no puede inicializar el mezclador de audio,
    el juego continúa funcionando sin cerrarse.
"""

import os
import pygame

from src.config.settings import (
    SOUND_ENABLED,
    EAT_SOUND_PATH,
    GAME_OVER_SOUND_PATH,
    START_SOUND_PATH
)


class SoundSystem:
    """
    Sistema encargado de administrar los sonidos del juego.

    Responsabilidades:
    - Inicializar el sistema de audio.
    - Cargar sonidos desde archivos.
    - Reproducir sonidos en eventos específicos.
    - Evitar que el juego falle si no existen archivos de sonido.
    """

    def __init__(self):
        """
        Constructor del sistema de sonido.

        Primero revisa si los sonidos están habilitados desde settings.py.
        Luego intenta inicializar pygame.mixer y cargar los archivos disponibles.
        """

        # Indica si los sonidos están habilitados.
        # Este valor viene desde settings.py.
        self.enabled = SOUND_ENABLED

        # Variables donde se guardarán los sonidos cargados.
        # Inicialmente son None porque aún no se han cargado.
        self.eat_sound = None
        self.game_over_sound = None
        self.start_sound = None

        # Si los sonidos están desactivados desde configuración,
        # no se intenta cargar nada.
        if not self.enabled:
            return

        try:
            # Inicializa el sistema de audio de Pygame.
            # mixer es el módulo encargado de reproducir sonidos.
            pygame.mixer.init()

            # Carga el sonido de comer.
            self.eat_sound = self.load_sound(EAT_SOUND_PATH)

            # Carga el sonido de Game Over.
            self.game_over_sound = self.load_sound(GAME_OVER_SOUND_PATH)

            # Carga el sonido de inicio o reinicio de partida.
            self.start_sound = self.load_sound(START_SOUND_PATH)

        except pygame.error:
            # Si ocurre un error al iniciar el sistema de audio,
            # se desactivan los sonidos para evitar que el juego falle.
            self.enabled = False

    def load_sound(self, path):
        """
        Carga un archivo de sonido si existe.

        Parámetros:
            path:
                Ruta del archivo de sonido.

        Retorna:
            pygame.mixer.Sound:
                Si el archivo existe y se carga correctamente.
            None:
                Si el archivo no existe o no se puede cargar.

        Decisión de diseño:
            Se valida la existencia del archivo antes de cargarlo para evitar
            errores cuando el proyecto aún no tiene sonidos agregados.
        """

        # Si el archivo no existe, se retorna None.
        # Esto permite que el juego continúe sin sonido.
        if not os.path.exists(path):
            return None

        try:
            # Intenta cargar el archivo de sonido.
            return pygame.mixer.Sound(path)

        except pygame.error:
            # Si Pygame no puede leer el archivo, se retorna None.
            # Esto puede ocurrir si el archivo está dañado o no es compatible.
            return None

    def play_sound(self, sound):
        """
        Reproduce un sonido si está disponible.

        Parámetros:
            sound:
                Objeto pygame.mixer.Sound o None.

        Este método centraliza la reproducción para no repetir la misma validación
        en play_eat(), play_game_over() y play_start().
        """

        # Solo reproduce si:
        # - El sistema de sonido está habilitado.
        # - El sonido fue cargado correctamente.
        if self.enabled and sound is not None:
            sound.play()

    def play_eat(self):
        """
        Reproduce el sonido cuando la serpiente come.

        Este método se llama desde game.py cuando se detecta colisión entre
        la serpiente y la comida.
        """

        self.play_sound(self.eat_sound)

    def play_game_over(self):
        """
        Reproduce el sonido de fin de partida.

        Este método se llama cuando la serpiente choca contra una pared
        o contra su propio cuerpo.
        """

        self.play_sound(self.game_over_sound)

    def play_start(self):
        """
        Reproduce el sonido de inicio o reinicio de partida.

        Este método se llama cuando el usuario inicia la partida desde la pantalla
        inicial o reinicia después de perder.
        """

        self.play_sound(self.start_sound)