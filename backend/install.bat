@echo off
title AI Empire Pro V8 Installer

echo ==========================================
echo        AI Empire Pro V8 Installer
echo ==========================================
echo.

echo Pruefe Node.js...
node -v >nul 2>&1

if %errorlevel% neq 0 (
    echo.
    echo Node.js wurde nicht gefunden.
    echo Bitte zuerst Node.js installieren:
    echo https://nodejs.org
    pause
    exit
)

echo Node.js gefunden.
node -v

echo.
echo Pruefe npm...
npm -v

echo.
echo Installiere Abhaengigkeiten...
call npm install

echo.
echo Erstelle Verzeichnisse...

if not exist database mkdir database
if not exist uploads mkdir uploads
if not exist logs mkdir logs

echo.
echo ==========================================
echo Installation erfolgreich abgeschlossen.
echo ==========================================
echo.
echo Backend starten:
echo.
echo     npm start
echo.
echo Entwicklungsmodus:
echo.
echo     npm run dev
echo.
pause
