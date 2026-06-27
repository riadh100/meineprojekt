/**
 * =====================================================
 * AI Empire Pro V8
 * Dashboard KPI Engine
 * Datei: modules/dashboard/dashboard-kpi.js
 * =====================================================
 */

const DashboardKPI = {

    metrics: {

        balance: 0,
        profit: 0,
        trades: 0,
        winRate: 0,
        users: 1,
        signals: 0

    },

    init() {

        console.log("KPI Engine gestartet.");

    },

    set(name, value) {

        this.metrics[name] = value;

        this.save();

    },

    get(name) {

        return this.metrics[name];

    },

    increment(name, amount = 1) {

        if (typeof this.metrics[name] === "number") {

            this.metrics[name] += amount;

            this.save();

        }

    },

    decrement(name, amount = 1) {

        if (typeof this.metrics[name] === "number") {

            this.metrics[name] -= amount;

            this.save();

        }

    },

    getAll() {

        return this.metrics;

    },

    save() {

        StateManager.set("dashboard.kpis", this.metrics);

        StorageManager.save();

    },

    load() {

        const data = StateManager.get("dashboard.kpis");

        if (data) {

            this.metrics = {
                ...this.metrics,
                ...data
            };

        }

    },

    reset() {

        this.metrics = {

            balance: 0,
            profit: 0,
            trades: 0,
            winRate: 0,
            users: 1,
            signals: 0

        };

        this.save();

    }

};

window.DashboardKPI = DashboardKPI;
