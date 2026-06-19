@echo off

REM ============================================================
REM Archivo: run_game.bat
REM Descripción:
REM     Este script ejecuta el Juego de la Serpiente utilizando
REM     específicamente Python 3.13.
REM
REM     Se utiliza este archivo para evitar que Windows ejecute el proyecto
REM     con otra versión de Python instalada en el sistema.
REM ============================================================

echo Iniciando Juego de la Serpiente con Python 3.13...

REM Ejecuta el archivo principal del proyecto con Python 3.13.
py -3.13 main.py

REM Mantiene la ventana abierta al finalizar, para que el usuario pueda
REM leer cualquier mensaje o error mostrado por el programa.
pause