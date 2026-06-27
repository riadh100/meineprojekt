/**
 * =====================================================
 * AI Empire Pro V8
 * Backend - Reward Model
 * Datei: backend/models/Reward.js
 * =====================================================
 */

class Reward {

    constructor(data = {}) {

        this.id = data.id || Date.now();

        this.title = data.title || "";

        this.description = data.description || "";

        this.cost = Number(data.cost || 0);

        this.claimed = data.claimed || false;

        this.claimedAt = data.claimedAt || null;

        this.createdAt = data.createdAt || new Date().toISOString();

    }

    claim() {

        this.claimed = true;

        this.claimedAt = new Date().toISOString();

    }

    unclaim() {

        this.claimed = false;

        this.claimedAt = null;

    }

    update(data = {}) {

        Object.assign(this, data);

    }

    toJSON() {

        return {

            id: this.id,

            title: this.title,

            description: this.description,

            cost: this.cost,

            claimed: this.claimed,

            claimedAt: this.claimedAt,

            createdAt: this.createdAt

        };

    }

}

module.exports = Reward;
