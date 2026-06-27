/**
 * =====================================================
 * AI Empire Pro V8
 * Update Manager
 * Datei: assets/js/update-manager.js
 * =====================================================
 */

const UpdateManager = {

    currentVersion: "8.0.0",

    latestVersion: null,

    checking: false,

    async init() {

        Logger.info("Update Manager gestartet.");

        await this.check();

    },

    async check() {

        if (this.checking) return;

        this.checking = true;

        try {

            const response = await API.get("/version");

            if (!response) {

                this.checking = false;

                return;

            }

            this.latestVersion = response.version;

            if (this.isNewer()) {

                NotificationCenter.info(

                    "Update verfügbar",

                    "Version " + this.latestVersion
                );

                Toast.info(

                    "Neue Version verfügbar."

                );

            } else {

                Logger.success(

                    "System aktuell."

                );

            }

        }

        catch(error){

            Logger.error(

                "Updateprüfung fehlgeschlagen.",

                error

            );

        }

        this.checking = false;

    },

    isNewer() {

        return (

            this.latestVersion &&

            this.latestVersion !== this.currentVersion

        );

    },

    info() {

        return {

            installed: this.currentVersion,

            latest: this.latestVersion,

            updateAvailable: this.isNewer()

        };

    }

};

window.UpdateManager = UpdateManager;
