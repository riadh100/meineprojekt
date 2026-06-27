/**
 * =====================================================
 * AI Empire Pro V8
 * Assistant Routes
 * Datei: server/routes/assistantRoutes.js
 * =====================================================
 */

const express = require("express");

const router = express.Router();

const AssistantController = require("../controllers/assistantController");

const authMiddleware = require("../middleware/auth");

/*
|--------------------------------------------------------------------------
| AI Chat
|--------------------------------------------------------------------------
*/

router.post(

    "/chat",

    authMiddleware,

    AssistantController.chat

);

/*
|--------------------------------------------------------------------------
| Conversation History
|--------------------------------------------------------------------------
*/

router.get(

    "/history",

    authMiddleware,

    AssistantController.history

);

router.get(

    "/conversation/:id",

    authMiddleware,

    AssistantController.conversation

);

module.exports = router;
