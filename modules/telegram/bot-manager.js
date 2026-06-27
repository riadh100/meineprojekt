/**
 * =====================================================
 * AI Empire Pro V8
 * Telegram - Bot Manager
 * Datei: modules/telegram/bot-manager.js
 * =====================================================
 */

const BotManager = {

    bots: [],

    init() {

        this.load();

        console.log("✔ Bot Manager gestartet.");

    },

    add(name, token, chatId) {

        const bot = {

            id: Utils.uuid(),

            name: name,

            token: token,

            chatId: chatId,

            active: true,

            created: Utils.formatDate()

        };

        this.bots.push(bot);

        this.save();

        return bot;

    },

    update(id, data) {

        const bot = this.bots.find(
            item => item.id === id
        );

        if (!bot) return false;

        Object.assign(bot, data);

        this.save();

        return true;

    },

    remove(id) {

        this.bots = this.bots.filter(
            item => item.id !== id
        );

        this.save();

    },

    enable(id) {

        const bot = this.get(id);

        if (!bot) return;

        bot.active = true;

        this.save();

    },

    disable(id) {

        const bot = this.get(id);

        if (!bot) return;

        bot.active = false;

        this.save();

    },

    get(id) {

        return this.bots.find(
            item => item.id === id
        );

    },

    getAll() {

        return this.bots;

    },

    clear() {

        this.bots = [];

        this.save();

    },

    save() {

        StateManager.set(
            "telegram.bots",
            this.bots
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "telegram.bots"
        );

        if (Array.isArray(data)) {

            this.bots = data;

        }

    }

};

window.BotManager = BotManager;
