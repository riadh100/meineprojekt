/**
 * =====================================================
 * AI Empire Pro V8
 * CORS Middleware
 * Datei: server/middleware/cors.js
 * =====================================================
 */

const cors = require("cors");

const allowedOrigins = (

    process.env.CORS_ORIGINS ||

    "http://localhost:3000,http://localhost:5173,http://localhost:8080"

)

.split(",")

.map(origin => origin.trim());

module.exports = cors({

    origin(origin, callback) {

        if (

            !origin ||

            allowedOrigins.includes(origin)

        ) {

            return callback(null, true);

        }

        return callback(

            new Error("CORS nicht erlaubt.")

        );

    },

    methods: [

        "GET",

        "POST",

        "PUT",

        "PATCH",

        "DELETE",

        "OPTIONS"

    ],

    allowedHeaders: [

        "Content-Type",

        "Authorization",

        "Accept",

        "Origin"

    ],

    exposedHeaders: [

        "Authorization"

    ],

    credentials: true,

    maxAge: 86400

});
