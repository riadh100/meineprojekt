/**
 * =====================================================
 * AI Empire Pro V8
 * Rate Limiter Middleware
 * Datei: server/middleware/rateLimiter.js
 * =====================================================
 */

const rateLimit = require("express-rate-limit");

const limiter = rateLimit({

    windowMs: 15 * 60 * 1000,

    max: 300,

    standardHeaders: true,

    legacyHeaders: false,

    message: {

        success: false,

        error: {

            code: 429,

            type: "RATE_LIMIT",

            message: "Zu viele Anfragen. Bitte versuche es später erneut."

        }

    },

    handler: (req, res, next, options) => {

        return res.status(options.statusCode).json({

            success: false,

            error: {

                code: 429,

                type: "RATE_LIMIT",

                message: options.message.error.message

            },

            retryAfter: Math.ceil(

                options.windowMs / 1000

            ),

            timestamp: new Date().toISOString()

        });

    }

});

module.exports = limiter;
