/**
 * =====================================================
 * AI Empire Pro V8
 * Trading Module
 * Datei: modules/trading/trading.js
 * =====================================================
 */

const Trading = {

    initialized: false,

    data: {

        portfolio: [],

        signals: [],

        history: []

    },

    init() {

        if (this.initialized) return;

        this.load();

        this.initialized = true;

        console.log("✔ Trading Modul gestartet.");

    },

    load() {

        const saved = StateManager.get("trading");

        if (saved) {

            this.data = {

                ...this.data,

                ...saved

            };

        }

    },

    save() {

        StateManager.set("trading", this.data);

        StorageManager.save();

    },

    addPortfolio(asset) {

        asset.id = Utils.uuid();

        asset.created = Utils.formatDate();

        this.data.portfolio.push(asset);

        this.save();

    },

    removePortfolio(id) {

        this.data.portfolio = this.data.portfolio.filter(

            asset => asset.id !== id

        );

        this.save();

    },

    addSignal(signal) {

        signal.id = Utils.uuid();

        signal.created = Utils.formatDate();

        this.data.signals.push(signal);

        this.save();

    },

    removeSignal(id) {

        this.data.signals = this.data.signals.filter(

            signal => signal.id !== id

        );

        this.save();

    },

    addTrade(trade) {

        trade.id = Utils.uuid();

        trade.date = Utils.formatDate();

        this.data.history.push(trade);

        this.save();

    },

    getPortfolio() {

        return this.data.portfolio;

    },

    getSignals() {

        return this.data.signals;

    },

    getHistory() {

        return this.data.history;

    },

    reset() {

        this.data = {

            portfolio: [],

            signals: [],

            history: []

        };

        this.save();

    }

};

window.Trading = Trading;
