const mongoose = require("mongoose");

const NotificationSchema = new mongoose.Schema(
    {
        title: {
            type: String,
            required: true,
            trim: true
        },

        message: {
            type: String,
            required: true,
            trim: true
        },

        type: {
            type: String,
            enum: [
                "info",
                "success",
                "warning",
                "error"
            ],
            default: "info"
        },

        read: {
            type: Boolean,
            default: false
        },

        user: {
            type: mongoose.Schema.Types.ObjectId,
            ref: "User",
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

NotificationSchema.index({
    user: 1,
    read: 1,
    createdAt: -1
});

module.exports = mongoose.model(
    "Notification",
    NotificationSchema
);
