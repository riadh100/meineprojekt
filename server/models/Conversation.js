const mongoose = require("mongoose");

const MessageSchema = new mongoose.Schema(
    {
        role: {
            type: String,
            enum: ["system", "user", "assistant"],
            required: true
        },

        content: {
            type: String,
            required: true,
            trim: true
        },

        tokens: {
            type: Number,
            default: 0
        },

        model: {
            type: String,
            default: ""
        },

        createdAt: {
            type: Date,
            default: Date.now
        }
    },
    {
        _id: false
    }
);

const ConversationSchema = new mongoose.Schema(
    {
        title: {
            type: String,
            default: "Neue Unterhaltung",
            trim: true
        },

        user: {
            type: mongoose.Schema.Types.ObjectId,
            ref: "User",
            default: null
        },

        messages: [MessageSchema],

        archived: {
            type: Boolean,
            default: false
        }
    },
    {
        timestamps: true
    }
);

module.exports = mongoose.model(
    "Conversation",
    ConversationSchema
);
