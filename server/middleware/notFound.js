/**
 * =====================================================
 * AI Empire Pro V8
 * 404 Middleware
 * Datei: server/middleware/notFound.js
 * =====================================================
 */

module.exports = (req, res) => {

    res.status(404).json({

        success: false,

        error: {

            code: 404,

            type: "NOT_FOUND",

            message: "Der angeforderte API-Endpunkt wurde nicht gefunden."

        },

        request: {

            method: req.method,

            url: req.originalUrl

        },

        timestamp: new Date().toISOString()

    });

};
