"""
Archivo: score_system.py
Descripción:
    Este archivo contiene la clase ScoreSystem, encargada de administrar
    el puntaje del jugador durante la partida.

    Separar el puntaje en un sistema independiente permite mantener la lógica
    del juego más organizada. De esta forma, el controlador principal no maneja
    directamente el valor del puntaje, sino que delega esa responsabilidad a
    esta clase.

    Este módulo permite:
    - Inicializar el puntaje.
    - Reiniciar el puntaje.
    - Aumentar el puntaje.
    - Consultar el puntaje actual.
"""


class ScoreSystem:
    """
    Sistema encargado de administrar el puntaje del juego.

    El puntaje representa el progreso del jugador. Cada vez que la serpiente
    come una comida, el puntaje aumenta.
    """

    def __init__(self):
        """
        Constructor de la clase ScoreSystem.

        Al crear el sistema de puntaje, el valor inicial se establece en cero,
        ya que al comenzar una partida el jugador todavía no ha obtenido puntos.
        """

        # Variable que almacena el puntaje actual del jugador.
        self.score = 0

    def reset(self):
        """
        Reinicia el puntaje a cero.

        Este método se utiliza cuando inicia una nueva partida o cuando
        el jugador decide reiniciar después de perder.
        """

        # Se restablece el puntaje inicial.
        self.score = 0

    def increase(self, points=10):
        """
        Aumenta el puntaje del jugador.

        Parámetros:
            points:
                Cantidad de puntos que se sumarán al puntaje actual.
                Por defecto, cada comida equivale a 10 puntos.
        """

        # Suma los puntos recibidos al puntaje actual.
        self.score += points

    def get_score(self):
        """
        Devuelve el puntaje actual del jugador.

        Retorna:
            int:
                Valor numérico del puntaje acumulado durante la partida.
        """

        # Retorna el valor actual del puntaje para que pueda mostrarse en pantalla.
        return self.score