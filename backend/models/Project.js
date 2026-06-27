/**
 * =====================================================
 * AI Empire Pro V8
 * Backend - Project Model
 * Datei: backend/models/Project.js
 * =====================================================
 */

class Project {

    constructor(data = {}) {

        this.id = data.id || Date.now();

        this.name = data.name || "";

        this.description = data.description || "";

        this.status = data.status || "NEW";

        this.progress = Number(data.progress || 0);

        this.owner = data.owner || "";

        this.createdAt = data.createdAt || new Date().toISOString();

        this.updatedAt = data.updatedAt || new Date().toISOString();

    }

    update(data = {}) {

        Object.assign(this, data);

        this.updatedAt = new Date().toISOString();

    }

    setProgress(progress) {

        this.progress = Number(progress);

        if (this.progress >= 100) {

            this.progress = 100;

            this.status = "COMPLETED";

        }

        this.updatedAt = new Date().toISOString();

    }

    toJSON() {

        return {

            id: this.id,

            name: this.name,

            description: this.description,

            status: this.status,

            progress: this.progress,

            owner: this.owner,

            createdAt: this.createdAt,

            updatedAt: this.updatedAt

        };

    }

}

module.exports = Project;
