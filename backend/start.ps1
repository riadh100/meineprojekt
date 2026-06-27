# =====================================================
# AI Empire Pro V8
# Backend Start Script
# Datei: backend/start.ps1
# =====================================================

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "       AI Empire Pro V8 Backend"
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

if (!(Test-Path "node_modules")) {

    Write-Host "node_modules nicht gefunden." -ForegroundColor Yellow
    Write-Host "Installiere Abhängigkeiten..."
    npm install

}

Write-Host ""
Write-Host "Starte Backend..." -ForegroundColor Green
Write-Host ""

node server.js

Write-Host ""
Write-Host "Backend wurde beendet."
Read-Host "Zum Beenden ENTER drücken"
