/**
 * =====================================================
 * AI Empire Pro V8
 * Backup Manager
 * Datei: assets/js/backup.js
 * =====================================================
 */

const Backup = {

    create() {

        try {

            const backup = {

                version: "8.0.0",

                created: new Date().toISOString(),

                state: localStorage.getItem("app-state"),

                settings: localStorage.getItem("ui-settings"),

                theme: localStorage.getItem("theme"),

                notifications: localStorage.getItem("notifications"),

                storage: {}

            };

            for (let i = 0; i < localStorage.length; i++) {

                const key = localStorage.key(i);

                backup.storage[key] = localStorage.getItem(key);

            }

            Helpers.download(

                `AI-Empire-Backup-${Date.now()}.json`,

                JSON.stringify(backup, null, 2)

            );

            Toast.success("Backup erfolgreich erstellt.");

        }

        catch(error){

            console.error(error);

            Toast.error("Backup konnte nicht erstellt werden.");

        }

    },

    restore(file) {

        const reader = new FileReader();

        reader.onload = event => {

            try {

                const backup = JSON.parse(event.target.result);

                Object.entries(backup.storage).forEach(

                    ([key, value]) => {

                        localStorage.setItem(key, value);

                    }

                );

                Toast.success(

                    "Backup erfolgreich wiederhergestellt."

                );

                setTimeout(() => {

                    location.reload();

                }, 1000);

            }

            catch(error){

                console.error(error);

                Toast.error("Ungültige Backup-Datei.");

            }

        };

        reader.readAsText(file);

    },

    clear() {

        Dialog.confirm(

            "Lokale Daten löschen",

            "Alle gespeicherten Daten werden entfernt.",

            () => {

                localStorage.clear();

                Toast.success("Lokale Daten gelöscht.");

                setTimeout(() => {

                    location.reload();

                }, 1000);

            }

        );

    }

};

window.Backup = Backup;
