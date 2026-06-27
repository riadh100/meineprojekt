/**
 * =====================================================
 * AI Empire Pro V8
 * Video Routes
 * Datei: server/routes/videoRoutes.js
 * =====================================================
 */

const express = require("express");

const router = express.Router();

const VideoController = require("../controllers/videoController");

const authMiddleware = require("../middleware/auth");

/*
|--------------------------------------------------------------------------
| Video Dashboard
|--------------------------------------------------------------------------
*/

router.get(

    "/",

    authMiddleware,

    VideoController.dashboard

);

router.get(

    "/dashboard",

    authMiddleware,

    VideoController.dashboard

);

/*
|--------------------------------------------------------------------------
| Projects
|--------------------------------------------------------------------------
*/

router.post(

    "/project",

    authMiddleware,

    VideoController.createProject

);

router.put(

    "/project/:id",

    authMiddleware,

    VideoController.updateProject

);

router.delete(

    "/project/:id",

    authMiddleware,

    VideoController.deleteProject

);

/*
|--------------------------------------------------------------------------
| Render Queue
|--------------------------------------------------------------------------
*/

router.post(

    "/render",

    authMiddleware,

    VideoController.createRender

);

router.put(

    "/render/:id",

    authMiddleware,

    VideoController.updateRender

);

router.get(

    "/history",

    authMiddleware,

    VideoController.history

);

module.exports = router;
