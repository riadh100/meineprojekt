/**
 * =====================================================
 * AI Empire Pro V8
 * Backend - Trade Model
 * Datei: backend/models/Trade.js
 * =====================================================
 */

class Trade {

    constructor(data = {}) {

        this.id = data.id || Date.now();

        this.symbol = data.symbol || "";

        this.type = data.type || "BUY";

        this.amount = Number(data.amount || 0);

        this.entryPrice = Number(data.entryPrice || 0);

        this.exitPrice = Number(data.exitPrice || 0);

        this.profit = Number(data.profit || 0);

        this.status = data.status || "OPEN";

        this.createdAt = data.createdAt || new Date().toISOString();

        this.closedAt = data.closedAt || null;

    }

    close(exitPrice) {

        this.exitPrice = Number(exitPrice);

        this.profit =
            (this.exitPrice - this.entryPrice) * this.amount;

        this.status = "CLOSED";

        this.closedAt = new Date().toISOString();

    }

    update(data = {}) {

        Object.assign(this, data);

    }

    toJSON() {

        return {

            id: this.id,

            symbol: this.symbol,

            type: this.type,

            amount: this.amount,

            entryPrice: this.entryPrice,

            exitPrice: this.exitPrice,

            profit: this.profit,

            status: this.status,

            createdAt: this.createdAt,

            closedAt: this.closedAt

        };

    }

}

module.exports = Trade;
