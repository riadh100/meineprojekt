const mongoose = require("mongoose");

const AchievementSchema = new mongoose.Schema(
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

        icon: {
            type: String,
            default: "🏆"
        },

        category: {
            type: String,
            enum: [
                "general",
                "trading",
                "assistant",
                "video",
                "telegram",
                "system"
            ],
            default: "general"
        },

        points: {
            type: Number,
            default: 10
        },

        unlocked: {
            type: Boolean,
            default: false
        },

        unlockedAt: {
            type: Date,
            default: null
        },

        hidden: {
            type: Boolean,
            default: false
        },

        progress: {
            type: Number,
            default: 0
        },

        target: {
            type: Number,
            default: 100
        }
    },
    {
        timestamps: true
    }
);

module.exports = mongoose.model(
    "Achievement",
    AchievementSchema
);
