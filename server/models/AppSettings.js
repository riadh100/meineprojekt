const mongoose = require("mongoose");

const AppSettingsSchema = new mongoose.Schema(
    {
        appName: {
            type: String,
            default: "AI Empire Pro",
            trim: true
        },

        version: {
            type: String,
            default: "8.0.0"
        },

        language: {
            type: String,
            default: "de"
        },

        timezone: {
            type: String,
            default: "Europe/Berlin"
        },

        theme: {
            type: String,
            enum: [
                "dark",
                "light",
                "system"
            ],
            default: "dark"
        },

        maintenanceMode: {
            type: Boolean,
            default: false
        },

        registrationEnabled: {
            type: Boolean,
            default: true
        },

        autoBackup: {
            type: Boolean,
            default: true
        },

        backupInterval: {
            type: Number,
            default: 24
        },

        api: {

            openaiModel: {
                type: String,
                default: "gpt-4.1"
            },

            refreshInterval: {
                type: Number,
                default: 10000
            }

        },

        trading: {

            defaultPair: {
                type: String,
                default: "BTCUSDT"
            },

            paperTrading: {
                type: Boolean,
                default: true
            }

        },

        notifications: {

            email: {
                type: Boolean,
                default: true
            },

            telegram: {
                type: Boolean,
                default: true
            },

            desktop: {
                type: Boolean,
                default: true
            }

        }

    },
    {
        timestamps: true
    }
);

module.exports = mongoose.model(
    "AppSettings",
    AppSettingsSchema
);
