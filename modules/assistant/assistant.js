/**
 * =====================================================
 * AI Empire Pro V8
 * Assistant Module
 * Datei: modules/assistant/assistant.js
 * =====================================================
 */

const Assistant = {

    initialized: false,

    data: {
        conversations: [],
        currentChat: null,
        promptLibrary: []
    },

    init() {

        if (this.initialized) return;

        this.load();

        this.initialized = true;

        console.log("✔ Assistant gestartet.");

    },

    load() {

        const saved = StateManager.get("assistant");

        if (saved) {

            this.data = {
                ...this.data,
                ...saved
            };

        }

    },

    save() {

        StateManager.set("assistant", this.data);

        StorageManager.save();

    },

    createChat(title = "Neuer Chat") {

        const chat = {

            id: Utils.uuid(),

            title: title,

            created: Utils.formatDate(),

            messages: []

        };

        this.data.conversations.push(chat);

        this.data.currentChat = chat.id;

        this.save();

        return chat;

    },

    sendMessage(role, content) {

        const chat = this.getCurrentChat();

        if (!chat) return;

        chat.messages.push({

            id: Utils.uuid(),

            role: role,

            content: content,

            timestamp: Utils.formatDate()

        });

        this.save();

    },

    getCurrentChat() {

        return this.data.conversations.find(
            chat => chat.id === this.data.currentChat
        );

    },

    setCurrentChat(id) {

        this.data.currentChat = id;

        this.save();

    },

    deleteChat(id) {

        this.data.conversations =
            this.data.conversations.filter(
                chat => chat.id !== id
            );

        if (this.data.currentChat === id) {
            this.data.currentChat = null;
        }

        this.save();

    },

    getChats() {

        return this.data.conversations;

    },

    reset() {

        this.data = {

            conversations: [],

            currentChat: null,

            promptLibrary: []

        };

        this.save();

    }

};

window.Assistant = Assistant;
