/**
 * =====================================================
 * AI Empire Pro V8
 * Tools - Debug Center
 * Datei: modules/tools/debug-center.js
 * =====================================================
 */

const DebugCenter = {

    enabled: false,

    errors: [],

    warnings: [],

    init() {

        this.load();

        console.log("✔ Debug Center gestartet.");

    },

    enable() {

        this.enabled = true;

        this.save();

    },

    disable() {

        this.enabled = false;

        this.save();

    },

    log(message) {

        if (!this.enabled) return;

        console.log("[DEBUG]", message);

    },

    error(message) {

        this.errors.unshift({

            id: Utils.uuid(),

            message,

            timestamp: Utils.formatDate()

        });

        this.save();

    },

    warning(message) {

        this.warnings.unshift({

            id: Utils.uuid(),

            message,

            timestamp: Utils.formatDate()

        });

        this.save();

    },

    getErrors() {

        return this.errors;

    },

    getWarnings() {

        return this.warnings;

    },

    clearErrors() {

        this.errors = [];

        this.save();

    },

    clearWarnings() {

        this.warnings = [];

        this.save();

    },

    clearAll() {

        this.errors = [];

        this.warnings = [];

        this.save();

    },

    save() {

        StateManager.set("tools.debug", {

            enabled: this.enabled,

            errors: this.errors,

            warnings: this.warnings

        });

        StorageManager.save();

    },

    load() {

        const data = StateManager.get("tools.debug");

        if (!data) return;

        this.enabled = data.enabled || false;

        this.errors = data.errors || [];

        this.warnings = data.warnings || [];

    }

};

window.DebugCenter = DebugCenter;
