const mongoose = require("mongoose");

const TelegramSettingsSchema = new mongoose.Schema(
    {
        botToken: {
            type: String,
            required: true,
            trim: true
        },

        botUsername: {
            type: String,
            default: "",
            trim: true
        },

        webhookUrl: {
            type: String,
            default: ""
        },

        polling: {
            type: Boolean,
            default: true
        },

        enabled: {
            type: Boolean,
            default: true
        },

        allowedChats: [
            {
                type: String,
                trim: true
            }
        ],

        adminChatId: {
            type: String,
            default: ""
        },

        defaultParseMode: {
            type: String,
            enum: [
                "Markdown",
                "MarkdownV2",
                "HTML"
            ],
            default: "HTML"
        },

        notifications: {

            trading: {
                type: Boolean,
                default: true
            },

            system: {
                type: Boolean,
                default: true
            },

            assistant: {
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
    "TelegramSettings",
    TelegramSettingsSchema
);
