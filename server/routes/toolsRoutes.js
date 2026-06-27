/**
 * =====================================================
 * AI Empire Pro V8
 * Tools Routes
 * Datei: server/routes/toolsRoutes.js
 * =====================================================
 */

const express = require("express");

const router = express.Router();

const ToolsController = require("../controllers/toolsController");

const authMiddleware = require("../middleware/auth");

/*
|--------------------------------------------------------------------------
| Tools Dashboard
|--------------------------------------------------------------------------
*/

router.get(

    "/",

    authMiddleware,

    ToolsController.dashboard

);

router.get(

    "/dashboard",

    authMiddleware,

    ToolsController.dashboard

);

/*
|--------------------------------------------------------------------------
| System Health
|--------------------------------------------------------------------------
*/

router.get(

    "/health",

    authMiddleware,

    ToolsController.health

);

router.get(

    "/environment",

    authMiddleware,

    ToolsController.environment

);

/*
|--------------------------------------------------------------------------
| Logs
|--------------------------------------------------------------------------
*/

router.get(

    "/logs",

    authMiddleware,

    ToolsController.logs

);

router.delete(

    "/logs",

    authMiddleware,

    ToolsController.clearLogs

);

module.exports = router;
