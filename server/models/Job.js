const mongoose = require("mongoose");

const JobSchema = new mongoose.Schema(
    {
        name: {
            type: String,
            required: true,
            trim: true
        },

        type: {
            type: String,
            enum: [
                "assistant",
                "trading",
                "video",
                "telegram",
                "backup",
                "system",
                "custom"
            ],
            default: "custom"
        },

        status: {
            type: String,
            enum: [
                "queued",
                "running",
                "completed",
                "failed",
                "cancelled"
            ],
            default: "queued"
        },

        progress: {
            type: Number,
            default: 0,
            min: 0,
            max: 100
        },

        priority: {
            type: String,
            enum: [
                "low",
                "normal",
                "high",
                "critical"
            ],
            default: "normal"
        },

        payload: {
            type: Object,
            default: {}
        },

        result: {
            type: Object,
            default: {}
        },

        error: {
            type: String,
            default: ""
        },

        startedAt: {
            type: Date,
            default: null
        },

        finishedAt: {
            type: Date,
            default: null
        },

        createdBy: {
            type: mongoose.Schema.Types.ObjectId,
            ref: "User",
            default: null
        }

    },
    {
        timestamps: true
    }
);

JobSchema.index({
    status: 1,
    priority: 1
});

JobSchema.index({
    createdAt: -1
});

module.exports = mongoose.model(
    "Job",
    JobSchema
);
