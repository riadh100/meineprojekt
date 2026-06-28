const mongoose = require("mongoose");

const APIKeySchema = new mongoose.Schema(
    {
        name: {
            type: String,
            required: true,
            trim: true
        },

        provider: {
            type: String,
            required: true,
            enum: [
                "openai",
                "binance",
                "coingecko",
                "telegram",
                "stripe",
                "github",
                "custom"
            ]
        },

        key: {
            type: String,
            required: true
        },

        secret: {
            type: String,
            default: ""
        },

        passphrase: {
            type: String,
            default: ""
        },

        endpoint: {
            type: String,
            default: ""
        },

        enabled: {
            type: Boolean,
            default: true
        },

        testMode: {
            type: Boolean,
            default: false
        },

        lastUsedAt: {
            type: Date,
            default: null
        },

        expiresAt: {
            type: Date,
            default: null
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

APIKeySchema.index({
    provider: 1,
    enabled: 1
});

module.exports = mongoose.model(
    "APIKey",
    APIKeySchema
);
