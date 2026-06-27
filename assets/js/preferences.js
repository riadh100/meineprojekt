/**
 * =====================================================
 * AI Empire Pro V8
 * User Preferences
 * Datei: assets/js/preferences.js
 * =====================================================
 */

const Preferences = {

    defaults: {

        language: "de",

        currency: "EUR",

        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,

        dateFormat: "DD.MM.YYYY",

        compactMode: false,

        animations: true,

        notifications: true,

        autoRefresh: true,

        refreshInterval: 10000

    },

    data: {},

    init() {

        this.load();

        Logger.success("Preferences gestartet.");

    },

    load() {

        this.data = StorageManager.get(

            "preferences",

            { ...this.defaults }

        );

    },

    save() {

        StorageManager.set(

            "preferences",

            this.data

        );

    },

    get(key) {

        return this.data[key];

    },

    set(key, value) {

        this.data[key] = value;

        this.save();

    },

    toggle(key) {

        if (typeof this.data[key] !== "boolean") {

            return;

        }

        this.data[key] = !this.data[key];

        this.save();

    },

    reset() {

        this.data = {

            ...this.defaults

        };

        this.save();

        Logger.info(

            "Benutzereinstellungen zurückgesetzt."

        );

    },

    export() {

        return structuredClone(this.data);

    },

    import(data = {}) {

        this.data = {

            ...this.defaults,

            ...data

        };

        this.save();

    }

};

window.Preferences = Preferences;
