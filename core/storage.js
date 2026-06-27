/**
 * =====================================================
 * AI Empire Pro V8
 * Core - Storage Engine
 * Datei: core/storage.js
 * =====================================================
 */

const StorageManager = {

    /**
     * Schlüssel für LocalStorage
     */
    key: "AIEmpireProV8",

    /**
     * Gesamten State speichern
     */
    save() {

        try {

            localStorage.setItem(
                this.key,
                JSON.stringify(StateManager.getState())
            );

            console.log("✔ State gespeichert.");

            return true;

        } catch (error) {

            console.error("Speichern fehlgeschlagen:", error);

            return false;

        }

    },

    /**
     * State laden
     */
    load() {

        try {

            const data = localStorage.getItem(this.key);

            if (!data) {

                console.log("Keine gespeicherten Daten gefunden.");

                return false;

            }

            const savedState = JSON.parse(data);

            Object.assign(AppState, savedState);

            console.log("✔ State geladen.");

            return true;

        } catch (error) {

            console.error("Laden fehlgeschlagen:", error);

            return false;

        }

    },

    /**
     * Speicher löschen
     */
    clear() {

        localStorage.removeItem(this.key);

        console.log("✔ LocalStorage gelöscht.");

    },

    /**
     * State exportieren
     */
    export() {

        return JSON.stringify(
            StateManager.getState(),
            null,
            2
        );

    },

    /**
     * State importieren
     */
    import(json) {

        try {

            const data = JSON.parse(json);

            Object.assign(AppState, data);

            this.save();

            console.log("✔ Daten importiert.");

            return true;

        } catch (error) {

            console.error("Import fehlgeschlagen:", error);

            return false;

        }

    }

};

window.StorageManager = StorageManager;
