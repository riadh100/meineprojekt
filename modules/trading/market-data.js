/**
 * =====================================================
 * AI Empire Pro V8
 * Trading - Market Data
 * Datei: modules/trading/market-data.js
 * =====================================================
 */

const MarketData = {

    endpoint: "",

    prices: {},

    setEndpoint(url) {

        this.endpoint = url;

    },

    async fetch(symbol) {

        if (!this.endpoint) {

            console.warn("Keine API konfiguriert.");

            return null;

        }

        try {

            const response = await fetch(
                `${this.endpoint}?symbol=${symbol}`
            );

            const data = await response.json();

            this.prices[symbol] = data;

            return data;

        } catch (error) {

            console.error(error);

            return null;

        }

    },

    setPrice(symbol, price) {

        this.prices[symbol] = {

            symbol,

            price,

            updated: Utils.formatDate()

        };

    },

    getPrice(symbol) {

        return this.prices[symbol] || null;

    },

    getAll() {

        return this.prices;

    },

    remove(symbol) {

        delete this.prices[symbol];

    },

    clear() {

        this.prices = {};

    }

};

window.MarketData = MarketData;
