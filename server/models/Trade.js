const mongoose = require("mongoose");

const TradeSchema = new mongoose.Schema(
    {
        symbol: {
            type: String,
            required: true,
            uppercase: true,
            trim: true
        },

        type: {
            type: String,
            enum: ["BUY", "SELL"],
            required: true
        },

        amount: {
            type: Number,
            required: true,
            default: 0
        },

        entryPrice: {
            type: Number,
            required: true,
            default: 0
        },

        exitPrice: {
            type: Number,
            default: 0
        },

        profit: {
            type: Number,
            default: 0
        },

        status: {
            type: String,
            enum: ["OPEN", "CLOSED", "CANCELLED"],
            default: "OPEN"
        },

        notes: {
            type: String,
            default: ""
        },

        user: {
            type: mongoose.Schema.Types.ObjectId,
            ref: "User",
            default: null
        }
    },
    {
        timestamps: true
    }
);

module.exports = mongoose.model("Trade", TradeSchema);
