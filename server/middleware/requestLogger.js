/**
 * =====================================================
 * AI Empire Pro V8
 * Request Logger Middleware
 * Datei: server/middleware/requestLogger.js
 * =====================================================
 */

const fs = require("fs");
const path = require("path");

const LOG_DIR = path.join(process.cwd(), "logs");
const LOG_FILE = path.join(LOG_DIR, "requests.log");

if (!fs.existsSync(LOG_DIR)) {

    fs.mkdirSync(LOG_DIR, {

        recursive: true

    });

}

module.exports = (req, res, next) => {

    const start = Date.now();

    res.on("finish", () => {

        const entry = {

            timestamp: new Date().toISOString(),

            method: req.method,

            url: req.originalUrl,

            status: res.statusCode,

            ip: req.ip,

            userAgent: req.get("user-agent"),

            duration: Date.now() - start

        };

        try {

            fs.appendFileSync(

                LOG_FILE,

                JSON.stringify(entry) + "\n"

            );

        }

        catch (error) {

            console.error(

                "Request Logger Fehler:",

                error

            );

        }

    });

    next();

};
