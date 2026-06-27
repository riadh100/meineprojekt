/**
 * =====================================================
 * AI Empire Pro V8
 * Job Manager
 * Datei: assets/js/job-manager.js
 * =====================================================
 */

const JobManager = {

    jobs: [],

    init() {

        this.load();

        Logger.success("Job Manager gestartet.");

    },

    create(name, type = "generic", payload = {}) {

        const job = {

            id: Helpers.uuid(),

            name,

            type,

            payload,

            status: "queued",

            progress: 0,

            created: new Date().toISOString(),

            started: null,

            finished: null

        };

        this.jobs.unshift(job);

        this.save();

        Logger.info(`Job erstellt: ${name}`);

        return job;

    },

    start(id) {

        const job = this.find(id);

        if (!job) return;

        job.status = "running";

        job.started = new Date().toISOString();

        this.save();

    },

    progress(id, value) {

        const job = this.find(id);

        if (!job) return;

        job.progress = Math.max(

            0,

            Math.min(100, value)

        );

        this.save();

    },

    finish(id) {

        const job = this.find(id);

        if (!job) return;

        job.status = "finished";

        job.progress = 100;

        job.finished = new Date().toISOString();

        this.save();

        NotificationCenter.success(

            "Job abgeschlossen",

            job.name

        );

    },

    fail(id, reason = "") {

        const job = this.find(id);

        if (!job) return;

        job.status = "failed";

        job.reason = reason;

        job.finished = new Date().toISOString();

        this.save();

        Logger.error(

            `Job fehlgeschlagen: ${job.name}`,

            reason

        );

    },

    cancel(id) {

        const job = this.find(id);

        if (!job) return;

        job.status = "cancelled";

        job.finished = new Date().toISOString();

        this.save();

    },

    find(id) {

        return this.jobs.find(

            job => job.id === id

        );

    },

    getAll() {

        return this.jobs;

    },

    getRunning() {

        return this.jobs.filter(

            job => job.status === "running"

        );

    },

    clearFinished() {

        this.jobs = this.jobs.filter(

            job =>

                job.status !== "finished" &&

                job.status !== "cancelled"

        );

        this.save();

    },

    save() {

        localStorage.setItem(

            "jobs",

            JSON.stringify(this.jobs)

        );

    },

    load() {

        const data = localStorage.getItem("jobs");

        if (!data) return;

        try {

            this.jobs = JSON.parse(data);

        }

        catch {

            this.jobs = [];

        }

    }

};

window.JobManager = JobManager;
