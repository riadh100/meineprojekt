/**
 * =====================================================
 * AI Empire Pro V8
 * Backend - Mission Model
 * Datei: backend/models/Mission.js
 * =====================================================
 */

class Mission {

    constructor(data = {}) {

        this.id = data.id || Date.now();

        this.title = data.title || "";

        this.description = data.description || "";

        this.rewardXP = Number(data.rewardXP || 100);

        this.completed = data.completed || false;

        this.completedAt = data.completedAt || null;

        this.createdAt = data.createdAt || new Date().toISOString();

    }

    complete() {

        this.completed = true;

        this.completedAt = new Date().toISOString();

    }

    reopen() {

        this.completed = false;

        this.completedAt = null;

    }

    update(data = {}) {

        Object.assign(this, data);

    }

    toJSON() {

        return {

            id: this.id,

            title: this.title,

            description: this.description,

            rewardXP: this.rewardXP,

            completed: this.completed,

            completedAt: this.completedAt,

            createdAt: this.createdAt

        };

    }

}

module.exports = Mission;
