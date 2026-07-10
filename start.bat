@echo off
title Valerryx - Made by rest

echo Checking Python...

python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH.
    echo Install Python from https://python.org and try again.
    pause
    exit /b
)

echo Python found.

echo Checking pymem...

python -c "import pymem" >nul 2>&1
if errorlevel 1 (
    echo pymem not found. Installing...
    python -m pip install pymem
) else (
    echo pymem found!
)

echo Starting program...
python Valerryx.py

pause
