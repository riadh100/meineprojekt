/**
 * =====================================================
 * AI Empire Pro V8
 * Response Utilities
 * Datei: server/utils/response.js
 * =====================================================
 */

class Response {

    static success(

        res,

        data = {},

        message = "OK",

        status = 200

    ) {

        return res.status(status).json({

            success: true,

            message,

            timestamp: new Date().toISOString(),

            data

        });

    }

    static created(

        res,

        data = {},

        message = "Erfolgreich erstellt."

    ) {

        return this.success(

            res,

            data,

            message,

            201

        );

    }

    static error(

        res,

        message = "Fehler.",

        status = 500,

        errors = null

    ) {

        return res.status(status).json({

            success: false,

            message,

            timestamp: new Date().toISOString(),

            errors

        });

    }

    static unauthorized(

        res,

        message = "Nicht autorisiert."

    ) {

        return this.error(

            res,

            message,

            401

        );

    }

    static forbidden(

        res,

        message = "Zugriff verweigert."

    ) {

        return this.error(

            res,

            message,

            403

        );

    }

    static notFound(

        res,

        message = "Nicht gefunden."

    ) {

        return this.error(

            res,

            message,

            404

        );

    }

    static validation(

        res,

        errors = {}

    ) {

        return this.error(

            res,

            "Validierungsfehler.",

            422,

            errors

        );

    }

}

module.exports = Response;
