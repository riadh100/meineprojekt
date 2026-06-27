#!/bin/bash

echo "=========================================="
echo " AI Empire Pro V8 Installation"
echo "=========================================="

echo ""
echo "Prüfe Node.js..."

if ! command -v node &> /dev/null
then
    echo "Node.js wurde nicht gefunden."
    exit 1
fi

echo "Node Version:"
node -v

echo ""
echo "Prüfe npm..."

if ! command -v npm &> /dev/null
then
    echo "npm wurde nicht gefunden."
    exit 1
fi

echo "npm Version:"
npm -v

echo ""
echo "Installiere Abhängigkeiten..."

npm install

echo ""
echo "Erstelle Datenbankordner..."

mkdir -p database

echo ""
echo "Erstelle Upload Ordner..."

mkdir -p uploads

echo ""
echo "Installation abgeschlossen."

echo ""
echo "Backend starten mit:"

echo "npm start"

echo ""
echo "Entwicklungsmodus:"

echo "npm run dev"

echo ""
echo "=========================================="
echo " AI Empire Pro V8 ist bereit."
echo "=========================================="
