/**
 * =====================================================
 * AI Empire Pro V8
 * Dashboard Charts
 * Datei: modules/dashboard/dashboard-charts.js
 * =====================================================
 */

const DashboardCharts = {

    charts: {},

    init() {

        console.log("Dashboard Charts initialisiert.");

    },

    create(id, config = {}) {

        this.charts[id] = {
            id,
            labels: config.labels || [],
            values: config.values || [],
            type: config.type || "line"
        };

    },

    update(id, labels, values) {

        if (!this.charts[id]) return;

        this.charts[id].labels = labels;
        this.charts[id].values = values;

    },

    addPoint(id, label, value) {

        if (!this.charts[id]) return;

        this.charts[id].labels.push(label);
        this.charts[id].values.push(value);

    },

    clear(id) {

        if (!this.charts[id]) return;

        this.charts[id].labels = [];
        this.charts[id].values = [];

    },

    remove(id) {

        delete this.charts[id];

    },

    get(id) {

        return this.charts[id];

    },

    getAll() {

        return this.charts;

    }

};

window.DashboardCharts = DashboardCharts;
