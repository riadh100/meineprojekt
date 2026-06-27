/**
 * =====================================================
 * AI Empire Pro V8
 * Core - Settings Manager
 * Datei: core/settings.js
 * =====================================================
 */

const SettingsManager = {

    defaults: {
        theme: "dark",
        language: "de",
        notifications: true,
        autoSave: true
    },

    init() {

        const settings = StateManager.get("settings");

        if (!settings) {
            StateManager.set("settings", { ...this.defaults });
            StorageManager.save();
        }

    },

    get(key) {

        return StateManager.get(`settings.${key}`);

    },

    set(key, value) {

        StateManager.set(`settings.${key}`, value);

        StorageManager.save();

    },

    has(key) {

        return this.get(key) !== undefined;

    },

    remove(key) {

        const settings = StateManager.get("settings");

        delete settings[key];

        StorageManager.save();

    },

    reset() {

        StateManager.set("settings", { ...this.defaults });

        StorageManager.save();

    },

    getAll() {

        return StateManager.get("settings");

    }

};

window.SettingsManager = SettingsManager;
