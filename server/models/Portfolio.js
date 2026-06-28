const mongoose = require("mongoose");

const PortfolioSchema = new mongoose.Schema(
    {
        name: {
            type: String,
            default: "Hauptportfolio",
            trim: true
        },

        balance: {
            type: Number,
            default: 0
        },

        invested: {
            type: Number,
            default: 0
        },

        profit: {
            type: Number,
            default: 0
        },

        currency: {
            type: String,
            default: "EUR",
            uppercase: true
        },

        assets: [
            {
                symbol: {
                    type: String,
                    required: true,
                    uppercase: true
                },

                amount: {
                    type: Number,
                    default: 0
                },

                averagePrice: {
                    type: Number,
                    default: 0
                },

                currentPrice: {
                    type: Number,
                    default: 0
                },

                value: {
                    type: Number,
                    default: 0
                },

                profit: {
                    type: Number,
                    default: 0
                }
            }
        ]
    },
    {
        timestamps: true
    }
);

module.exports = mongoose.model(
    "Portfolio",
    PortfolioSchema
);
