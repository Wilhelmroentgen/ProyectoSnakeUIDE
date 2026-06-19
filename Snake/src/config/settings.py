"""
Archivo: settings.py
Descripción:
    Este archivo contiene las constantes generales de configuración del juego.

    La finalidad de separar la configuración en un archivo independiente es evitar
    que valores importantes, como el tamaño de la ventana, colores o velocidad del
    juego, estén dispersos en varios módulos del programa.

    De esta forma, si se desea modificar el tamaño del tablero, la velocidad o los
    colores del juego, solo es necesario cambiar los valores en este archivo.
"""


# ============================================================
# CONFIGURACIÓN GENERAL DE LA VENTANA
# ============================================================

# Ancho de la ventana del juego en píxeles.
# En este caso, la ventana tendrá 400 píxeles de ancho.
SCREEN_WIDTH = 400

# Alto de la ventana del juego en píxeles.
# En este caso, la ventana tendrá 400 píxeles de alto.
SCREEN_HEIGHT = 400

# Tamaño de cada celda del tablero en píxeles.
# La serpiente y la comida se moverán en bloques de 20x20 píxeles.
# Esto permite que el movimiento sea ordenado y alineado a una cuadrícula.
CELL_SIZE = 20


# ============================================================
# CONFIGURACIÓN DE VELOCIDAD DEL JUEGO
# ============================================================

# Cantidad de cuadros por segundo.
# Este valor controla la velocidad general del juego.
# Mientras mayor sea el número, más rápido se moverá la serpiente.
FPS = 10


# ============================================================
# COLORES PRINCIPALES DEL JUEGO
# ============================================================

# Color de fondo de la ventana.
# El formato utilizado por Pygame es RGB: (rojo, verde, azul).
# En este caso se usa un gris muy oscuro.
BACKGROUND_COLOR = (18, 18, 18)

# Color de las líneas de la cuadrícula.
# Se usa un gris ligeramente más claro que el fondo para que la cuadrícula
# sea visible sin distraer demasiado al jugador.
GRID_COLOR = (35, 35, 35)

# Color del cuerpo de la serpiente.
# Se utiliza un color verde para representar visualmente a la serpiente.
SNAKE_COLOR = (0, 200, 80)

# Color de la cabeza de la serpiente.
# Se usa un verde más brillante para diferenciar la cabeza del cuerpo.
SNAKE_HEAD_COLOR = (0, 255, 120)

# Color de la comida.
# Se utiliza rojo para que sea fácil de identificar dentro del tablero.
FOOD_COLOR = (220, 40, 40)

# Color general del texto que se muestra en pantalla.
# Blanco, para generar contraste con el fondo oscuro.
TEXT_COLOR = (255, 255, 255)

# Color específico para el mensaje de Game Over.
# Se utiliza un rojo claro para indicar visualmente que la partida terminó.
GAME_OVER_COLOR = (255, 80, 80)


# ============================================================
# TÍTULOS Y TEXTOS GENERALES
# ============================================================

# Título de la ventana que aparecerá en la barra superior del programa.
WINDOW_TITLE = "Juego de la Serpiente"