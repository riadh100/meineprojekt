const mongoose = require("mongoose");

const TelegramMessageSchema = new mongoose.Schema(
    {
        chatId: {
            type: String,
            required: true,
            index: true
        },

        messageId: {
            type: Number,
            default: null
        },

        username: {
            type: String,
            default: ""
        },

        firstName: {
            type: String,
            default: ""
        },

        lastName: {
            type: String,
            default: ""
        },

        text: {
            type: String,
            default: ""
        },

        type: {
            type: String,
            enum: [
                "text",
                "photo",
                "video",
                "document",
                "audio",
                "voice",
                "sticker",
                "location",
                "contact",
                "callback"
            ],
            default: "text"
        },

        direction: {
            type: String,
            enum: [
                "incoming",
                "outgoing"
            ],
            default: "incoming"
        },

        delivered: {
            type: Boolean,
            default: true
        },

        metadata: {
            type: Object,
            default: {}
        }

    },
    {
        timestamps: true
    }
);

TelegramMessageSchema.index({
    chatId: 1,
    createdAt: -1
});

module.exports = mongoose.model(
    "TelegramMessage",
    TelegramMessageSchema
);
