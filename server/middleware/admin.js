/**
 * =====================================================
 * AI Empire Pro V8
 * Admin Middleware
 * Datei: server/middleware/admin.js
 * =====================================================
 */

module.exports = (req, res, next) => {

    try {

        if (!req.user) {

            return res.status(401).json({

                success: false,

                message: "Nicht authentifiziert."

            });

        }

        if (req.user.role !== "admin") {

            return res.status(403).json({

                success: false,

                message: "Administratorrechte erforderlich."

            });

        }

        next();

    }

    catch (error) {

        console.error(error);

        return res.status(500).json({

            success: false,

            message: "Autorisierungsfehler."

        });

    }

};
