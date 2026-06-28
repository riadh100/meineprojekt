const mongoose = require("mongoose");

const RenderJobSchema = new mongoose.Schema(
    {
        project: {
            type: mongoose.Schema.Types.ObjectId,
            ref: "VideoProject",
            required: true
        },

        name: {
            type: String,
            required: true,
            trim: true
        },

        status: {
            type: String,
            enum: [
                "queued",
                "processing",
                "rendering",
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

        engine: {
            type: String,
            default: "ffmpeg"
        },

        outputFile: {
            type: String,
            default: ""
        },

        outputSize: {
            type: Number,
            default: 0
        },

        startedAt: {
            type: Date,
            default: null
        },

        finishedAt: {
            type: Date,
            default: null
        },

        duration: {
            type: Number,
            default: 0
        },

        error: {
            type: String,
            default: ""
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

module.exports = mongoose.model(
    "RenderJob",
    RenderJobSchema
);
