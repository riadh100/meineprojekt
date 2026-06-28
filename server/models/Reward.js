const mongoose = require("mongoose");

const RewardSchema = new mongoose.Schema(
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

        type: {
            type: String,
            enum: [
                "coins",
                "xp",
                "badge",
                "item",
                "unlock"
            ],
            default: "coins"
        },

        value: {
            type: Number,
            default: 0
        },

        icon: {
            type: String,
            default: "🎁"
        },

        rarity: {
            type: String,
            enum: [
                "common",
                "rare",
                "epic",
                "legendary"
            ],
            default: "common"
        },

        claimed: {
            type: Boolean,
            default: false
        },

        claimedAt: {
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
    "Reward",
    RewardSchema
);
