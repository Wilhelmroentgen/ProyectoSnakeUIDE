# Código Fuente – Juego de la Serpiente

## Descripción

Esta carpeta contiene el código fuente del proyecto **Juego de la Serpiente**, desarrollado en Python utilizando la librería Pygame.

El objetivo de esta sección del proyecto es organizar todos los archivos necesarios para ejecutar el videojuego, separando el código por módulos según su responsabilidad dentro del sistema.

La estructura del código permite identificar claramente qué archivo se encarga de la configuración, cuál controla la lógica principal, cuál representa a la serpiente, cuál administra la comida, cuál verifica colisiones, cuál maneja el puntaje, cuál dibuja los elementos visuales y cuál muestra las pantallas especiales del juego.

---

## Objetivo del código

El objetivo del código es implementar un videojuego funcional donde el usuario pueda controlar una serpiente dentro de un tablero, recolectar comida, aumentar su puntaje, superar su récord y evitar colisionar contra los bordes o contra el propio cuerpo de la serpiente.

El código fue desarrollado aplicando los contenidos de la asignatura **Lógica de Programación I**, como variables, tipos de datos, operadores, condicionales, ciclos, listas, tuplas, diccionarios, funciones, módulos, depuración y organización de algoritmos.

---

## Tecnologías utilizadas

* Python 3.13
* Pygame
* Visual Studio Code

---

## Estructura de la carpeta de código

```text
codigo/
│
├── main.py
├── requirements.txt
├── run_game.bat
├── install_dependencies.bat
│
├── assets/
│   └── sounds/
│       ├── eat.wav
│       ├── game_over.wav
│       └── start.wav
│
├── data/
│   └── high_score.txt
│
└── src/
    ├── config/
    │   └── settings.py
    │
    ├── core/
    │   ├── game.py
    │   ├── game_state.py
    │   └── input_handler.py
    │
    ├── entities/
    │   ├── snake.py
    │   └── food.py
    │
    ├── systems/
    │   ├── collision_system.py
    │   ├── score_system.py
    │   └── sound_system.py
    │
    ├── ui/
    │   ├── renderer.py
    │   └── screens.py
    │
    └── utils/
        └── helpers.py
```

---

## Descripción de archivos principales

### `main.py`

Es el punto de entrada principal del programa. Valida que el proyecto se ejecute con Python 3.13, crea una instancia del juego y ejecuta el ciclo principal.

---

### `requirements.txt`

Contiene la dependencia principal del proyecto:

```text
pygame>=2.6.1
```

Este archivo permite instalar las librerías necesarias para ejecutar el juego.

---

### `run_game.bat`

Archivo de ejecución para Windows. Permite iniciar el juego usando Python 3.13 sin escribir manualmente el comando en la terminal.

---

### `install_dependencies.bat`

Archivo auxiliar para instalar las dependencias del proyecto desde `requirements.txt`.

---

## Carpeta `src/config`

Contiene la configuración general del juego.

### `settings.py`

Define valores globales como:

* Tamaño de la pantalla.
* Tamaño de las celdas.
* Velocidad inicial.
* Velocidad máxima.
* Colores principales.
* Título de la ventana.
* Ruta del archivo de récord.
* Rutas de sonidos.

---

## Carpeta `src/core`

Contiene la lógica central de control del juego.

### `game.py`

Es el controlador principal del sistema. Coordina la ejecución del juego, procesa eventos, actualiza la lógica, dibuja la pantalla, controla estados, reproduce sonidos y aplica la dificultad progresiva.

### `game_state.py`

Define los estados principales del juego:

* `START_SCREEN`: pantalla inicial.
* `RUNNING`: partida en ejecución.
* `GAME_OVER`: partida finalizada.
* `EXIT`: cierre del programa.

### `input_handler.py`

Interpreta las teclas presionadas por el jugador. Convierte las flechas del teclado en direcciones lógicas y detecta teclas especiales como `ENTER`, `R` y `ESC`.

---

## Carpeta `src/entities`

Contiene las entidades principales del juego.

### `snake.py`

Representa a la serpiente. Administra su cuerpo, posición, dirección, movimiento, crecimiento y buffer de entrada para mejorar la fluidez del control.

### `food.py`

Representa la comida. Genera posiciones aleatorias dentro del tablero y evita que la comida aparezca sobre el cuerpo de la serpiente.

---

## Carpeta `src/systems`

Contiene sistemas especializados de lógica.

### `collision_system.py`

Verifica colisiones del juego:

* Colisión con paredes.
* Colisión con el propio cuerpo.
* Colisión con la comida.
* Condiciones de Game Over.

### `score_system.py`

Administra el puntaje actual y el puntaje máximo. El récord se guarda en un archivo dentro de la carpeta `data`.

### `sound_system.py`

Carga y reproduce sonidos del juego. Maneja sonidos para inicio de partida, comida y Game Over. Si los archivos de sonido no existen, el juego continúa funcionando sin detenerse.

---

## Carpeta `src/ui`

Contiene los módulos visuales del juego.

### `renderer.py`

Dibuja los elementos principales durante la partida:

* Fondo.
* Cuadrícula.
* Serpiente.
* Comida.
* Puntaje actual.
* Récord.

### `screens.py`

Muestra pantallas especiales, como:

* Pantalla inicial.
* Pantalla de Game Over.

---

## Carpeta `src/utils`

Contiene archivos auxiliares.

### `helpers.py`

Archivo reservado para futuras funciones auxiliares del proyecto. Actualmente no contiene lógica adicional, pero se mantiene para respetar la arquitectura modular.

---

## Carpeta `assets/sounds`

Contiene los archivos de sonido del juego:

```text
eat.wav
game_over.wav
start.wav
```

Estos sonidos se reproducen cuando la serpiente come, cuando ocurre Game Over y cuando inicia o reinicia una partida.

---

## Carpeta `data`

Contiene archivos generados por el programa.

### `high_score.txt`

Guarda el puntaje máximo alcanzado por el jugador. Si el archivo no existe, el sistema lo crea automáticamente cuando se supera un récord.

---

## Instalación

Para instalar las dependencias del proyecto, ejecutar el siguiente comando desde la carpeta del código:

```bash
py -3.13 -m pip install -r requirements.txt
```

También se puede ejecutar:

```text
install_dependencies.bat
```

---

## Ejecución

Para iniciar el juego, ejecutar:

```bash
py -3.13 main.py
```

También se puede ejecutar:

```text
run_game.bat
```

---

## Controles del juego

| Tecla            | Acción                              |
| ---------------- | ----------------------------------- |
| `ENTER`          | Iniciar partida                     |
| Flecha arriba    | Mover hacia arriba                  |
| Flecha abajo     | Mover hacia abajo                   |
| Flecha izquierda | Mover hacia la izquierda            |
| Flecha derecha   | Mover hacia la derecha              |
| `R`              | Reiniciar partida después de perder |
| `ESC`            | Salir del juego                     |

---

## Funcionalidades implementadas

* Pantalla inicial con instrucciones.
* Movimiento de la serpiente mediante teclado.
* Sistema de input buffer para mejorar la fluidez del control.
* Generación aleatoria de comida.
* Validación para evitar comida sobre la serpiente.
* Crecimiento de la serpiente al comer.
* Puntaje actual.
* Puntaje máximo o récord.
* Almacenamiento del récord en archivo.
* Detección de colisiones con paredes.
* Detección de colisiones con el propio cuerpo.
* Pantalla de Game Over.
* Reinicio de partida.
* Salida del juego.
* Dificultad progresiva.
* Sonidos básicos.
* Organización modular del código.

---

## Fecha

Junio de 2026

---

## Autor

Erick Pries
Carrera: Ingeniería en Ciberseguridad
Materia: Lógica de Programación I
Universidad Internacional del Ecuador
