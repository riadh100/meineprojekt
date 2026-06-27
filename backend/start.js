/**
 * =====================================================
 * AI Empire Pro V8
 * Backend Starter
 * Datei: backend/start.js
 * =====================================================
 */

const { spawn } = require("child_process");
const fs = require("fs");

console.clear();

console.log("==========================================");
console.log("        AI Empire Pro V8 Backend");
console.log("==========================================");
console.log("");

if (!fs.existsSync("./node_modules")) {

    console.log("node_modules nicht gefunden.");
    console.log("Bitte zuerst ausführen:");
    console.log("");
    console.log("    npm install");
    console.log("");

    process.exit(1);

}

const server = spawn("node", ["server.js"], {

    stdio: "inherit",

    shell: true

});

server.on("close", (code) => {

    console.log("");
    console.log("Backend beendet.");
    console.log("Exit Code:", code);

});

server.on("error", (err) => {

    console.error("Startfehler:", err);

});
