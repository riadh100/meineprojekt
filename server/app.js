/**
 * =====================================================
 * AI Empire Pro V8
 * Express Application
 * Datei: server/app.js
 * =====================================================
 */

require("dotenv").config();

const express = require("express");
const compression = require("compression");
const cookieParser = require("cookie-parser");
const morgan = require("morgan");

const cors = require("./middleware/cors");
const securityHeaders = require("./middleware/securityHeaders");
const rateLimiter = require("./middleware/rateLimiter");
const requestLogger = require("./middleware/requestLogger");
const notFound = require("./middleware/notFound");
const errorHandler = require("./middleware/errorHandler");

const routes = require("./routes");

const app = express();

/*
|--------------------------------------------------------------------------
| Express Configuration
|--------------------------------------------------------------------------
*/

app.disable("x-powered-by");

app.use(securityHeaders);

app.use(cors);

app.use(rateLimiter);

app.use(compression());

app.use(cookieParser());

app.use(express.json({

    limit: "50mb"

}));

app.use(express.urlencoded({

    extended: true,

    limit: "50mb"

}));

app.use(

    express.static("public")

);

app.use(

    "/uploads",

    express.static("uploads")

);

app.use(

    morgan("dev")

);

app.use(

    requestLogger

);

/*
|--------------------------------------------------------------------------
| API
|--------------------------------------------------------------------------
*/

app.use(

    "/api",

    routes

);

/*
|--------------------------------------------------------------------------
| Root
|--------------------------------------------------------------------------
*/

app.get("/", (req, res) => {

    res.json({

        success: true,

        application: "AI Empire Pro",

        version: "8.0.0",

        status: "running",

        timestamp: new Date().toISOString()

    });

});

/*
|--------------------------------------------------------------------------
| Error Handling
|--------------------------------------------------------------------------
*/

app.use(notFound);

app.use(errorHandler);

module.exports = app;
