/**
 * =====================================================
 * AI Empire Pro V8
 * API Router
 * Datei: server/routes/index.js
 * =====================================================
 */

const express = require("express");

const router = express.Router();

/*
|--------------------------------------------------------------------------
| Route Modules
|--------------------------------------------------------------------------
*/

const authRoutes = require("./authRoutes");
const dashboardRoutes = require("./dashboardRoutes");
const assistantRoutes = require("./assistantRoutes");
const tradingRoutes = require("./tradingRoutes");
const telegramRoutes = require("./telegramRoutes");
const videoRoutes = require("./videoRoutes");
const gameRoutes = require("./gameRoutes");
const toolsRoutes = require("./toolsRoutes");
const setupRoutes = require("./setupRoutes");

/*
|--------------------------------------------------------------------------
| Health Check
|--------------------------------------------------------------------------
*/

router.get("/", (req, res) => {

    res.json({

        success: true,

        application: "AI Empire Pro",

        version: "8.0.0",

        status: "online",

        timestamp: new Date().toISOString()

    });

});

/*
|--------------------------------------------------------------------------
| API Modules
|--------------------------------------------------------------------------
*/

router.use("/auth", authRoutes);

router.use("/dashboard", dashboardRoutes);

router.use("/assistant", assistantRoutes);

router.use("/trading", tradingRoutes);

router.use("/telegram", telegramRoutes);

router.use("/video", videoRoutes);

router.use("/game", gameRoutes);

router.use("/tools", toolsRoutes);

router.use("/setup", setupRoutes);

/*
|--------------------------------------------------------------------------
| 404 API Handler
|--------------------------------------------------------------------------
*/

router.use((req, res) => {

    res.status(404).json({

        success: false,

        message: "API-Endpunkt nicht gefunden.",

        path: req.originalUrl

    });

});

module.exports = router;
