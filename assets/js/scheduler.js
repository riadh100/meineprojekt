/**
 * =====================================================
 * AI Empire Pro V8
 * Scheduler
 * Datei: assets/js/scheduler.js
 * =====================================================
 */

const Scheduler = {

    jobs: [],

    timer: null,

    init() {

        this.load();

        this.start();

        Logger.success("Scheduler gestartet.");

    },

    start() {

        this.stop();

        this.timer = setInterval(() => {

            this.tick();

        }, 1000);

    },

    stop() {

        if (this.timer) {

            clearInterval(this.timer);

            this.timer = null;

        }

    },

    add(name, callback, delay
