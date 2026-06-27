/**
 * =====================================================
 * AI Empire Pro V8
 * Dashboard Activity Feed
 * Datei: modules/dashboard/dashboard-activity.js
 * =====================================================
 */

const DashboardActivity = {

    activities: [],

    init() {

        this.load();

        console.log("Activity Feed gestartet.");

    },

    add(type, message) {

        const activity = {

            id: Utils.uuid(),

            type: type,

            message: message,

            timestamp: Utils.formatDate()

        };

        this.activities.unshift(activity);

        this.save();

    },

    remove(id) {

        this.activities = this.activities.filter(
            activity => activity.id !== id
        );

        this.save();

    },

    clear() {

        this.activities = [];

        this.save();

    },

    get(id) {

        return this.activities.find(
            activity => activity.id === id
        );

    },

    getAll() {

        return this.activities;

    },

    save() {

        StateManager.set(
            "dashboard.activity",
            this.activities
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "dashboard.activity"
        );

        if (Array.isArray(data)) {

            this.activities = data;

        }

    }

};

window.DashboardActivity = DashboardActivity;
