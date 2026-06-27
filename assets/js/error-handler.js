/**
 * =====================================================
 * AI Empire Pro V8
 * Global Error Handler
 * Datei: assets/js/error-handler.js
 * =====================================================
 */

const ErrorHandler = {

    errors: [],

    init() {

        window.addEventListener("error", (event) => {

            this.capture({

                type: "JavaScript",

                message: event.message,

                file: event.filename,

                line: event.lineno,

                column: event.colno,

                stack: event.error
                    ? event.error.stack
                    : null

            });

        });

        window.addEventListener(

            "unhandledrejection",

            (event) => {

                this.capture({

                    type: "Promise",

                    message: event.reason?.message || String(event.reason),

                    stack: event.reason?.stack || null

                });

            }

        );

        Logger.success("Error Handler gestartet.");

    },

    capture(error) {

        const entry = {

            id: Helpers.uuid(),

            timestamp: new Date().toISOString(),

            ...error

        };

        this.errors.unshift(entry);

        Logger.error(

            entry.message,

            entry

        );

        if (typeof DebugCenter !== "undefined") {

            DebugCenter.add(entry);

        }

        if (typeof NotificationCenter !== "undefined") {

            NotificationCenter.error(

                "Systemfehler",

                entry.message

            );

        }

    },

    getAll() {

        return this.errors;

    },

    latest(limit = 20) {

        return this.errors.slice(0, limit);

    },

    clear() {

        this.errors = [];

        Logger.info("Fehlerliste geleert.");

    }

};

window.ErrorHandler = ErrorHandler;
