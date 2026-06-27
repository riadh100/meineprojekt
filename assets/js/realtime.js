/**
 * =====================================================
 * AI Empire Pro V8
 * Realtime Engine
 * Datei: assets/js/realtime.js
 * =====================================================
 */

const Realtime = {

    timers: {},

    started: false,

    init() {

        if (this.started) return;

        this.started = true;

        this.startDashboard();

        this.startClock();

        this.startMemoryMonitor();

        this.startConnectionMonitor();

        Logger.success("Realtime Engine gestartet.");

    },

    startDashboard() {

        this.stop("dashboard");

        this.timers.dashboard = setInterval(async () => {

            try {

                if (typeof DashboardLive !== "undefined") {

                    await DashboardLive.update();

                }

            } catch (error) {

                Logger.error(

                    "Dashboard Update Fehler",

                    error

                );

            }

        }, 10000);

    },

    startClock() {

        this.stop("clock");

        this.timers.clock = setInterval(() => {

            const element = document.getElementById("ui-clock");

            if (element) {

                element.textContent =

                    new Date().toLocaleTimeString("de-DE");

            }

        }, 1000);

    },

    startMemoryMonitor() {

        this.stop("memory");

        this.timers.memory = setInterval(() => {

            if (!performance || !performance.memory) return;

            const used = Math.round(

                performance.memory.usedJSHeapSize / 1024 / 1024

            );

            Logger.info(

                "RAM",

                used + " MB"

            );

        }, 60000);

    },

    startConnectionMonitor() {

        window.addEventListener("online", () => {

            NotificationCenter.success(

                "Internet",

                "Verbindung wiederhergestellt"

            );

        });

        window.addEventListener("offline", () => {

            NotificationCenter.warning(

                "Internet",

                "Keine Internetverbindung"

            );

        });

    },

    stop(name) {

        if (!this.timers[name]) return;

        clearInterval(this.timers[name]);

        delete this.timers[name];

    },

    stopAll() {

        Object.keys(this.timers).forEach(name => {

            this.stop(name);

        });

    }

};

window.Realtime = Realtime;
