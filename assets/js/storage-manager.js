/**
 * =====================================================
 * AI Empire Pro V8
 * Storage Manager
 * Datei: assets/js/storage-manager.js
 * =====================================================
 */

const StorageManager = {

    prefix: "aiempire-",

    init() {

        Logger.success("Storage Manager gestartet.");

    },

    set(key, value) {

        try {

            localStorage.setItem(

                this.prefix + key,

                JSON.stringify(value)

            );

            return true;

        }

        catch (error) {

            Logger.error(

                "Storage Fehler",

                error

            );

            return false;

        }

    },

    get(key, defaultValue = null) {

        try {

            const data = localStorage.getItem(

                this.prefix + key

            );

            if (!data) {

                return defaultValue;

            }

            return JSON.parse(data);

        }

        catch (error) {

            Logger.error(

                "Storage Lesen fehlgeschlagen",

                error

            );

            return defaultValue;

        }

    },

    remove(key) {

        localStorage.removeItem(

            this.prefix + key

        );

    },

    exists(key) {

        return localStorage.getItem(

            this.prefix + key

        ) !== null;

    },

    keys() {

        return Object.keys(localStorage)

            .filter(key =>

                key.startsWith(this.prefix)

            )

            .map(key =>

                key.replace(this.prefix, "")

            );

    },

    clear() {

        this.keys().forEach(key => {

            this.remove(key);

        });

        Logger.warn(

            "Storage geleert."

        );

    },

    export() {

        const data = {};

        this.keys().forEach(key => {

            data[key] = this.get(key);

        });

        return data;

    },

    import(data = {}) {

        Object.entries(data).forEach(

            ([key, value]) => {

                this.set(key, value);

            }

        );

        Logger.success(

            "Storage importiert."

        );

    }

};

window.StorageManager = StorageManager;
