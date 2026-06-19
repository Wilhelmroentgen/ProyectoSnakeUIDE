# Diagramas del Proyecto – Juego de la Serpiente

Esta carpeta contiene los diagramas utilizados para representar el diseño funcional y la arquitectura del proyecto **Juego de la Serpiente**, desarrollado como parte de la actividad académica de la materia **Lógica de Programación I**.

El objetivo de estos diagramas es documentar visualmente cómo funciona el sistema antes y durante su desarrollo, mostrando tanto la interacción del usuario con el juego como la estructura interna del software.

---

## Contenido de la carpeta

La carpeta contiene los siguientes diagramas:

```text
diagramas/
│
├── 01_diagrama_casos_uso.png
├── 02_diagrama_flujo_funcional.png
├── 03_diagrama_arquitectura_componentes.png
├── 04_diagrama_arquitectura_capas.png
├── 05_diagrama_estados_juego.png
├── 06_diagrama_input_buffer.png
└── README.md
```

Los nombres de los archivos pueden variar según el formato utilizado, por ejemplo `.png`, `.svg`, `.pdf` o `.mmd`.

---

## 1. Diagrama funcional tipo casos de uso

Este diagrama representa las funcionalidades principales del sistema desde la perspectiva del jugador.

Permite identificar las acciones que puede realizar el usuario, tales como iniciar la partida, controlar la dirección de la serpiente, ver el puntaje, reiniciar el juego y salir del programa.

También muestra las acciones internas que realiza el sistema, como crear la serpiente inicial, generar comida, mover la serpiente, detectar comida, actualizar el puntaje, detectar colisiones y finalizar la partida.

---

## 2. Diagrama de flujo funcional

Este diagrama muestra la secuencia lógica del juego desde el inicio del programa hasta su finalización.

El flujo inicia con la pantalla inicial, continúa con la creación de la serpiente, el puntaje inicial y la generación de comida. Luego entra en el ciclo principal del juego, donde se leen las entradas del teclado, se actualiza la dirección, se mueve la serpiente y se verifica si comió comida o si ocurrió una colisión.

Si no existe colisión, el juego continúa. Si ocurre una colisión, se muestra la pantalla de Game Over y el jugador puede reiniciar o finalizar el programa.

---

## 3. Diagrama de arquitectura por componentes

Este diagrama representa la división interna del sistema en componentes especializados.

El proyecto se organiza en módulos como:

* Interfaz gráfica.
* Controlador principal del juego.
* Entrada de teclado.
* Lógica de la serpiente.
* Módulo de comida.
* Sistema de colisiones.
* Sistema de puntaje.
* Estado del juego.
* Renderizado.

Esta organización permite separar responsabilidades, facilitar el mantenimiento del código y permitir futuras mejoras sin afectar todo el sistema.

---

## 4. Diagrama de arquitectura por capas

Este diagrama muestra el sistema organizado por niveles o capas.

Las capas principales son:

* **Capa de presentación:** muestra el tablero, la serpiente, la comida, el puntaje y los mensajes en pantalla.
* **Capa de control:** coordina el ciclo principal del juego y comunica los módulos.
* **Capa de lógica del juego:** contiene las reglas de movimiento, comida, colisiones y puntaje.
* **Capa de estado en memoria:** almacena los datos actuales del juego, como posición de la serpiente, dirección, buffer de entrada, comida, puntaje y estado de la partida.

Este diagrama ayuda a comprender cómo se estructura el programa desde una visión más general.

---

## 5. Diagrama de estados del juego

Este diagrama representa los estados principales del programa.

Actualmente, el juego maneja los siguientes estados:

* **RUNNING:** la partida está en ejecución.
* **GAME_OVER:** la partida ha terminado por una colisión.
* **EXIT:** el programa debe cerrarse.

El diagrama muestra cómo el sistema cambia de un estado a otro según las acciones del jugador o las condiciones del juego.

Por ejemplo, si la serpiente choca con una pared o con su propio cuerpo, el estado cambia de `RUNNING` a `GAME_OVER`. Desde `GAME_OVER`, el jugador puede reiniciar con la tecla `R` o salir con `ESC`.

---

## 6. Diagrama del input buffer

Este diagrama explica el funcionamiento del sistema de buffer de entrada implementado para mejorar la fluidez del control de la serpiente.

El input buffer permite guardar direcciones ingresadas rápidamente por el jugador y aplicarlas en orden durante los siguientes movimientos.

Esta mejora evita errores como colisiones falsas cuando el jugador presiona varias teclas en muy poco tiempo. También impide giros inválidos, como cambiar directamente de derecha a izquierda o de arriba hacia abajo.

---

## Herramienta utilizada

Los diagramas fueron construidos utilizando **Mermaid**, una herramienta que permite crear diagramas mediante texto estructurado.

Mermaid facilita la documentación técnica porque permite versionar, modificar y reutilizar diagramas de forma sencilla.

---

## Relación con el desarrollo del software

Los diagramas de esta carpeta se relacionan directamente con la estructura del código fuente del proyecto.

Por ejemplo:

```text
Diagrama de arquitectura          Código del proyecto
---------------------------------------------------------
Controlador principal             src/core/game.py
Entrada de teclado                src/core/input_handler.py
Estado del juego                  src/core/game_state.py
Lógica de la serpiente            src/entities/snake.py
Comida                            src/entities/food.py
Colisiones                        src/systems/collision_system.py
Puntaje                           src/systems/score_system.py
Renderizado                       src/ui/renderer.py
Pantallas                         src/ui/screens.py
```

Esto demuestra que el desarrollo del juego sigue la arquitectura planteada durante la fase de diseño.

---

## Estado del proyecto

Estos diagramas corresponden a la primera versión funcional del proyecto.

En esta etapa ya se representa:

* El funcionamiento general del juego.
* Las principales funcionalidades del usuario.
* La arquitectura modular.
* Los estados actuales del sistema.
* La lógica del input buffer.

Para la entrega final, los diagramas podrían actualizarse si se agregan nuevas funcionalidades, como pantalla inicial, pausa, dificultad progresiva, puntaje máximo o sonidos.

---

## Autor

**Erick Pries**
Carrera: Ingeniería en Ciberseguridad
Materia: Lógica de Programación I
Universidad Internacional del Ecuador
