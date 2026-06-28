const mongoose = require("mongoose");

const SettingSchema = new mongoose.Schema(
    {
        key: {
            type: String,
            required: true,
            unique: true,
            trim: true,
            index: true
        },

        value: {
            type: mongoose.Schema.Types.Mixed,
            default: null
        },

        category: {
            type: String,
            default: "general",
            trim: true,
            index: true
        },

        type: {
            type: String,
            enum: [
                "string",
                "number",
                "boolean",
                "object",
                "array"
            ],
            default: "string"
        },

        description: {
            type: String,
            default: ""
        },

        editable: {
            type: Boolean,
            default: true
        },

        encrypted: {
            type: Boolean,
            default: false
        },

        updatedBy: {
            type: mongoose.Schema.Types.ObjectId,
            ref: "User",
            default: null
        }

    },
    {
        timestamps: true
    }
);

SettingSchema.index({
    category: 1,
    key: 1
});

module.exports = mongoose.model(
    "Setting",
    SettingSchema
);
