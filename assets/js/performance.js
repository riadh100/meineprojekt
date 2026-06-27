/**
 * =====================================================
 * AI Empire Pro V8
 * Performance Manager
 * Datei: assets/js/performance.js
 * =====================================================
 */

const PerformanceManager = {

    metrics: {

        startTime: performance.now(),

        loadTime: 0,

        renderTime: 0,

        apiCalls: 0,

        apiErrors: 0,

        pageSwitches: 0

    },

    init() {

        window.addEventListener("load", () => {

            this.metrics.loadTime = Math.round(

                performance.now()

            );

            Logger.success(

                "Seite geladen",

                this.metrics.loadTime + " ms"

            );

        });

        console.log("✔ Performance Manager gestartet.");

    },

    measureRender(callback) {

        const start = performance.now();

        callback();

        this.metrics.renderTime = Math.round(

            performance.now() - start

        );

        Logger.info(

            "Renderzeit",

            this.metrics.renderTime + " ms"

        );

    },

    apiRequest(success = true) {

        this.metrics.apiCalls++;

        if (!success) {

            this.metrics.apiErrors++;

        }

    },

    pageSwitch() {

        this.metrics.pageSwitches++;

    },

    getStats() {

        return {

            loadTime:

                this.metrics.loadTime + " ms",

            renderTime:

                this.metrics.renderTime + " ms",

            apiCalls:

                this.metrics.apiCalls,

            apiErrors:

                this.metrics.apiErrors,

            pageSwitches:

                this.metrics.pageSwitches,

            uptime:

                Math.round(

                    (performance.now() -

                    this.metrics.startTime) / 1000

                ) + " s"

        };

    },

    reset() {

        this.metrics = {

            startTime: performance.now(),

            loadTime: 0,

            renderTime: 0,

            apiCalls: 0,

            apiErrors: 0,

            pageSwitches: 0

        };

        Logger.info("Performance-Metriken zurückgesetzt.");

    }

};

window.PerformanceManager = PerformanceManager;
