const mongoose = require("mongoose");

const TaskSchema = new mongoose.Schema(
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
                "todo",
                "in_progress",
                "review",
                "completed",
                "cancelled"
            ],
            default: "todo"
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

        category: {
            type: String,
            default: "general"
        },

        progress: {
            type: Number,
            default: 0,
            min: 0,
            max: 100
        },

        dueDate: {
            type: Date,
            default: null
        },

        completedAt: {
            type: Date,
            default: null
        },

        assignedTo: {
            type: mongoose.Schema.Types.ObjectId,
            ref: "User",
            default: null
        },

        createdBy: {
            type: mongoose.Schema.Types.ObjectId,
            ref: "User",
            default: null
        },

        tags: [{
            type: String,
            trim: true
        }],

        metadata: {
            type: Object,
            default: {}
        }

    },
    {
        timestamps: true
    }
);

TaskSchema.index({
    status: 1,
    priority: 1
});

TaskSchema.index({
    dueDate: 1
});

module.exports = mongoose.model(
    "Task",
    TaskSchema
);
