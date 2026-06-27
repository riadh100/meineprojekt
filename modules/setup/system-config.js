/**
 * =====================================================
 * AI Empire Pro V8
 * Setup - System Configuration
 * Datei: modules/setup/system-config.js
 * =====================================================
 */

const SystemConfig = {

    config: {

        appName: "AI Empire Pro",

        version: "8.0.0",

        language: "de",

        theme: "dark",

        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,

        autoSave: true,

        notifications: true

    },

    init() {

        this.load();

        console.log("✔ System Configuration gestartet.");

    },

    get(key) {

        return this.config[key];

    },

    set(key, value) {

        this.config[key] = value;

        this.save();

    },

    getAll() {

        return this.config;

    },

    reset() {

        this.config = {

            appName: "AI Empire Pro",

            version: "8.0.0",

            language: "de",

            theme: "dark",

            timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,

            autoSave: true,

            notifications: true

        };

        this.save();

    },

    save() {

        StateManager.set(
            "setup.system",
            this.config
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "setup.system"
        );

        if (data) {

            this.config = {

                ...this.config,

                ...data

            };

        }

    }

};

window.SystemConfig = SystemConfig;
