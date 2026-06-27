/**
 * =====================================================
 * AI Empire Pro V8
 * Backend - Achievement Model
 * Datei: backend/models/Achievement.js
 * =====================================================
 */

class Achievement {

    constructor(data = {}) {

        this.id = data.id || Date.now();

        this.title = data.title || "";

        this.description = data.description || "";

        this.xp = Number(data.xp || 100);

        this.unlocked = data.unlocked || false;

        this.unlockedAt = data.unlockedAt || null;

        this.createdAt = data.createdAt || new Date().toISOString();

    }

    unlock() {

        this.unlocked = true;

        this.unlockedAt = new Date().toISOString();

    }

    lock() {

        this.unlocked = false;

        this.unlockedAt = null;

    }

    update(data = {}) {

        Object.assign(this, data);

    }

    toJSON() {

        return {

            id: this.id,

            title: this.title,

            description: this.description,

            xp: this.xp,

            unlocked: this.unlocked,

            unlockedAt: this.unlockedAt,

            createdAt: this.createdAt

        };

    }

}

module.exports = Achievement;
