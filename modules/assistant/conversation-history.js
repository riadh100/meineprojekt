/**
 * =====================================================
 * AI Empire Pro V8
 * Assistant - Conversation History
 * Datei: modules/assistant/conversation-history.js
 * =====================================================
 */

const ConversationHistory = {

    history: [],

    init() {

        this.load();

        console.log("✔ Conversation History geladen.");

    },

    add(chat) {

        if (!chat) return;

        this.history.unshift({

            id: chat.id,

            title: chat.title,

            created: chat.created,

            messages: chat.messages.length,

            lastUpdated: Utils.formatDate()

        });

        this.save();

    },

    update(chat) {

        const item = this.history.find(
            history => history.id === chat.id
        );

        if (!item) return;

        item.title = chat.title;
        item.messages = chat.messages.length;
        item.lastUpdated = Utils.formatDate();

        this.save();

    },

    remove(id) {

        this.history = this.history.filter(
            item => item.id !== id
        );

        this.save();

    },

    clear() {

        this.history = [];

        this.save();

    },

    get(id) {

        return this.history.find(
            item => item.id === id
        );

    },

    getAll() {

        return this.history;

    },

    save() {

        StateManager.set(
            "assistant.history",
            this.history
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "assistant.history"
        );

        if (Array.isArray(data)) {

            this.history = data;

        }

    }

};

window.ConversationHistory = ConversationHistory;
