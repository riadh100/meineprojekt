/**
 * =====================================================
 * AI Empire Pro V8
 * Game Routes
 * Datei: server/routes/gameRoutes.js
 * =====================================================
 */

const express = require("express");

const router = express.Router();

const GameController = require("../controllers/gameController");

const authMiddleware = require("../middleware/auth");

/*
|--------------------------------------------------------------------------
| Game Dashboard
|--------------------------------------------------------------------------
*/

router.get(

    "/",

    authMiddleware,

    GameController.dashboard

);

router.get(

    "/dashboard",

    authMiddleware,

    GameController.dashboard

);

/*
|--------------------------------------------------------------------------
| XP System
|--------------------------------------------------------------------------
*/

router.post(

    "/xp",

    authMiddleware,

    GameController.addXP

);

/*
|--------------------------------------------------------------------------
| Missions
|--------------------------------------------------------------------------
*/

router.post(

    "/mission/:id/complete",

    authMiddleware,

    GameController.completeMission

);

/*
|--------------------------------------------------------------------------
| Achievements
|--------------------------------------------------------------------------
*/

router.post(

    "/achievement/:id/unlock",

    authMiddleware,

    GameController.unlockAchievement

);

/*
|--------------------------------------------------------------------------
| Rewards
|--------------------------------------------------------------------------
*/

router.post(

    "/reward/:id/claim",

    authMiddleware,

    GameController.claimReward

);

module.exports = router;
