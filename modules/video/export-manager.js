/**
 * =====================================================
 * AI Empire Pro V8
 * Video - Export Manager
 * Datei: modules/video/export-manager.js
 * =====================================================
 */

const ExportManager = {

    exports: [],

    init() {

        this.load();

        console.log("✔ Export Manager gestartet.");

    },

    create(projectId, format = "mp4", quality = "1080p") {

        const exportJob = {

            id: Utils.uuid(),

            projectId: projectId,

            format: format,

            quality: quality,

            status: "PENDING",

            fileName: "",

            created: Utils.formatDate(),

            finished: null

        };

        this.exports.push(exportJob);

        this.save();

        return exportJob;

    },

    complete(id, fileName) {

        const job = this.get(id);

        if (!job) return;

        job.status = "COMPLETED";

        job.fileName = fileName;

        job.finished = Utils.formatDate();

        this.save();

    },

    fail(id) {

        const job = this.get(id);

        if (!job) return;

        job.status = "FAILED";

        job.finished = Utils.formatDate();

        this.save();

    },

    remove(id) {

        this.exports = this.exports.filter(
            job => job.id !== id
        );

        this.save();

    },

    get(id) {

        return this.exports.find(
            job => job.id === id
        );

    },

    getAll() {

        return this.exports;

    },

    getCompleted() {

        return this.exports.filter(
            job => job.status === "COMPLETED"
        );

    },

    clear() {

        this.exports = [];

        this.save();

    },

    save() {

        StateManager.set(
            "video.exports",
            this.exports
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "video.exports"
        );

        if (Array.isArray(data)) {

            this.exports = data;

        }

    }

};

window.ExportManager = ExportManager;
