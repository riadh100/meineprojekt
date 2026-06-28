const mongoose = require("mongoose");

const PlayerSchema = new mongoose.Schema(
    {
        username: {
            type: String,
            required: true,
            unique: true,
            trim: true
        },

        level: {
            type: Number,
            default: 1
        },

        xp: {
            type: Number,
            default: 0
        },

        nextLevelXP: {
            type: Number,
            default: 100
        },

        coins: {
            type: Number,
            default: 0
        },

        energy: {
            type: Number,
            default: 100
        },

        health: {
            type: Number,
            default: 100
        },

        rank: {
            type: String,
            default: "Beginner"
        },

        achievements: [
            {
                type: mongoose.Schema.Types.ObjectId,
                ref: "Achievement"
            }
        ],

        inventory: [
            {
                type: String
            }
        ],

        statistics: {

            missionsCompleted: {
                type: Number,
                default: 0
            },

            tradesCompleted: {
                type: Number,
                default: 0
            },

            loginCount: {
                type: Number,
                default: 0
            }

        }

    },
    {
        timestamps: true
    }
);

module.exports = mongoose.model(
    "Player",
    PlayerSchema
);
