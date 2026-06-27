/**
 * =====================================================
 * AI Empire Pro V8
 * Trading - Portfolio Manager
 * Datei: modules/trading/portfolio.js
 * =====================================================
 */

const Portfolio = {

    assets: [],

    init() {

        this.load();

        console.log("✔ Portfolio Manager gestartet.");

    },

    add(symbol, amount, buyPrice) {

        const asset = {

            id: Utils.uuid(),

            symbol: symbol,

            amount: Number(amount),

            buyPrice: Number(buyPrice),

            currentPrice: Number(buyPrice),

            created: Utils.formatDate()

        };

        this.assets.push(asset);

        this.save();

        return asset;

    },

    updatePrice(id, price) {

        const asset = this.assets.find(
            item => item.id === id
        );

        if (!asset) return;

        asset.currentPrice = Number(price);

        this.save();

    },

    remove(id) {

        this.assets = this.assets.filter(
            item => item.id !== id
        );

        this.save();

    },

    get(id) {

        return this.assets.find(
            item => item.id === id
        );

    },

    getAll() {

        return this.assets;

    },

    getTotalValue() {

        return this.assets.reduce((total, asset) => {

            return total + (asset.amount * asset.currentPrice);

        }, 0);

    },

    clear() {

        this.assets = [];

        this.save();

    },

    save() {

        StateManager.set(
            "trading.portfolio",
            this.assets
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "trading.portfolio"
        );

        if (Array.isArray(data)) {

            this.assets = data;

        }

    }

};

window.Portfolio = Portfolio;
