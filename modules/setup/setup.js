/**
 * =====================================================
 * AI Empire Pro V8
 * Setup Module
 * Datei: modules/setup/setup.js
 * =====================================================
 */

const Setup = {

    initialized: false,

    data: {

        profile: {

            username: "",

            email: "",

            avatar: ""

        },

        security: {

            twoFactor: false,

            autoLock: false

        },

        backup: {

            lastBackup: null

        },

        system: {

            language: "de",

            theme: "dark"

        }

    },

    init() {

        if (this.initialized) return;

        this.load();

        this.initialized = true;

        console.log("✔ Setup Modul gestartet.");

    },

    load() {

        const saved = StateManager.get("setup");

        if (saved) {

            this.data = {

                ...this.data,

                ...saved

            };

        }

    },

    save() {

        StateManager.set("setup", this.data);

        StorageManager.save();

    },

    reset() {

        this.data = {

            profile: {

                username: "",

                email: "",

                avatar: ""

            },

            security: {

                twoFactor: false,

                autoLock: false

            },

            backup: {

                lastBackup: null

            },

            system: {

                language: "de",

                theme: "dark"

            }

        };

        this.save();

    }

};

window.Setup = Setup;
