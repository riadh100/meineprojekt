/**
 * =====================================================
 * AI Empire Pro V8
 * Server Entry Point
 * Datei: server/server.js
 * =====================================================
 */

require("dotenv").config();

const http = require("http");

const app = require("./app");

const databaseService = require("./services/databaseService");
const websocketService = require("./services/websocketService");
const telegramService = require("./services/telegramService");
const configService = require("./services/configService");

const PORT = process.env.PORT || 3000;

const HOST = process.env.HOST || "0.0.0.0";

async function start() {

    try {

        configService.init();

        const databaseConnected = await databaseService.connect();

        if (!databaseConnected) {

            console.warn(

                "Server läuft ohne Datenbank."

            );

        }

        telegramService.init();

        const server = http.createServer(app);

        websocketService.init(server);

        server.listen(

            PORT,

            HOST,

            () => {

                console.log("");

                console.log(

                    "===================================="

                );

                console.log(

                    " AI Empire Pro V8 gestartet"

                );

                console.log(

                    "===================================="

                );

                console.log(

                    `Host: http://${HOST}:${PORT}`

                );

                console.log(

                    `Port: ${PORT}`

                );

                console.log(

                    `Node: ${process.version}`

                );

                console.log(

                    `Environment: ${process.env.NODE_ENV || "development"}`

                );

                console.log(

                    "===================================="

                );

            }

        );

        process.on(

            "SIGINT",

            async () => {

                console.log(

                    "\nServer wird beendet..."

                );

                await databaseService.disconnect();

                server.close(() => {

                    process.exit(0);

                });

            }

        );

        process.on(

            "SIGTERM",

            async () => {

                console.log(

                    "\nServer wird beendet..."

                );

                await databaseService.disconnect();

                server.close(() => {

                    process.exit(0);

                });

            }

        );

    }

    catch (error) {

        console.error(

            "Serverstart fehlgeschlagen:",

            error

        );

        process.exit(1);

    }

}

start();
