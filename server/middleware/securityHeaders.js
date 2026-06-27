/**
 * =====================================================
 * AI Empire Pro V8
 * Security Headers Middleware
 * Datei: server/middleware/securityHeaders.js
 * =====================================================
 */

const helmet = require("helmet");

const securityHeaders = helmet({

    contentSecurityPolicy: {

        useDefaults: true,

        directives: {

            defaultSrc: [

                "'self'"

            ],

            scriptSrc: [

                "'self'",

                "'unsafe-inline'"

            ],

            styleSrc: [

                "'self'",

                "'unsafe-inline'"

            ],

            imgSrc: [

                "'self'",

                "data:",

                "https:"

            ],

            connectSrc: [

                "'self'",

                "ws:",

                "wss:"

            ],

            fontSrc: [

                "'self'",

                "data:"

            ],

            objectSrc: [

                "'none'"

            ]

        }

    },

    crossOriginEmbedderPolicy: false,

    referrerPolicy: {

        policy: "strict-origin-when-cross-origin"

    },

    frameguard: {

        action: "deny"

    },

    noSniff: true,

    xssFilter: true,

    hidePoweredBy: true

});

module.exports = securityHeaders;
