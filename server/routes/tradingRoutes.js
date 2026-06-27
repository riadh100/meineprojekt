/**
 * =====================================================
 * AI Empire Pro V8
 * Trading Routes
 * Datei: server/routes/tradingRoutes.js
 * =====================================================
 */

const express = require("express");

const router = express.Router();

const TradingController = require("../controllers/tradingController");

const authMiddleware = require("../middleware/auth");

/*
|--------------------------------------------------------------------------
| Trading Dashboard
|--------------------------------------------------------------------------
*/

router.get(

    "/",

    authMiddleware,

    TradingController.dashboard

);

router.get(

    "/dashboard",

    authMiddleware,

    TradingController.dashboard

);

/*
|--------------------------------------------------------------------------
| Trade History
|--------------------------------------------------------------------------
*/

router.get(

    "/history",

    authMiddleware,

    TradingController.history

);

/*
|--------------------------------------------------------------------------
| Trade Management
|--------------------------------------------------------------------------
*/

router.post(

    "/trade",

    authMiddleware,

    TradingController.createTrade

);

router.put(

    "/trade/:id",

    authMiddleware,

    TradingController.updateTrade

);

router.delete(

    "/trade/:id",

    authMiddleware,

    TradingController.deleteTrade

);

module.exports = router;
