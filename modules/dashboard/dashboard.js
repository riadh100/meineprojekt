/**
 * =====================================================
 * AI Empire Pro V8
 * Dashboard Module
 * Datei: modules/dashboard/dashboard.js
 * =====================================================
 */

const Dashboard = {

    initialized: false,

    data: {
        balance: 0,
        profit: 0,
        trades: 0,
        users: 1
    },

    init() {

        if (this.initialized) return;

        this.load();

        this.initialized = true;

        console.log("✔ Dashboard geladen.");

    },

    load() {

        const saved = StateManager.get("dashboard");

        if (saved) {

            this.data = {
                ...this.data,
                ...saved
            };

        }

    },

    save() {

        StateManager.set("dashboard", this.data);

        StorageManager.save();

    },

    update(key, value) {

        this.data[key] = value;

        this.save();

    },

    increment(key, amount = 1) {

        if (typeof this.data[key] === "number") {

            this.data[key] += amount;

            this.save();

        }

    },

    get(key) {

        return this.data[key];

    },

    getAll() {

        return this.data;

    },

    reset() {

        this.data = {
            balance: 0,
            profit: 0,
            trades: 0,
            users: 1
        };

        this.save();

    },

    render() {

        console.log("===== DASHBOARD =====");

        console.table(this.data);

    }

};

window.Dashboard = Dashboard;
