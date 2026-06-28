"""
Archivo: score_system.py
Descripción:
    Este archivo contiene la clase ScoreSystem, responsable de administrar
    el puntaje actual y el puntaje máximo del jugador.

    En una versión básica del juego solo se necesita un puntaje actual.
    Sin embargo, para una versión más completa se agregó un sistema de
    High Score o récord.

    El puntaje máximo se guarda en un archivo de texto para que no se pierda
    cuando se cierra el programa.
"""

# os permite trabajar con carpetas y archivos del sistema operativo.
# Se usa aquí para verificar si el archivo de récord existe y para crear
# la carpeta data si todavía no existe.
import os

from src.config.settings import HIGH_SCORE_FILE


class ScoreSystem:
    """
    Sistema encargado de administrar el puntaje del juego.

    Responsabilidades:
    - Guardar el puntaje actual.
    - Aumentar el puntaje cuando la serpiente come.
    - Reiniciar el puntaje al comenzar una nueva partida.
    - Cargar el récord desde archivo.
    - Guardar el récord cuando se supera.
    """

    def __init__(self):
        """
        Constructor del sistema de puntaje.

        Al iniciar, el puntaje actual siempre empieza en cero.
        El récord se carga desde el archivo definido en settings.py.
        """

        # Puntaje actual de la partida.
        self.score = 0

        # Puntaje máximo histórico.
        # Se carga desde archivo para conservarlo entre ejecuciones.
        self.high_score = self.load_high_score()

    def load_high_score(self):
        """
        Carga el puntaje máximo desde un archivo de texto.

        Retorna:
            int:
                Puntaje máximo guardado.
                Si no existe archivo o el contenido no es válido, retorna 0.

        Decisión de diseño:
            Se utiliza un archivo .txt porque el dato a guardar es muy simple:
            solamente un número entero. Para este proyecto no se necesita una
            base de datos ni un archivo JSON complejo.
        """

        # Si el archivo no existe, significa que todavía no hay récord guardado.
        # En ese caso se retorna 0.
        if not os.path.exists(HIGH_SCORE_FILE):
            return 0

        try:
            # Abre el archivo en modo lectura.
            # encoding="utf-8" ayuda a evitar problemas con caracteres especiales.
            with open(HIGH_SCORE_FILE, "r", encoding="utf-8") as file:

                # Lee el contenido, elimina espacios o saltos de línea con strip(),
                # y convierte el resultado a entero.
                return int(file.read().strip())

        except ValueError:
            # Si el archivo existe pero contiene texto inválido,
            # se evita que el programa se caiga y se retorna 0.
            return 0

    def save_high_score(self):
        """
        Guarda el puntaje máximo en un archivo de texto.

        Este método se ejecuta cuando el puntaje actual supera el récord anterior.
        """

        # Obtiene el nombre de la carpeta donde se guardará el archivo.
        # En este caso, para "data/high_score.txt", la carpeta es "data".
        folder = os.path.dirname(HIGH_SCORE_FILE)

        # Si la carpeta existe como ruta válida, se crea en caso de que no exista.
        # exist_ok=True evita errores si la carpeta ya fue creada anteriormente.
        if folder:
            os.makedirs(folder, exist_ok=True)

        # Abre el archivo en modo escritura.
        # Si el archivo no existe, Python lo crea automáticamente.
        # Si existe, reemplaza su contenido por el nuevo récord.
        with open(HIGH_SCORE_FILE, "w", encoding="utf-8") as file:
            file.write(str(self.high_score))

    def reset(self):
        """
        Reinicia el puntaje actual a cero.

        Este método se utiliza cada vez que empieza una nueva partida.
        No reinicia el high score, porque el récord debe conservarse.
        """

        self.score = 0

    def increase(self, points=10):
        """
        Aumenta el puntaje actual.

        Parámetros:
            points:
                Cantidad de puntos a sumar.
                Por defecto, cada comida suma 10 puntos.

        Además:
            Si el nuevo puntaje supera el récord, se actualiza el high score
            y se guarda en el archivo correspondiente.
        """

        # Suma los puntos al puntaje actual.
        self.score += points

        # Verifica si el puntaje actual supera el récord histórico.
        if self.score > self.high_score:

            # Actualiza el récord en memoria.
            self.high_score = self.score

            # Guarda el récord en archivo para conservarlo.
            self.save_high_score()

    def get_score(self):
        """
        Devuelve el puntaje actual.

        Este método permite que otros módulos consulten el puntaje sin acceder
        directamente al atributo self.score.
        """

        return self.score

    def get_high_score(self):
        """
        Devuelve el puntaje máximo.

        Este método se usa para mostrar el récord en la pantalla inicial,
        durante la partida y en la pantalla de Game Over.
        """

        return self.high_score