/**
 * =====================================================
 * AI Empire Pro V8
 * Dashboard UI
 * Datei: modules/dashboard/dashboard-ui.js
 * =====================================================
 */

const DashboardUI = {

    container: null,

    init(containerId = "app") {

        this.container = document.getElementById(containerId);

        if (!this.container) {

            console.error("Dashboard Container nicht gefunden.");

            return;

        }

        this.render();

    },

    render() {

        this.container.innerHTML = `
            <div class="dashboard">

                <h1>Dashboard</h1>

                <div class="dashboard-grid">

                    <div class="card">
                        <h3>Kontostand</h3>
                        <h2 id="dashboard-balance">0 €</h2>
                    </div>

                    <div class="card">
                        <h3>Gewinn</h3>
                        <h2 id="dashboard-profit">0 €</h2>
                    </div>

                    <div class="card">
                        <h3>Trades</h3>
                        <h2 id="dashboard-trades">0</h2>
                    </div>

                    <div class="card">
                        <h3>Benutzer</h3>
                        <h2 id="dashboard-users">1</h2>
                    </div>

                </div>

            </div>
        `;

        this.refresh();

    },

    refresh() {

        document.getElementById("dashboard-balance").textContent =
            Dashboard.get("balance") + " €";

        document.getElementById("dashboard-profit").textContent =
            Dashboard.get("profit") + " €";

        document.getElementById("dashboard-trades").textContent =
            Dashboard.get("trades");

        document.getElementById("dashboard-users").textContent =
            Dashboard.get("users");

    }

};

window.DashboardUI = DashboardUI;
