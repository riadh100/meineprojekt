/**
 * =====================================================
 * AI Empire Pro V8
 * Telegram - Broadcast System
 * Datei: modules/telegram/broadcast-system.js
 * =====================================================
 */

const BroadcastSystem = {

    broadcasts: [],

    init() {

        this.load();

        console.log("✔ Broadcast System gestartet.");

    },

    create(title, message) {

        const broadcast = {

            id: Utils.uuid(),

            title: title,

            message: message,

            status: "PENDING",

            created: Utils.formatDate(),

            sent: null

        };

        this.broadcasts.push(broadcast);

        this.save();

        return broadcast;

    },

    send(id) {

        const broadcast = this.get(id);

        if (!broadcast) return false;

        broadcast.status = "SENT";

        broadcast.sent = Utils.formatDate();

        this.save();

        return true;

    },

    cancel(id) {

        const broadcast = this.get(id);

        if (!broadcast) return false;

        broadcast.status = "CANCELLED";

        this.save();

        return true;

    },

    remove(id) {

        this.broadcasts = this.broadcasts.filter(
            item => item.id !== id
        );

        this.save();

    },

    get(id) {

        return this.broadcasts.find(
            item => item.id === id
        );

    },

    getAll() {

        return this.broadcasts;

    },

    getPending() {

        return this.broadcasts.filter(
            item => item.status === "PENDING"
        );

    },

    getSent() {

        return this.broadcasts.filter(
            item => item.status === "SENT"
        );

    },

    clear() {

        this.broadcasts = [];

        this.save();

    },

    save() {

        StateManager.set(
            "telegram.broadcasts",
            this.broadcasts
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "telegram.broadcasts"
        );

        if (Array.isArray(data)) {

            this.broadcasts = data;

        }

    }

};

window.BroadcastSystem = BroadcastSystem;
