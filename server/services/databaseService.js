/**
 * =====================================================
 * AI Empire Pro V8
 * Database Service
 * Datei: server/services/databaseService.js
 * =====================================================
 */

const mongoose = require("mongoose");

class DatabaseService {

    constructor() {

        this.connected = false;

    }

    async connect() {

        try {

            const uri =

                process.env.MONGODB_URI ||

                "mongodb://127.0.0.1:27017/aiempire";

            await mongoose.connect(uri, {

                autoIndex: true,

                serverSelectionTimeoutMS: 5000,

                socketTimeoutMS: 45000

            });

            this.connected = true;

            console.log("MongoDB verbunden.");

            mongoose.connection.on("error", error => {

                console.error(

                    "MongoDB Fehler:",

                    error

                );

            });

            mongoose.connection.on("disconnected", () => {

                this.connected = false;

                console.warn(

                    "MongoDB Verbindung getrennt."

                );

            });

            mongoose.connection.on("reconnected", () => {

                this.connected = true;

                console.log(

                    "MongoDB erneut verbunden."

                );

            });

            return true;

        }

        catch (error) {

            console.error(

                "MongoDB Verbindung fehlgeschlagen.",

                error

            );

            this.connected = false;

            return false;

        }

    }

    async disconnect() {

        try {

            await mongoose.disconnect();

            this.connected = false;

            console.log("MongoDB getrennt.");

        }

        catch (error) {

            console.error(error);

        }

    }

    status() {

        return {

            connected: this.connected,

            readyState: mongoose.connection.readyState,

            database: mongoose.connection.name,

            host: mongoose.connection.host,

            port: mongoose.connection.port

        };

    }

}

module.exports = new DatabaseService();
