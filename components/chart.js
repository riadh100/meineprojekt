/**
 * =====================================================
 * AI Empire Pro V8
 * Component - Chart
 * Datei: components/chart.js
 * =====================================================
 */

const Chart = {

    charts: {},

    create(id, options = {}) {

        this.charts[id] = {

            id: id,

            type: options.type || "line",

            labels: options.labels || [],

            values: options.values || [],

            title: options.title || ""

        };

        this.render(id);

    },

    render(id) {

        const chart = this.charts[id];

        if (!chart) return;

        const canvas = document.getElementById(id);

        if (!canvas) return;

        const ctx = canvas.getContext("2d");

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        const values = chart.values;

        if (!values.length) return;

        const max = Math.max(...values);

        const min = Math.min(...values);

        const range = max - min || 1;

        const stepX = canvas.width / Math.max(values.length - 1, 1);

        ctx.beginPath();

        values.forEach((value, index) => {

            const x = index * stepX;

            const y = canvas.height - ((value - min) / range) * canvas.height;

            if (index === 0) {

                ctx.moveTo(x, y);

            } else {

                ctx.lineTo(x, y);

            }

        });

        ctx.lineWidth = 2;

        ctx.strokeStyle = "#4CAF50";

        ctx.stroke();

    },

    update(id, labels, values) {

        if (!this.charts[id]) return;

        this.charts[id].labels = labels;

        this.charts[id].values = values;

        this.render(id);

    },

    addPoint(id, label, value) {

        if (!this.charts[id]) return;

        this.charts[id].labels.push(label);

        this.charts[id].values.push(value);

        this.render(id);

    },

    clear(id) {

        if (!this.charts[id]) return;

        this.charts[id].labels = [];

        this.charts[id].values = [];

        this.render(id);

    },

    destroy(id) {

        delete this.charts[id];

    }

};

window.Chart = Chart;
