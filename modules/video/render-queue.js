/**
 * =====================================================
 * AI Empire Pro V8
 * Video - Render Queue
 * Datei: modules/video/render-queue.js
 * =====================================================
 */

const RenderQueue = {

    queue: [],

    init() {

        this.load();

        console.log("✔ Render Queue gestartet.");

    },

    add(projectId, quality = "1080p", format = "mp4") {

        const job = {

            id: Utils.uuid(),

            projectId: projectId,

            quality: quality,

            format: format,

            status: "WAITING",

            progress: 0,

            created: Utils.formatDate()

        };

        this.queue.push(job);

        this.save();

        return job;

    },

    start(id) {

        const job = this.get(id);

        if (!job) return;

        job.status = "RENDERING";

        this.save();

    },

    updateProgress(id, progress) {

        const job = this.get(id);

        if (!job) return;

        job.progress = progress;

        if (progress >= 100) {

            job.progress = 100;

            job.status = "FINISHED";

            job.finished = Utils.formatDate();

        }

        this.save();

    },

    cancel(id) {

        const job = this.get(id);

        if (!job) return;

        job.status = "CANCELLED";

        this.save();

    },

    remove(id) {

        this.queue = this.queue.filter(
            job => job.id !== id
        );

        this.save();

    },

    get(id) {

        return this.queue.find(
            job => job.id === id
        );

    },

    getAll() {

        return this.queue;

    },

    clear() {

        this.queue = [];

        this.save();

    },

    save() {

        StateManager.set(
            "video.renderQueue",
            this.queue
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "video.renderQueue"
        );

        if (Array.isArray(data)) {

            this.queue = data;

        }

    }

};

window.RenderQueue = RenderQueue;
