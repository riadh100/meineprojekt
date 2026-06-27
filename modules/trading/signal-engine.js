/**
 * =====================================================
 * AI Empire Pro V8
 * Trading - Signal Engine
 * Datei: modules/trading/signal-engine.js
 * =====================================================
 */

const SignalEngine = {

    signals: [],

    init() {

        this.load();

        console.log("✔ Signal Engine gestartet.");

    },

    create(symbol, type, price, confidence = 0) {

        const signal = {

            id: Utils.uuid(),

            symbol: symbol,

            type: type,

            price: Number(price),

            confidence: Number(confidence),

            status: "OPEN",

            created: Utils.formatDate()

        };

        this.signals.push(signal);

        this.save();

        return signal;

    },

    close(id) {

        const signal = this.signals.find(
            item => item.id === id
        );

        if (!signal) return;

        signal.status = "CLOSED";

        signal.closed = Utils.formatDate();

        this.save();

    },

    remove(id) {

        this.signals = this.signals.filter(
            item => item.id !== id
        );

        this.save();

    },

    get(id) {

        return this.signals.find(
            item => item.id === id
        );

    },

    getAll() {

        return this.signals;

    },

    getOpen() {

        return this.signals.filter(
            item => item.status === "OPEN"
        );

    },

    getClosed() {

        return this.signals.filter(
            item => item.status === "CLOSED"
        );

    },

    clear() {

        this.signals = [];

        this.save();

    },

    save() {

        StateManager.set(
            "trading.signals",
            this.signals
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "trading.signals"
        );

        if (Array.isArray(data)) {

            this.signals = data;

        }

    }

};

window.SignalEngine = SignalEngine;
