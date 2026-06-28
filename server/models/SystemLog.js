const mongoose = require("mongoose");

const SystemLogSchema = new mongoose.Schema(
    {
        level: {
            type: String,
            enum: [
                "info",
                "success",
                "warning",
                "error",
                "critical"
            ],
            default: "info",
            index: true
        },

        source: {
            type: String,
            default: "system",
            trim: true,
            index: true
        },

        message: {
            type: String,
            required: true,
            trim: true
        },

        details: {
            type: Object,
            default: {}
        },

        user: {
            type: mongoose.Schema.Types.ObjectId,
            ref: "User",
            default: null
        },

        ip: {
            type: String,
            default: ""
        },

        userAgent: {
            type: String,
            default: ""
        },

        resolved: {
            type: Boolean,
            default: false
        },

        resolvedAt: {
            type: Date,
            default: null
        }

    },
    {
        timestamps: true
    }
);

SystemLogSchema.index({
    createdAt: -1
});

SystemLogSchema.index({
    level: 1,
    createdAt: -1
});

module.exports = mongoose.model(
    "SystemLog",
    SystemLogSchema
);
