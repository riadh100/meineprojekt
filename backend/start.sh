#!/bin/bash

echo "=========================================="
echo "       AI Empire Pro V8 Backend"
echo "=========================================="

if [ ! -d "node_modules" ]; then
    echo ""
    echo "node_modules nicht gefunden."
    echo "Installiere Abhängigkeiten..."
    npm install
fi

echo ""
echo "Starte AI Empire Pro Backend..."
echo ""

node server.js

echo ""
echo "Backend wurde beendet."
