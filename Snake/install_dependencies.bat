@echo off

REM ============================================================
REM Archivo: install_dependencies.bat
REM Descripción:
REM     Este script instala las dependencias necesarias para ejecutar
REM     el Juego de la Serpiente.
REM
REM     Se utiliza Python 3.13 de forma explícita porque Pygame puede
REM     presentar problemas de instalación con versiones más recientes
REM     como Python 3.14.
REM ============================================================

echo Instalando dependencias con Python 3.13...

REM Ejecuta pip usando específicamente Python 3.13.
REM El archivo requirements.txt contiene las librerías necesarias.
py -3.13 -m pip install -r requirements.txt

REM Mantiene la ventana abierta para que el usuario pueda ver el resultado
REM de la instalación antes de que se cierre la consola.
pause