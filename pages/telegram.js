/**
 * =====================================================
 * AI Empire Pro V8
 * Telegram Page
 * Datei: pages/telegram.js
 * =====================================================
 */

const TelegramPage = {

    render(containerId = "app") {

        const app = document.getElementById(containerId);

        if (!app) return;

        app.innerHTML = `

            <div class="page telegram-page">

                <div class="page-header">

                    <h1>Telegram Center</h1>

                </div>

                <div class="dashboard-cards">

                    ${Card.create({
                        id: "telegram-status",
                        title: "Verbindung",
                        value: Telegram.isConnected() ? "Online" : "Offline",
                        subtitle: "Bot Status",
                        icon: "📨"
                    })}

                    ${Card.create({
                        id: "telegram-bots",
                        title: "Bots",
                        value: BotManager.getAll().length,
                        subtitle: "Registriert",
                        icon: "🤖"
                    })}

                    ${Card.create({
                        id: "telegram-broadcasts",
                        title: "Broadcasts",
                        value: BroadcastSystem.getAll().length,
                        subtitle: "Gesendet",
                        icon: "📢"
                    })}

                </div>

                <h2>Bot Manager</h2>

                <div id="bots-table"></div>

                <h2>Broadcasts</h2>

                <div id="broadcast-table"></div>

            </div>

        `;

        this.renderBots();

        this.renderBroadcasts();

    },

    renderBots() {

        const rows = BotManager.getAll().map(bot => [

            bot.name,

            bot.chatId,

            bot.active ? "Online" : "Offline",

            bot.created

        ]);

        Table.render(

            "bots-table",

            [

                "Bot",

                "Chat ID",

                "Status",

                "Erstellt"

            ],

            rows

        );

    },

    renderBroadcasts() {

        const rows = BroadcastSystem.getAll().map(item => [

            item.title,

            item.status,

            item.created,

            item.sent || "-"

        ]);

        Table.render(

            "broadcast-table",

            [

                "Titel",

                "Status",

                "Erstellt",

                "Gesendet"

            ],

            rows

        );

    }

};

window.TelegramPage = TelegramPage;
