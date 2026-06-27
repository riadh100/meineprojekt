/**
 * =====================================================
 * AI Empire Pro V8
 * Dashboard Mission Engine
 * Datei: modules/dashboard/dashboard-missions.js
 * =====================================================
 */

const DashboardMissions = {

    missions: [],

    init() {

        this.load();

        console.log("Mission Engine gestartet.");

    },

    add(title, description, reward = 0) {

        const mission = {

            id: Utils.uuid(),

            title: title,

            description: description,

            reward: reward,

            completed: false,

            created: Utils.formatDate()

        };

        this.missions.push(mission);

        this.save();

    },

    complete(id) {

        const mission = this.missions.find(
            item => item.id === id
        );

        if (!mission) return;

        mission.completed = true;

        this.save();

    },

    remove(id) {

        this.missions = this.missions.filter(
            item => item.id !== id
        );

        this.save();

    },

    clear() {

        this.missions = [];

        this.save();

    },

    get(id) {

        return this.missions.find(
            item => item.id === id
        );

    },

    getAll() {

        return this.missions;

    },

    getCompleted() {

        return this.missions.filter(
            item => item.completed
        );

    },

    getOpen() {

        return this.missions.filter(
            item => !item.completed
        );

    },

    save() {

        StateManager.set(
            "dashboard.missions",
            this.missions
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "dashboard.missions"
        );

        if (Array.isArray(data)) {

            this.missions = data;

        }

    }

};

window.DashboardMissions = DashboardMissions;
