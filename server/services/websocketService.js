/**
 * =====================================================
 * AI Empire Pro V8
 * WebSocket Service
 * Datei: server/services/websocketService.js
 * =====================================================
 */

const { Server } = require("socket.io");

class WebSocketService {

    constructor() {

        this.io = null;

        this.clients = new Map();

    }

    init(server) {

        this.io = new Server(server, {

            cors: {

                origin: process.env.CORS_ORIGIN || "*",

                methods: [

                    "GET",

                    "POST"

                ]

            }

        });

        this.io.on("connection", socket => {

            this.clients.set(

                socket.id,

                socket

            );

            console.log(

                `Client verbunden: ${socket.id}`

            );

            socket.emit("connected", {

                success: true,

                id: socket.id,

                timestamp: new Date()

            });

            socket.on("disconnect", () => {

                this.clients.delete(

                    socket.id

                );

                console.log(

                    `Client getrennt: ${socket.id}`

                );

            });

            socket.on("ping", () => {

                socket.emit("pong", {

                    timestamp: Date.now()

                });

            });

        });

        console.log("WebSocket Service gestartet.");

    }

    emit(event, data = {}) {

        if (!this.io) return;

        this.io.emit(event, data);

    }

    emitTo(socketId, event, data = {}) {

        const socket = this.clients.get(socketId);

        if (!socket) return;

        socket.emit(event, data);

    }

    broadcastNotification(title, message) {

        this.emit("notification", {

            title,

            message,

            createdAt: new Date()

        });

    }

    dashboardUpdate(data) {

        this.emit(

            "dashboard-update",

            data

        );

    }

    tradingUpdate(data) {

        this.emit(

            "trading-update",

            data

        );

    }

    assistantMessage(data) {

        this.emit(

            "assistant-message",

            data

        );

    }

    onlineClients() {

        return this.clients.size;

    }

}

module.exports = new WebSocketService();
