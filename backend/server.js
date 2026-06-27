/**
 * =====================================================
 * AI Empire Pro V8
 * Backend - Node.js Server
 * Datei: backend/server.js
 * =====================================================
 */

const express = require("express");
const cors = require("cors");

const app = express();

const PORT = process.env.PORT || 3000;

app.use(cors());

app.use(express.json());

app.get("/", (req, res) => {

    res.json({

        name: "AI Empire Pro API",

        version: "8.0.0",

        status: "online"

    });

});

app.get("/api/status", (req, res) => {

    res.json({

        success: true,

        server: "running",

        timestamp: new Date().toISOString()

    });

});

app.get("/api/health", (req, res) => {

    res.json({

        status: "healthy",

        uptime: process.uptime(),

        memory: process.memoryUsage(),

        node: process.version

    });

});

app.use((req, res) => {

    res.status(404).json({

        success: false,

        message: "Route not found"

    });

});

app.listen(PORT, () => {

    console.log("===================================");

    console.log("AI Empire Pro Backend");

    console.log("Server läuft auf Port:", PORT);

    console.log("===================================");

});
