/**
 * =====================================================
 * AI Empire Pro V8
 * State Synchronization
 * Datei: assets/js/state-sync.js
 * =====================================================
 */

const StateSync = {

    interval: null,

    init() {

        this.restore();

        this.start();

        console.log("✔ State Sync gestartet.");

    },

    start() {

        this.stop();

        this.interval = setInterval(() => {

            this.sync();

        }, 5000);

    },

    stop() {

        if (this.interval) {

            clearInterval(this.interval);

            this.interval = null;

        }

    },

    sync() {

        const state = {

            page: typeof Navigation !== "undefined"
                ? Navigation.getCurrent()
                : "dashboard",

            theme: typeof ThemeSwitcher !== "undefined"
                ? ThemeSwitcher.current
                : "dark",

            sidebarCollapsed: typeof Layout !== "undefined"
                ? Layout.sidebarCollapsed
                : false,

            timestamp: new Date().toISOString()

        };

        localStorage.setItem(

            "app-state",

            JSON.stringify(state)

        );

    },

    restore() {

        const data = localStorage.getItem("app-state");

        if (!data) return;

        try {

            const state = JSON.parse(data);

            if (

                state.page &&

                typeof Navigation !== "undefined"

            ) {

                Navigation.go(state.page);

            }

            if (

                state.theme &&

                typeof ThemeSwitcher !== "undefined"

            ) {

                ThemeSwitcher.current = state.theme;

                ThemeSwitcher.apply();

            }

            if (

                typeof state.sidebarCollapsed === "boolean" &&

                typeof Layout !== "undefined"

            ) {

                Layout.sidebarCollapsed =

                    state.sidebarCollapsed;

                Layout.apply();

            }

        } catch (error) {

            console.error(

                "State konnte nicht wiederhergestellt werden.",

                error

            );

        }

    },

    clear() {

        localStorage.removeItem("app-state");

    }

};

window.StateSync = StateSync;
