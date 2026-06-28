const mongoose = require("mongoose");

const BackupSchema = new mongoose.Schema(
    {
        filename: {
            type: String,
            required: true,
            trim: true
        },

        path: {
            type: String,
            required: true
        },

        size: {
            type: Number,
            default: 0
        },

        type: {
            type: String,
            enum: [
                "manual",
                "automatic",
                "scheduled"
            ],
            default: "manual"
        },

        version: {
            type: String,
            default: "8.0.0"
        },

        status: {
            type: String,
            enum: [
                "creating",
                "completed",
                "failed",
                "restored"
            ],
            default: "creating"
        },

        checksum: {
            type: String,
            default: ""
        },

        createdBy: {
            type: mongoose.Schema.Types.ObjectId,
            ref: "User",
            default: null
        },

        restoredAt: {
            type: Date,
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

BackupSchema.index({
    createdAt: -1
});

BackupSchema.index({
    status: 1,
    createdAt: -1
});

module.exports = mongoose.model(
    "Backup",
    BackupSchema
);
