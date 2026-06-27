/**
 * =====================================================
 * AI Empire Pro V8
 * Telegram Module
 * Datei: modules/telegram/telegram.js
 * =====================================================
 */

const Telegram = {

    initialized: false,

    data: {

        connected: false,

        botToken: "",

        chatId: "",

        bots: [],

        broadcasts: []

    },

    init() {

        if (this.initialized) return;

        this.load();

        this.initialized = true;

        console.log("✔ Telegram Modul gestartet.");

    },

    load() {

        const saved = StateManager.get("telegram");

        if (saved) {

            this.data = {

                ...this.data,

                ...saved

            };

        }

    },

    save() {

        StateManager.set("telegram", this.data);

        StorageManager.save();

    },

    connect(token, chatId) {

        this.data.connected = true;

        this.data.botToken = token;

        this.data.chatId = chatId;

        this.save();

    },

    disconnect() {

        this.data.connected = false;

        this.data.botToken = "";

        this.data.chatId = "";

        this.save();

    },

    addBot(bot) {

        bot.id = Utils.uuid();

        bot.created = Utils.formatDate();

        this.data.bots.push(bot);

        this.save();

    },

    removeBot(id) {

        this.data.bots = this.data.bots.filter(

            bot => bot.id !== id

        );

        this.save();

    },

    addBroadcast(message) {

        this.data.broadcasts.push({

            id: Utils.uuid(),

            message,

            created: Utils.formatDate()

        });

        this.save();

    },

    getBots() {

        return this.data.bots;

    },

    getBroadcasts() {

        return this.data.broadcasts;

    },

    isConnected() {

        return this.data.connected;

    }

};

window.Telegram = Telegram;
