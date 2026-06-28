const mongoose = require("mongoose");

const MissionSchema = new mongoose.Schema(
    {
        title: {
            type: String,
            required: true,
            trim: true
        },

        description: {
            type: String,
            default: ""
        },

        category: {
            type: String,
            enum: [
                "daily",
                "weekly",
                "monthly",
                "special"
            ],
            default: "daily"
        },

        difficulty: {
            type: String,
            enum: [
                "easy",
                "medium",
                "hard",
                "expert"
            ],
            default: "easy"
        },

        rewardXP: {
            type: Number,
            default: 50
        },

        rewardCoins: {
            type: Number,
            default: 10
        },

        progress: {
            type: Number,
            default: 0
        },

        target: {
            type: Number,
            default: 1
        },

        completed: {
            type: Boolean,
            default: false
        },

        completedAt: {
            type: Date,
            default: null
        },

        expiresAt: {
            type: Date,
            default: null
        },

        active: {
            type: Boolean,
            default: true
        }
    },
    {
        timestamps: true
    }
);

module.exports = mongoose.model(
    "Mission",
    MissionSchema
);
