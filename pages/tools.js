/**
 * =====================================================
 * AI Empire Pro V8
 * Tools Page
 * Datei: pages/tools.js
 * =====================================================
 */

const ToolsPage = {

    render(containerId = "app") {

        const app = document.getElementById(containerId);

        if (!app) return;

        app.innerHTML = `

            <div class="page tools-page">

                <div class="page-header">

                    <h1>Tools Center</h1>

                </div>

                <div class="dashboard-cards">

                    ${Card.create({
                        id: "tools-apis",
                        title: "APIs",
                        value: APIManager.getAll().length,
                        subtitle: "Konfiguriert",
                        icon: "🔌"
                    })}

                    ${Card.create({
                        id: "tools-logs",
                        title: "Logs",
                        value: LogManager.getAll().length,
                        subtitle: "Einträge",
                        icon: "📜"
                    })}

                    ${Card.create({
                        id: "tools-debug",
                        title: "Debug",
                        value: DebugCenter.enabled ? "Aktiv" : "Aus",
                        subtitle: "Debug Center",
                        icon: "🐞"
                    })}

                </div>

                <h2>API Manager</h2>
                <div id="apis-table"></div>

                <h2>Logs</h2>
                <div id="logs-table"></div>

                <h2>Debug Fehler</h2>
                <div id="debug-table"></div>

            </div>

        `;

        this.renderApis();
        this.renderLogs();
        this.renderDebug();

    },

    renderApis() {

        const rows = APIManager.getAll().map(api => [
            api.name,
            api.url,
            api.active ? "Aktiv" : "Inaktiv",
            api.online === undefined ? "-" : api.online ? "Online" : "Offline"
        ]);

        Table.render(
            "apis-table",
            ["Name", "URL", "Status", "Verbindung"],
            rows
        );

    },

    renderLogs() {

        const rows = LogManager.getAll().map(log => [
            log.type,
            log.message,
            log.timestamp
        ]);

        Table.render(
            "logs-table",
            ["Typ", "Nachricht", "Zeit"],
            rows
        );

    },

    renderDebug() {

        const rows = DebugCenter.getErrors().map(error => [
            "ERROR",
            error.message,
            error.timestamp
        ]);

        Table.render(
            "debug-table",
            ["Typ", "Nachricht", "Zeit"],
            rows
        );

    }

};

window.ToolsPage = ToolsPage;
