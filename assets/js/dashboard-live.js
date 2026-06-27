/**
 * =====================================================
 * AI Empire Pro V8
 * Live Dashboard
 * Datei: assets/js/dashboard-live.js
 * =====================================================
 */

const DashboardLive = {

    interval: null,

    start() {

        this.stop();

        this.update();

        this.interval = setInterval(() => {

            this.update();

        }, 5000);

    },

    stop() {

        if (this.interval) {

            clearInterval(this.interval);

            this.interval = null;

        }

    },

    async update() {

        try {

            const data = await API.dashboard();

            if (!data) return;

            if (data.balance !== undefined) {

                Card.update(

                    "card-balance",

                    Helpers.formatCurrency(data.balance)

                );

            }

            if (data.profit !== undefined) {

                Card.update(

                    "card-profit",

                    Helpers.formatCurrency(data.profit)

                );

            }

            if (data.trades !== undefined) {

                Card.update(

                    "card-trades",

                    Helpers.formatNumber(data.trades)

                );

            }

            if (data.users !== undefined) {

                Card.update(

                    "card-users",

                    Helpers.formatNumber(data.users)

                );

            }

            if (data.chart) {

                Chart.update(

                    "dashboardChart",

                    data.chart.labels,

                    data.chart.values

                );

            }

        }

        catch(error){

            console.error(error);

        }

    }

};

window.DashboardLive = DashboardLive;
