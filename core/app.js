/**
 * =====================================================
 * AI Empire Pro V8
 * Core - App
 * Datei: core/app.js
 * =====================================================
 */

const App = {

    version: "8.0.0",

    name: "AI Empire Pro",

    initialized: false,

    init() {

        console.log("=================================");
        console.log(this.name + " V" + this.version);
        console.log("System wird gestartet...");
        console.log("=================================");

        StorageManager.load();

        this.initialized = true;

        console.log("✔ App erfolgreich gestartet.");

    },

    restart() {

        console.log("System wird neu gestartet...");

        location.reload();

    },

    shutdown() {

        StorageManager.save();

        console.log("System beendet.");

    },

    getVersion() {

        return this.version;

    },

    isReady() {

        return this.initialized;

    }

};

window.App = App;

document.addEventListener("DOMContentLoaded", () => {

    App.init();

});
