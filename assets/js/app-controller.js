/**
 * =====================================================
 * AI Empire Pro V8
 * Application Controller
 * Datei: assets/js/app-controller.js
 * =====================================================
 */

const AppController = {

    version: "8.0.0",

    started: false,

    init() {

        if (this.started) return;

        this.started = true;

        console.log("====================================");
        console.log("AI Empire Pro V8");
        console.log("Application Controller");
        console.log("Version:", this.version);
        console.log("====================================");

        UI.init();

        Events.init();

        this.loadState();

        this.startHeartbeat();

    },

    loadState() {

        const page = StateManager.get("app.currentPage");

        if (page) {

            PageRouter.navigate(page);

        }

    },

    saveState() {

        StorageManager.save();

    },

    reset() {

        Dialog.confirm(

            "System zurücksetzen",

            "Möchtest du wirklich alle lokalen Daten löschen?",

            () => {

                localStorage.clear();

                location.reload();

            }

        );

    },

    restart() {

        location.reload();

    },

    startHeartbeat() {

        setInterval(() => {

            this.saveState();

        }, 30000);

    },

    info() {

        return {

            app: "AI Empire Pro",

            version: this.version,

            page: PageRouter.getCurrent(),

            theme: ThemeManager.current,

            started: this.started

        };

    }

};

window.AppController = AppController;
