/**
 * =====================================================
 * AI Empire Pro V8
 * Trading Page
 * Datei: pages/trading.js
 * =====================================================
 */

const TradingPage = {

    render(containerId = "app") {

        const app = document.getElementById(containerId);

        if (!app) return;

        app.innerHTML = `

            <div class="page trading-page">

                <div class="page-header">

                    <h1>Trading Center</h1>

                </div>

                <div class="dashboard-cards">

                    ${Card.create({
                        id: "portfolio-card",
                        title: "Portfolio",
                        value: Portfolio.getTotalValue().toFixed(2) + " €",
                        subtitle: "Gesamtwert",
                        icon: "💼"
                    })}

                    ${Card.create({
                        id: "signal-card",
                        title: "Signale",
                        value: SignalEngine.getOpen().length,
                        subtitle: "Aktiv",
                        icon: "📡"
                    })}

                    ${Card.create({
                        id: "history-card",
                        title: "Trades",
                        value: TradeHistory.getAll().length,
                        subtitle: "Historie",
                        icon: "📈"
                    })}

                </div>

                <h2>Portfolio</h2>

                <div id="portfolio-table"></div>

                <h2>Signale</h2>

                <div id="signals-table"></div>

            </div>

        `;

        this.renderPortfolio();

        this.renderSignals();

    },

    renderPortfolio() {

        const rows = Portfolio.getAll().map(asset => [

            asset.symbol,

            asset.amount,

            asset.buyPrice,

            asset.currentPrice,

            (asset.amount * asset.currentPrice).toFixed(2) + " €"

        ]);

        Table.render(

            "portfolio-table",

            [

                "Coin",

                "Menge",

                "Kauf",

                "Aktuell",

                "Wert"

            ],

            rows

        );

    },

    renderSignals() {

        const rows = SignalEngine.getAll().map(signal => [

            signal.symbol,

            signal.type,

            signal.price,

            signal.confidence + "%",

            signal.status

        ]);

        Table.render(

            "signals-table",

            [

                "Coin",

                "Signal",

                "Preis",

                "Confidence",

                "Status"

            ],

            rows

        );

    }

};

window.TradingPage = TradingPage;
