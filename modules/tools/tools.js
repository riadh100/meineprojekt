/**
 * =====================================================
 * AI Empire Pro V8
 * Tools Module
 * Datei: modules/tools/tools.js
 * =====================================================
 */

const Tools = {

    initialized: false,

    data: {

        apiKeys: {},

        logs: [],

        debug: {

            enabled: false

        }

    },

    init() {

        if (this.initialized) return;

        this.load();

        this.initialized = true;

        console.log("✔ Tools Modul gestartet.");

    },

    load() {

        const saved = StateManager.get("tools");

        if (saved) {

            this.data = {

                ...this.data,

                ...saved

            };

        }

    },

    save() {

        StateManager.set("tools", this.data);

        StorageManager.save();

    },

    addApiKey(name, key) {

        this.data.apiKeys[name] = key;

        this.save();

    },

    getApiKey(name) {

        return this.data.apiKeys[name] || "";

    },

    removeApiKey(name) {

        delete this.data.apiKeys[name];

        this.save();

    },

    addLog(type, message) {

        this.data.logs.unshift({

            id: Utils.uuid(),

            type,

            message,

            created: Utils.formatDate()

        });

        this.save();

    },

    getLogs() {

        return this.data.logs;

    },

    clearLogs() {

        this.data.logs = [];

        this.save();

    },

    enableDebug() {

        this.data.debug.enabled = true;

        this.save();

    },

    disableDebug() {

        this.data.debug.enabled = false;

        this.save();

    }

};

window.Tools = Tools;
