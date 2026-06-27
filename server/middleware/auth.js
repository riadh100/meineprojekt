/**
 * =====================================================
 * AI Empire Pro V8
 * JWT Authentication Middleware
 * Datei: server/middleware/auth.js
 * =====================================================
 */

const jwt = require("jsonwebtoken");

const User = require("../models/User");

const JWT_SECRET =

    process.env.JWT_SECRET ||

    "AI_EMPIRE_SECRET";

module.exports = async (req, res, next) => {

    try {

        const header = req.headers.authorization;

        if (

            !header ||

            !header.startsWith("Bearer ")

        ) {

            return res.status(401).json({

                success: false,

                message: "Keine Authentifizierung vorhanden."

            });

        }

        const token = header.replace(

            "Bearer ",

            ""

        );

        const decoded = jwt.verify(

            token,

            JWT_SECRET

        );

        const user = await User.findById(

            decoded.id

        ).select("-password");

        if (!user) {

            return res.status(401).json({

                success: false,

                message: "Benutzer nicht gefunden."

            });

        }

        req.user = user;

        next();

    }

    catch (error) {

        console.error(error);

        return res.status(401).json({

            success: false,

            message: "Ungültiger oder abgelaufener Token."

        });

    }

};
