const mongoose = require("mongoose");

const VideoProjectSchema = new mongoose.Schema(
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

        status: {
            type: String,
            enum: [
                "draft",
                "editing",
                "rendering",
                "completed",
                "archived"
            ],
            default: "draft"
        },

        template: {
            type: String,
            default: ""
        },

        resolution: {
            type: String,
            default: "1920x1080"
        },

        fps: {
            type: Number,
            default: 30
        },

        duration: {
            type: Number,
            default: 0
        },

        thumbnail: {
            type: String,
            default: ""
        },

        outputFile: {
            type: String,
            default: ""
        },

        createdBy: {
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

module.exports = mongoose.model(
    "VideoProject",
    VideoProjectSchema
);
