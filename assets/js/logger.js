/**
 * =====================================================
 * AI Empire Pro V8
 * Logger
 * Datei: assets/js/logger.js
 * =====================================================
 */

const Logger = {

    logs: [],

    maxEntries: 1000,

    init() {

        this.load();

        console.log("✔ Logger gestartet.");

    },

    log(level = "INFO", message = "", data = null) {

        const entry = {

            id: Helpers.uuid(),

            level,

            message,

            data,

            timestamp: new Date().toISOString()

        };

        this.logs.unshift(entry);

        if (this.logs.length > this.maxEntries) {

            this.logs = this.logs.slice(0, this.maxEntries);

        }

        this.save();

        switch (level) {

            case "ERROR":

                console.error(message, data);

                break;

            case "WARN":

                console.warn(message, data);

                break;

            case "SUCCESS":

                console.info("✔", message, data);

                break;

            default:

                console.log(message, data);

        }

    },

    info(message, data = null) {

        this.log("INFO", message, data);

    },

    success(message, data = null) {

        this.log("SUCCESS", message, data);

    },

    warn(message, data = null) {

        this.log("WARN", message, data);

    },

    error(message, data = null) {

        this.log("ERROR", message, data);

    },

    getAll() {

        return this.logs;

    },

    latest(limit = 20) {

        return this.logs.slice(0, limit);

    },

    clear() {

        this.logs = [];

        this.save();

    },

    save() {

        localStorage.setItem(

            "system-logs",

            JSON.stringify(this.logs)

        );

    },

    load() {

        const data = localStorage.getItem("system-logs");

        if (!data) return;

        try {

            this.logs = JSON.parse(data);

        } catch {

            this.logs = [];

        }

    }

};

window.Logger = Logger;
