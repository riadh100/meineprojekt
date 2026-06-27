/**
 * =====================================================
 * AI Empire Pro V8
 * Global Error Handler Middleware
 * Datei: server/middleware/errorHandler.js
 * =====================================================
 */

const fs = require("fs");
const path = require("path");

const LOG_DIR = path.join(process.cwd(), "logs");
const LOG_FILE = path.join(LOG_DIR, "errors.log");

if (!fs.existsSync(LOG_DIR)) {

    fs.mkdirSync(LOG_DIR, {

        recursive: true

    });

}

module.exports = (err, req, res, next) => {

    const error = {

        timestamp: new Date().toISOString(),

        method: req.method,

        url: req.originalUrl,

        ip: req.ip,

        message: err.message,

        stack: err.stack

    };

    console.error(error);

    try {

        fs.appendFileSync(

            LOG_FILE,

            JSON.stringify(error) + "\n"

        );

    }

    catch (logError) {

        console.error(

            "Fehler beim Schreiben der Logdatei.",

            logError

        );

    }

    res.status(

        err.status || 500

    ).json({

        success: false,

        message:

            process.env.NODE_ENV === "production"

                ? "Interner Serverfehler."

                : err.message,

        timestamp: error.timestamp

    });

};
