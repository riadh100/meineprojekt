/**
 * =====================================================
 * AI Empire Pro V8
 * Request Validation Middleware
 * Datei: server/middleware/validate.js
 * =====================================================
 */

const { validationResult } = require("express-validator");

module.exports = (req, res, next) => {

    const errors = validationResult(req);

    if (!errors.isEmpty()) {

        return res.status(400).json({

            success: false,

            error: {

                code: 400,

                type: "VALIDATION_ERROR",

                message: "Die Anfrage enthält ungültige Daten."

            },

            fields: errors.array().map(error => ({

                field: error.param,

                message: error.msg,

                value: error.value

            })),

            timestamp: new Date().toISOString()

        });

    }

    next();

};
