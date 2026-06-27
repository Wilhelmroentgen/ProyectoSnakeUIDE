# Juego de la Serpiente

## Nombre del proyecto

**Juego de la Serpiente**

---

## Integrantes

* **Erick Pries**

---

## Objetivo del sistema

El objetivo del sistema es desarrollar un videojuego básico e interactivo en Python que permita aplicar los fundamentos de la lógica de programación mediante el control de una serpiente dentro de un tablero.

El jugador debe mover la serpiente utilizando el teclado, recolectar comida, aumentar su puntaje y evitar colisionar contra los bordes del tablero o contra el propio cuerpo de la serpiente. El proyecto busca demostrar el uso de conceptos como variables, tipos de datos, operadores, condicionales, ciclos, listas, tuplas, diccionarios, funciones, diagramas de flujo, depuración y organización modular del código.

---

## Descripción del proyecto

El **Juego de la Serpiente** es un programa desarrollado en Python utilizando la librería Pygame. El sistema presenta una ventana gráfica donde el jugador controla una serpiente que se desplaza dentro de un tablero. La comida aparece en posiciones aleatorias y, cuando la serpiente la alcanza, aumenta el puntaje y el tamaño del cuerpo.

El juego finaliza cuando la serpiente choca contra una pared o contra su propio cuerpo. Al terminar la partida, el sistema muestra una pantalla de Game Over con el puntaje final y el puntaje máximo alcanzado.

---

## Descripción de funcionalidades

El sistema desarrollado incluye las siguientes funcionalidades principales:

* Pantalla inicial con instrucciones del juego.
* Inicio de partida mediante la tecla `ENTER`.
* Movimiento de la serpiente con las flechas del teclado.
* Generación aleatoria de comida dentro del tablero.
* Validación para evitar que la comida aparezca sobre el cuerpo de la serpiente.
* Crecimiento de la serpiente al comer.
* Sistema de puntaje actual.
* Sistema de puntaje máximo o récord.
* Almacenamiento del puntaje máximo en archivo.
* Detección de colisiones con las paredes.
* Detección de colisiones con el propio cuerpo de la serpiente.
* Pantalla de Game Over.
* Reinicio de partida mediante la tecla `R`.
* Salida del juego mediante la tecla `ESC`.
* Dificultad progresiva mediante aumento de velocidad según el puntaje.
* Sistema de input buffer para mejorar la fluidez del control.
* Sonidos básicos para inicio, comida y fin de partida.
* Organización modular del código fuente.
* Diagramas funcionales y de arquitectura del sistema.
* Documentación del proyecto mediante archivos README y documento final.

---

## Tecnologías utilizadas

* Python 3.13
* Pygame
* Visual Studio Code
* Mermaid para diagramas
* GitHub para almacenamiento del proyecto

---

## Ejecución del proyecto

Para instalar las dependencias del proyecto, ejecutar:

```bash
py -3.13 -m pip install -r requirements.txt
```

Para iniciar el juego, ejecutar:

```bash
py -3.13 main.py
```

También se puede ejecutar el archivo:

```text
run_game.bat
```

---

## Estructura general del proyecto

```text
ProyectoSnakeUIDE/
│
├── main.py
├── requirements.txt
├── run_game.bat
├── install_dependencies.bat
├── README.md
│
├── assets/
│   └── sounds/
│
├── data/
│   └── high_score.txt
│
├── src/
│   ├── config/
│   ├── core/
│   ├── entities/
│   ├── systems/
│   ├── ui/
│   └── utils/
│
└── Materiales de entrega/
    ├── Diagramas/
    └── Documentos/
```

---

## Materiales de entrega

Los documentos principales del proyecto se encuentran disponibles en los siguientes enlaces:

* [Cronograma de Actividades - Erick Pries](https://github.com/Wilhelmroentgen/ProyectoSnakeUIDE/blob/main/Materiales%20de%20entrega/Documentos/Cronograma%20de%20Actividades%20-%20Erick%20Pries.pdf)

* [Proyecto Integrador - Erick Pries](https://github.com/Wilhelmroentgen/ProyectoSnakeUIDE/blob/main/Materiales%20de%20entrega/Documentos/Proyecto%20Integrador%20-%20Erick%20Pries.pdf)

* [Video Final - Erick Pries](https://github.com/Wilhelmroentgen/ProyectoSnakeUIDE/blob/main/Materiales%20de%20entrega/Documentos/Proyecto%20Integrador%20-%20Erick%20Pries.pdf)

---

## Fecha

**Junio de 2026**

---

## Autor

**Erick Pries**
Carrera: Ingeniería en Ciberseguridad
Materia: Lógica de Programación I
Universidad Internacional del Ecuador
