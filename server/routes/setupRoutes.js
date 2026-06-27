/**
 * =====================================================
 * AI Empire Pro V8
 * Setup Routes
 * Datei: server/routes/setupRoutes.js
 * =====================================================
 */

const express = require("express");

const router = express.Router();

const SetupController = require("../controllers/setupController");

const authMiddleware = require("../middleware/auth");

/*
|--------------------------------------------------------------------------
| Setup Dashboard
|--------------------------------------------------------------------------
*/

router.get(

    "/",

    authMiddleware,

    SetupController.dashboard

);

router.get(

    "/dashboard",

    authMiddleware,

    SetupController.dashboard

);

/*
|--------------------------------------------------------------------------
| Settings
|--------------------------------------------------------------------------
*/

router.get(

    "/settings",

    authMiddleware,

    SetupController.settings

);

router.put(

    "/settings",

    authMiddleware,

    SetupController.saveSettings

);

/*
|--------------------------------------------------------------------------
| Backup
|--------------------------------------------------------------------------
*/

router.post(

    "/backup",

    authMiddleware,

    SetupController.backup

);

router.post(

    "/restore",

    authMiddleware,

    SetupController.restore

);

module.exports = router;
