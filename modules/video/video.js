/**
 * =====================================================
 * AI Empire Pro V8
 * Video Module
 * Datei: modules/video/video.js
 * =====================================================
 */

const Video = {

    initialized: false,

    data: {

        projects: [],

        renderQueue: [],

        exports: []

    },

    init() {

        if (this.initialized) return;

        this.load();

        this.initialized = true;

        console.log("✔ Video Modul gestartet.");

    },

    load() {

        const saved = StateManager.get("video");

        if (saved) {

            this.data = {

                ...this.data,

                ...saved

            };

        }

    },

    save() {

        StateManager.set("video", this.data);

        StorageManager.save();

    },

    createProject(name) {

        const project = {

            id: Utils.uuid(),

            name: name,

            created: Utils.formatDate(),

            status: "NEW"

        };

        this.data.projects.push(project);

        this.save();

        return project;

    },

    removeProject(id) {

        this.data.projects = this.data.projects.filter(

            project => project.id !== id

        );

        this.save();

    },

    getProjects() {

        return this.data.projects;

    },

    addToQueue(projectId) {

        this.data.renderQueue.push({

            id: Utils.uuid(),

            projectId,

            status: "WAITING",

            created: Utils.formatDate()

        });

        this.save();

    },

    export(projectId, format = "mp4") {

        this.data.exports.push({

            id: Utils.uuid(),

            projectId,

            format,

            created: Utils.formatDate()

        });

        this.save();

    },

    reset() {

        this.data = {

            projects: [],

            renderQueue: [],

            exports: []

        };

        this.save();

    }

};

window.Video = Video;
