/**
 * =====================================================
 * AI Empire Pro V8
 * Frontend Initializer
 * Datei: assets/js/init.js
 * =====================================================
 */

document.addEventListener("DOMContentLoaded", () => {

    console.log("====================================");
    console.log(" AI Empire Pro V8");
    console.log(" Frontend wird gestartet...");
    console.log("====================================");

    try {

        if (typeof StorageManager !== "undefined") {

            StorageManager.load();

        }

        if (typeof ThemeManager !== "undefined") {

            ThemeManager.init();

        }

        if (typeof SettingsManager !== "undefined") {

            SettingsManager.init();

        }

        if (typeof Sidebar !== "undefined") {

            Sidebar.render();

        }

        if (typeof Navbar !== "undefined") {

            Navbar.render();

        }

        if (typeof PageRouter !== "undefined") {

            PageRouter.init();

        }

        if (typeof Toast !== "undefined") {

            Toast.success("AI Empire Pro V8 erfolgreich gestartet");

        }

        console.log("Frontend bereit.");

    } catch (error) {

        console.error("Initialisierungsfehler:");

        console.error(error);

        if (typeof Toast !== "undefined") {

            Toast.error("Fehler beim Start des Systems.");

        }

    }

});
