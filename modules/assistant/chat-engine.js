/**
 * =====================================================
 * AI Empire Pro V8
 * Assistant - Chat Engine
 * Datei: modules/assistant/chat-engine.js
 * =====================================================
 */

const ChatEngine = {

    send(role, content) {

        const chat = Assistant.getCurrentChat();

        if (!chat) {
            console.error("Kein Chat ausgewählt.");
            return;
        }

        chat.messages.push({

            id: Utils.uuid(),

            role: role,

            content: content,

            timestamp: Utils.formatDate()

        });

        Assistant.save();

    },

    user(message) {

        this.send("user", message);

    },

    assistant(message) {

        this.send("assistant", message);

    },

    system(message) {

        this.send("system", message);

    },

    getMessages() {

        const chat = Assistant.getCurrentChat();

        if (!chat) return [];

        return chat.messages;

    },

    clear() {

        const chat = Assistant.getCurrentChat();

        if (!chat) return;

        chat.messages = [];

        Assistant.save();

    },

    deleteMessage(id) {

        const chat = Assistant.getCurrentChat();

        if (!chat) return;

        chat.messages = chat.messages.filter(
            message => message.id !== id
        );

        Assistant.save();

    },

    count() {

        return this.getMessages().length;

    }

};

window.ChatEngine = ChatEngine;
