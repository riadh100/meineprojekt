/**
 * =====================================================
 * AI Empire Pro V8
 * Backend Database Test
 * Datei: backend/test-database.js
 * =====================================================
 */

const db = require("./database");

console.clear();

console.log("==========================================");
console.log(" AI Empire Pro V8 Database Test");
console.log("==========================================");
console.log("");

console.log("Benutzer:");

console.log(db.users());

console.log("");

console.log("Trades:");

console.log(db.trades());

console.log("");

console.log("Projekte:");

console.log(db.projects());

console.log("");

console.log("Bots:");

console.log(db.bots());

console.log("");

console.log("Konversationen:");

console.log(db.conversations());

console.log("");

console.log("Achievements:");

console.log(db.achievements());

console.log("");

console.log("Missionen:");

console.log(db.missions());

console.log("");

console.log("Belohnungen:");

console.log(db.rewards());

console.log("");

console.log("==========================================");
console.log("Database Test abgeschlossen");
console.log("==========================================");
