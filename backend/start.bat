@echo off
title AI Empire Pro V8

echo ==========================================
echo         AI Empire Pro V8 Backend
echo ==========================================
echo.

if not exist node_modules (
    echo node_modules nicht gefunden.
    echo Fuehre Installation aus...
    call npm install
)

echo.

echo Starte Backend...

node server.js

echo.

echo Server wurde beendet.
pause
