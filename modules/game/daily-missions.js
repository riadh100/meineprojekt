/**
 * =====================================================
 * AI Empire Pro V8
 * Game - Daily Missions
 * Datei: modules/game/daily-missions.js
 * =====================================================
 */

const DailyMissions = {

    missions: [],

    init() {

        this.load();

        console.log("✔ Daily Missions gestartet.");

    },

    add(title, description, rewardXP = 100) {

        const mission = {

            id: Utils.uuid(),

            title: title,

            description: description,

            rewardXP: Number(rewardXP),

            completed: false,

            created: Utils.formatDate(),

            completedAt: null

        };

        this.missions.push(mission);

        this.save();

        return mission;

    },

    complete(id) {

        const mission = this.get(id);

        if (!mission) return false;

        if (mission.completed) return true;

        mission.completed = true;

        mission.completedAt = Utils.formatDate();

        XPEngine.add(mission.rewardXP);

        this.save();

        return true;

    },

    reset() {

        this.missions.forEach(mission => {

            mission.completed = false;

            mission.completedAt = null;

        });

        this.save();

    },

    remove(id) {

        this.missions = this.missions.filter(
            mission => mission.id !== id
        );

        this.save();

    },

    get(id) {

        return this.missions.find(
            mission => mission.id === id
        );

    },

    getAll() {

        return this.missions;

    },

    getCompleted() {

        return this.missions.filter(
            mission => mission.completed
        );

    },

    getOpen() {

        return this.missions.filter(
            mission => !mission.completed
        );

    },

    clear() {

        this.missions = [];

        this.save();

    },

    save() {

        StateManager.set(
            "game.dailyMissions",
            this.missions
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "game.dailyMissions"
        );

        if (Array.isArray(data)) {

            this.missions = data;

        }

    }

};

window.DailyMissions = DailyMissions;
