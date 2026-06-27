/**
 * =====================================================
 * AI Empire Pro V8
 * System Monitor
 * Datei: assets/js/system-monitor.js
 * =====================================================
 */

const SystemMonitor = {

    stats: {

        fps: 0,

        memory: 0,

        online: navigator.onLine,

        uptime: Date.now(),

        lastUpdate: null

    },

    interval: null,

    init() {

        this.measureFPS();

        this.start();

        Logger.success("System Monitor gestartet.");

    },

    start() {

        this.stop();

        this.interval = setInterval(() => {

            this.update();

        }, 5000);

    },

    stop() {

        if (this.interval) {

            clearInterval(this.interval);

            this.interval = null;

        }

    },

    update() {

        this.stats.online = navigator.onLine;

        this.stats.lastUpdate = new Date().toISOString();

        if (

            window.performance &&

            performance.memory

        ) {

            this.stats.memory = Math.round(

                performance.memory.usedJSHeapSize /

                1024 /

                1024

            );

        }

        Logger.info(

            "Systemstatus",

            this.getStats()

        );

    },

    measureFPS() {

        let frames = 0;

        let last = performance.now();

        const loop = (time) => {

            frames++;

            if (time >= last + 1000) {

                this.stats.fps = frames;

                frames = 0;

                last = time;

            }

            requestAnimationFrame(loop);

        };

        requestAnimationFrame(loop);

    },

    uptime() {

        const seconds = Math.floor(

            (Date.now() - this.stats.uptime) / 1000

        );

        const hours = Math.floor(seconds / 3600);

        const minutes = Math.floor(

            (seconds % 3600) / 60

        );

        return `${hours}h ${minutes}m`;

    },

    getStats() {

        return {

            fps: this.stats.fps,

            memory: this.stats.memory + " MB",

            online: this.stats.online,

            uptime: this.uptime(),

            lastUpdate: this.stats.lastUpdate

        };

    }

};

window.SystemMonitor = SystemMonitor;
