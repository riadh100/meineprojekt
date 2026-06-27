/**
 * =====================================================
 * AI Empire Pro V8
 * Backend - Telegram Bot Model
 * Datei: backend/models/Bot.js
 * =====================================================
 */

class Bot {

    constructor(data = {}) {

        this.id = data.id || Date.now();

        this.name = data.name || "";

        this.token = data.token || "";

        this.chatId = data.chatId || "";

        this.active = data.active ?? true;

        this.description = data.description || "";

        this.createdAt = data.createdAt || new Date().toISOString();

        this.updatedAt = data.updatedAt || new Date().toISOString();

    }

    activate() {

        this.active = true;

        this.updatedAt = new Date().toISOString();

    }

    deactivate() {

        this.active = false;

        this.updatedAt = new Date().toISOString();

    }

    update(data = {}) {

        Object.assign(this, data);

        this.updatedAt = new Date().toISOString();

    }

    toJSON() {

        return {

            id: this.id,

            name: this.name,

            token: this.token,

            chatId: this.chatId,

            active: this.active,

            description: this.description,

            createdAt: this.createdAt,

            updatedAt: this.updatedAt

        };

    }

}

module.exports = Bot;
