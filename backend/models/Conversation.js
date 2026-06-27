/**
 * =====================================================
 * AI Empire Pro V8
 * Backend - Conversation Model
 * Datei: backend/models/Conversation.js
 * =====================================================
 */

class Conversation {

    constructor(data = {}) {

        this.id = data.id || Date.now();

        this.title = data.title || "Neuer Chat";

        this.messages = data.messages || [];

        this.createdAt = data.createdAt || new Date().toISOString();

        this.updatedAt = data.updatedAt || new Date().toISOString();

    }

    addMessage(role, content) {

        this.messages.push({

            id: Date.now(),

            role: role,

            content: content,

            createdAt: new Date().toISOString()

        });

        this.updatedAt = new Date().toISOString();

    }

    removeMessage(id) {

        this.messages = this.messages.filter(

            message => message.id !== id

        );

        this.updatedAt = new Date().toISOString();

    }

    clearMessages() {

        this.messages = [];

        this.updatedAt = new Date().toISOString();

    }

    update(data = {}) {

        Object.assign(this, data);

        this.updatedAt = new Date().toISOString();

    }

    toJSON() {

        return {

            id: this.id,

            title: this.title,

            messages: this.messages,

            createdAt: this.createdAt,

            updatedAt: this.updatedAt

        };

    }

}

module.exports = Conversation;
