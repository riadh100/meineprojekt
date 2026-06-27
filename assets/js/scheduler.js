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

    add(name, callback, delay = 1000, repeat = false) {

        const job = {

            id: Helpers.uuid(),

            name,

            callback,

            delay,

            repeat,

            nextRun: Date.now() + delay,

            created: new Date().toISOString(),

            enabled: true

        };

        this.jobs.push(job);

        this.save();

        Logger.info(`Scheduler Job hinzugefügt: ${name}`);

        return job.id;

    },

    remove(id) {

        this.jobs = this.jobs.filter(

            job => job.id !== id

        );

        this.save();

    },

    enable(id) {

        const job = this.jobs.find(j => j.id === id);

        if (job) {

            job.enabled = true;

            this.save();

        }

    },

    disable(id) {

        const job = this.jobs.find(j => j.id === id);

        if (job) {

            job.enabled = false;

            this.save();

        }

    },

    tick() {

        const now = Date.now();

        this.jobs.forEach(job => {

            if (

                !job.enabled ||

                now < job.nextRun

            ) return;

            try {

                if (typeof job.callback === "function") {

                    job.callback();

                }

            }

            catch(error){

                Logger.error(

                    `Scheduler Fehler (${job.name})`,

                    error

                );

            }

            if (job.repeat) {

                job.nextRun = now + job.delay;

            }

            else {

                job.enabled = false;

            }

        });

    },

    save() {

        const exportJobs = this.jobs.map(job => ({

            ...job,

            callback: null

        }));

        localStorage.setItem(

            "scheduler",

            JSON.stringify(exportJobs)

        );

    },

    load() {

        const data = localStorage.getItem("scheduler");

        if (!data) return;

        try {

            this.jobs = JSON.parse(data);

        }

        catch {

            this.jobs = [];

        }

    },

    getAll() {

        return this.jobs;

    }

};

window.Scheduler = Scheduler;
