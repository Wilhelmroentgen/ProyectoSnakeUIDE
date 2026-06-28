"""
Archivo: settings.py
Descripción:
    Este archivo centraliza todas las constantes de configuración del juego.

    Una constante es un valor que se utiliza en varias partes del programa,
    pero que normalmente no cambia durante la ejecución. Por ejemplo:
    - El tamaño de la pantalla.
    - El tamaño de cada celda.
    - Los colores.
    - La velocidad inicial del juego.
    - Las rutas de archivos de sonido.
    - La ruta donde se guarda el puntaje máximo.

    La razón principal para tener este archivo separado es mantener el código
    más ordenado. Si en el futuro se desea cambiar el tamaño de la pantalla,
    el color de la serpiente o la velocidad del juego, no será necesario buscar
    esos valores dentro de todos los archivos del proyecto, sino solamente
    modificar este archivo.
"""


# ============================================================
# CONFIGURACIÓN GENERAL DE LA VENTANA
# ============================================================

# Ancho de la ventana principal del juego, expresado en píxeles.
# En este caso, el tablero tendrá 400 píxeles de ancho.
SCREEN_WIDTH = 600

# Alto de la ventana principal del juego, expresado en píxeles.
# En este caso, el tablero tendrá 400 píxeles de alto.
SCREEN_HEIGHT = 600

# Tamaño de cada celda del tablero.
# La serpiente no se mueve píxel por píxel, sino por bloques.
# Cada bloque mide 20x20 píxeles.
#
# Esto facilita la lógica del juego porque todas las posiciones quedan
# alineadas a una cuadrícula.
CELL_SIZE = 20


# ============================================================
# CONFIGURACIÓN DE VELOCIDAD
# ============================================================

# Velocidad inicial del juego.
# FPS significa "frames per second", es decir, cuadros por segundo.
# En este juego, también se usa para controlar cuántas veces por segundo
# se actualiza la lógica principal.
#
# Mientras mayor sea este número, más rápido se moverá la serpiente.
FPS = 5

# Velocidad máxima permitida.
# Aunque el juego tenga dificultad progresiva, se establece un límite para evitar
# que la serpiente llegue a moverse demasiado rápido y el juego se vuelva
# prácticamente imposible de controlar.
MAX_FPS = 15

# Cantidad de puntos necesarios para aumentar la velocidad.
# Por ejemplo, si este valor es 100:
# - De 0 a 99 puntos se usa la velocidad inicial.
# - Al llegar a 100 puntos, aumenta en 1 el FPS.
# - Al llegar a 200 puntos, aumenta nuevamente.
#
# Esta lógica se aplica en game.py, dentro del método get_current_fps().
SPEED_INCREASE_EVERY = 100


# ============================================================
# COLORES PRINCIPALES
# ============================================================

# Pygame utiliza colores en formato RGB.
# RGB significa Red, Green, Blue.
# Cada valor va de 0 a 255.
#
# Ejemplo:
# (255, 0, 0) sería rojo puro.
# (0, 255, 0) sería verde puro.
# (0, 0, 255) sería azul puro.

# Color de fondo del tablero.
# Se usa un gris muy oscuro para dar contraste a la serpiente, la comida y textos.
BACKGROUND_COLOR = (18, 18, 18)

# Color de la cuadrícula.
# Es un gris un poco más claro que el fondo.
# Su objetivo es ayudar visualmente al jugador a percibir las celdas del tablero
# sin distraer demasiado.
GRID_COLOR = (35, 35, 35)

# Color del cuerpo de la serpiente.
# Se usa verde porque tradicionalmente la serpiente se representa con este color.
SNAKE_COLOR = (0, 200, 80)

# Color de la cabeza de la serpiente.
# Se usa un verde más brillante para diferenciar claramente la cabeza del cuerpo.
# Esto ayuda al jugador a identificar la dirección actual del movimiento.
SNAKE_HEAD_COLOR = (0, 255, 120)

# Color de la comida.
# Se usa rojo porque contrasta bien con el fondo oscuro y con la serpiente verde.
FOOD_COLOR = (220, 40, 40)

# Color principal de los textos.
# El blanco permite buena lectura sobre fondo oscuro.
TEXT_COLOR = (255, 255, 255)

# Color usado para el mensaje de Game Over.
# Se usa rojo claro porque visualmente se asocia con error, alerta o finalización.
GAME_OVER_COLOR = (255, 80, 80)

# Color usado para destacar información importante, como el récord.
# Se usa un tono amarillo para diferenciarlo del texto normal.
HIGHLIGHT_COLOR = (255, 220, 100)


# ============================================================
# TÍTULOS Y TEXTOS
# ============================================================

# Título que aparece en la barra superior de la ventana del juego.
WINDOW_TITLE = "Juego de la Serpiente"


# ============================================================
# ARCHIVOS DEL PROYECTO
# ============================================================

# Ruta del archivo donde se guardará el puntaje máximo.
#
# Se utiliza una carpeta llamada data para separar los datos generados por
# el programa del código fuente.
#
# El archivo high_score.txt será creado automáticamente si no existe.
HIGH_SCORE_FILE = "data/high_score.txt"


# ============================================================
# SONIDOS
# ============================================================

# Variable general para activar o desactivar los sonidos del juego.
#
# Si está en True, el sistema intentará cargar y reproducir sonidos.
# Si está en False, el juego funcionará sin sonidos.
#
# Esta opción es útil porque los sonidos son una mejora visual/auditiva,
# pero no son indispensables para la lógica principal del juego.
SOUND_ENABLED = True

# Ruta del sonido que se reproduce cuando la serpiente come.
EAT_SOUND_PATH = "assets/sounds/eat.wav"

# Ruta del sonido que se reproduce cuando ocurre Game Over.
GAME_OVER_SOUND_PATH = "assets/sounds/game_over.wav"

# Ruta del sonido que se reproduce al iniciar o reiniciar una partida.
START_SOUND_PATH = "assets/sounds/start.wav"