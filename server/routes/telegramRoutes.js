/**
 * =====================================================
 * AI Empire Pro V8
 * Telegram Routes
 * Datei: server/routes/telegramRoutes.js
 * =====================================================
 */

const express = require("express");

const router = express.Router();

const TelegramController = require("../controllers/telegramController");

const authMiddleware = require("../middleware/auth");

/*
|--------------------------------------------------------------------------
| Telegram Status
|--------------------------------------------------------------------------
*/

router.get(

    "/status",

    authMiddleware,

    TelegramController.status

);

/*
|--------------------------------------------------------------------------
| Send Message
|--------------------------------------------------------------------------
*/

router.post(

    "/send",

    authMiddleware,

    TelegramController.send

);

/*
|--------------------------------------------------------------------------
| Broadcast
|--------------------------------------------------------------------------
*/

router.post(

    "/broadcast",

    authMiddleware,

    TelegramController.broadcast

);

/*
|--------------------------------------------------------------------------
| Message History
|--------------------------------------------------------------------------
*/

router.get(

    "/history",

    authMiddleware,

    TelegramController.history

);

module.exports = router;
