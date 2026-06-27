/**
 * =====================================================
 * AI Empire Pro V8
 * Video - Project Manager
 * Datei: modules/video/project-manager.js
 * =====================================================
 */

const ProjectManager = {

    projects: [],

    init() {

        this.load();

        console.log("✔ Project Manager gestartet.");

    },

    create(name, description = "") {

        const project = {

            id: Utils.uuid(),

            name: name,

            description: description,

            status: "NEW",

            created: Utils.formatDate(),

            updated: Utils.formatDate()

        };

        this.projects.push(project);

        this.save();

        return project;

    },

    update(id, data) {

        const project = this.get(id);

        if (!project) return false;

        Object.assign(project, data);

        project.updated = Utils.formatDate();

        this.save();

        return true;

    },

    remove(id) {

        this.projects = this.projects.filter(
            project => project.id !== id
        );

        this.save();

    },

    get(id) {

        return this.projects.find(
            project => project.id === id
        );

    },

    getAll() {

        return this.projects;

    },

    clear() {

        this.projects = [];

        this.save();

    },

    save() {

        StateManager.set(
            "video.projects",
            this.projects
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "video.projects"
        );

        if (Array.isArray(data)) {

            this.projects = data;

        }

    }

};

window.ProjectManager = ProjectManager;
