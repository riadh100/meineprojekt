/**
 * =====================================================
 * AI Empire Pro V8
 * Dashboard Routes
 * Datei: server/routes/dashboardRoutes.js
 * =====================================================
 */

const express = require("express");

const router = express.Router();

const DashboardController = require("../controllers/dashboardController");

const authMiddleware = require("../middleware/auth");

/*
|--------------------------------------------------------------------------
| Dashboard
|--------------------------------------------------------------------------
*/

router.get(

    "/",

    authMiddleware,

    DashboardController.overview

);

router.get(

    "/overview",

    authMiddleware,

    DashboardController.overview

);

router.get(

    "/system",

    authMiddleware,

    DashboardController.system

);

module.exports = router;
