/**
 * =====================================================
 * AI Empire Pro V8
 * WebSocket Manager
 * Datei: assets/js/websocket.js
 * =====================================================
 */

const WebSocketManager = {

    socket: null,

    connected: false,

    reconnectDelay: 5000,

    url: "ws://localhost:3000",

    init() {

        this.connect();

        console.log("✔ WebSocket Manager gestartet.");

    },

    connect() {

        try {

            this.socket = new WebSocket(this.url);

            this.socket.onopen = () => {

                this.connected = true;

                Logger.success("WebSocket verbunden.");

                NotificationCenter.success(

                    "WebSocket",

                    "Verbindung hergestellt."

                );

            };

            this.socket.onmessage = (event) => {

                this.handle(event.data);

            };

            this.socket.onerror = (error) => {

                Logger.error(

                    "WebSocket Fehler",

                    error

                );

            };

            this.socket.onclose = () => {

                this.connected = false;

                Logger.warn(

                    "WebSocket getrennt."

                );

                setTimeout(() => {

                    this.connect();

                }, this.reconnectDelay);

            };

        }

        catch(error){

            Logger.error(

                "WebSocket konnte nicht gestartet werden.",

                error

            );

        }

    },

    handle(data) {

        try {

            const message = JSON.parse(data);

            Logger.info(

                "WebSocket Nachricht",

                message

            );

            switch (message.type) {

                case "dashboard-update":

                    DashboardLive.update();

                    break;

                case "notification":

                    NotificationCenter.info(

                        message.title,

                        message.message

                    );

                    break;

                case "log":

                    Logger.info(

                        message.message

                    );

                    break;

                default:

                    console.log(

                        "WS:",

                        message

                    );

            }

        }

        catch(error){

            Logger.error(

                "Ungültige WebSocket Nachricht.",

                error

            );

        }

    },

    send(data) {

        if (

            !this.connected ||

            !this.socket

        ) return;

        this.socket.send(

            JSON.stringify(data)

        );

    },

    disconnect() {

        if (this.socket) {

            this.socket.close();

        }

    }

};

window.WebSocketManager = WebSocketManager;
