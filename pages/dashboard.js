/**
 * =====================================================
 * AI Empire Pro V8
 * Dashboard Page
 * Datei: pages/dashboard.js
 * =====================================================
 */

const DashboardPage = {

    render(containerId = "app") {

        const app = document.getElementById(containerId);

        if (!app) return;

        app.innerHTML = `

            <div class="page dashboard-page">

                <h1>Dashboard 🚀 AI Empire Pro V9</h1>

                <div class="dashboard-cards">

                    ${Card.create({
                        id: "card-balance",
                        title: "Kontostand",
                        value: DashboardKPI.get("balance") + " €",
                        subtitle: "Aktuelles Guthaben",
                        icon: "💰"
                    })}

                    ${Card.create({
                        id: "card-profit",
                        title: "Gewinn",
                        value: DashboardKPI.get("profit") + " €",
                        subtitle: "Gesamtgewinn",
                        icon: "📈"
                    })}

                    ${Card.create({
                        id: "card-trades",
                        title: "Trades",
                        value: DashboardKPI.get("trades"),
                        subtitle: "Abgeschlossene Trades",
                        icon: "📊"
                    })}

                    ${Card.create({
                        id: "card-users",
                        title: "Benutzer",
                        value: DashboardKPI.get("users"),
                        subtitle: "Aktive Benutzer",
                        icon: "👥"
                    })}

                </div>

                <div class="dashboard-chart">

                    <canvas
                        id="dashboardChart"
                        width="900"
                        height="320">
                    </canvas>

                </div>

                <div id="dashboard-table"></div>

            </div>

        `;

        Chart.create("dashboardChart", {

            labels: [

                "Mo",
                "Di",
                "Mi",
                "Do",
                "Fr",
                "Sa",
                "So"

            ],

            values: [

                120,
                180,
                160,
                260,
                310,
                295,
                420

            ]

        });

        Table.render(

            "dashboard-table",

            [

                "KPI",
                "Wert"

            ],

            [

                ["Empire Score", DashboardKPI.get("balance")],

                ["Gewinn", DashboardKPI.get("profit")],

                ["Trades", DashboardKPI.get("trades")],

                ["Benutzer", DashboardKPI.get("users")]

            ]

        );

    }

};

window.DashboardPage = DashboardPage;
