/**
 * =====================================================
 * AI Empire Pro V8
 * Trading - Trade History
 * Datei: modules/trading/trade-history.js
 * =====================================================
 */

const TradeHistory = {

    trades: [],

    init() {

        this.load();

        console.log("✔ Trade History gestartet.");

    },

    add(trade) {

        trade.id = Utils.uuid();

        trade.date = Utils.formatDate();

        this.trades.push(trade);

        this.save();

        return trade;

    },

    update(id, data) {

        const trade = this.trades.find(
            item => item.id === id
        );

        if (!trade) return false;

        Object.assign(trade, data);

        this.save();

        return true;

    },

    remove(id) {

        this.trades = this.trades.filter(
            item => item.id !== id
        );

        this.save();

    },

    get(id) {

        return this.trades.find(
            item => item.id === id
        );

    },

    getAll() {

        return this.trades;

    },

    getBySymbol(symbol) {

        return this.trades.filter(
            item => item.symbol === symbol
        );

    },

    clear() {

        this.trades = [];

        this.save();

    },

    save() {

        StateManager.set(
            "trading.history",
            this.trades
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "trading.history"
        );

        if (Array.isArray(data)) {

            this.trades = data;

        }

    }

};

window.TradeHistory = TradeHistory;
