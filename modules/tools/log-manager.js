/**
 * =====================================================
 * AI Empire Pro V8
 * Tools - Log Manager
 * Datei: modules/tools/log-manager.js
 * =====================================================
 */

const LogManager = {

    logs: [],

    init() {

        this.load();

        console.log("✔ Log Manager gestartet.");

    },

    add(type, message) {

        const log = {

            id: Utils.uuid(),

            type: type,

            message: message,

            timestamp: Utils.formatDate()

        };

        this.logs.unshift(log);

        this.save();

        return log;

    },

    info(message) {

        return this.add("INFO", message);

    },

    warning(message) {

        return this.add("WARNING", message);

    },

    error(message) {

        return this.add("ERROR", message);

    },

    success(message) {

        return this.add("SUCCESS", message);

    },

    remove(id) {

        this.logs = this.logs.filter(
            log => log.id !== id
        );

        this.save();

    },

    clear() {

        this.logs = [];

        this.save();

    },

    get(id) {

        return this.logs.find(
            log => log.id === id
        );

    },

    getAll() {

        return this.logs;

    },

    save() {

        StateManager.set(
            "tools.logs",
            this.logs
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "tools.logs"
        );

        if (Array.isArray(data)) {

            this.logs = data;

        }

    }

};

window.LogManager = LogManager;
