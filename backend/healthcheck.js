/**
 * =====================================================
 * AI Empire Pro V8
 * Backend Health Check
 * Datei: backend/healthcheck.js
 * =====================================================
 */

const os = require("os");
const fs = require("fs");
const path = require("path");

function formatBytes(bytes) {

    const units = ["B", "KB", "MB", "GB"];

    let i = 0;

    while (bytes >= 1024 && i < units.length - 1) {

        bytes /= 1024;

        i++;

    }

    return bytes.toFixed(2) + " " + units[i];

}

console.log("");
console.log("==========================================");
console.log(" AI Empire Pro V8 Health Check");
console.log("==========================================");
console.log("");

console.log("Node Version:");
console.log(process.version);

console.log("");

console.log("Betriebssystem:");
console.log(os.type(), os.release());

console.log("");

console.log("CPU:");
console.log(os.cpus()[0].model);

console.log("");

console.log("Speicher:");

console.log(
    "Gesamt:",
    formatBytes(os.totalmem())
);

console.log(
    "Frei:",
    formatBytes(os.freemem())
);

console.log("");

console.log("Projektstruktur:");

[
    "controllers",
    "models",
    "routes",
    "database"
].forEach(folder => {

    const exists = fs.existsSync(
        path.join(__dirname, folder)
    );

    console.log(
        folder + ":",
        exists ? "OK" : "FEHLT"
    );

});

console.log("");

console.log("Environment:");

console.log(
    ".env:",
    fs.existsSync(path.join(__dirname, ".env"))
        ? "OK"
        : "FEHLT"
);

console.log("");

console.log("Status:");

console.log("Backend bereit.");

console.log("");

console.log("==========================================");
console.log("Health Check abgeschlossen");
console.log("==========================================");
