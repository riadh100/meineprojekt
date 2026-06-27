/**
 * =====================================================
 * AI Empire Pro V8
 * Settings UI
 * Datei: assets/js/settings-ui.js
 * =====================================================
 */

const SettingsUI = {

    defaults: {

        language: "de",

        theme: "dark",

        animations: true,

        notifications: true,

        autoSave: true,

        compactMode: false

    },

    settings: {},

    init() {

        this.load();

        this.apply();

        console.log("✔ Settings UI gestartet.");

    },

    load() {

        const saved = localStorage.getItem("ui-settings");

        this.settings = saved
            ? JSON.parse(saved)
            : { ...this.defaults };

    },

    save() {

        localStorage.setItem(

            "ui-settings",

            JSON.stringify(this.settings)

        );

    },

    apply() {

        document.documentElement.setAttribute(

            "data-theme",

            this.settings.theme

        );

        document.body.classList.toggle(

            "compact-mode",

            this.settings.compactMode

        );

        document.body.classList.toggle(

            "animations-disabled",

            !this.settings.animations

        );

    },

    set(key, value) {

        this.settings[key] = value;

        this.save();

        this.apply();

    },

    get(key) {

        return this.settings[key];

    },

    toggle(key) {

        this.settings[key] = !this.settings[key];

        this.save();

        this.apply();

        return this.settings[key];

    },

    reset() {

        this.settings = {

            ...this.defaults

        };

        this.save();

        this.apply();

        Toast.success("Einstellungen zurückgesetzt.");

    }

};

window.SettingsUI = SettingsUI;
