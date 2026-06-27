/**
 * =====================================================
 * AI Empire Pro V8
 * Game Module
 * Datei: modules/game/game.js
 * =====================================================
 */

const Game = {

    initialized: false,

    data: {

        level: 1,

        xp: 0,

        achievements: [],

        dailyMissions: [],

        rewards: []

    },

    init() {

        if (this.initialized) return;

        this.load();

        this.initialized = true;

        console.log("✔ Game Modul gestartet.");

    },

    load() {

        const saved = StateManager.get("game");

        if (saved) {

            this.data = {

                ...this.data,

                ...saved

            };

        }

    },

    save() {

        StateManager.set("game", this.data);

        StorageManager.save();

    },

    addXP(amount) {

        this.data.xp += Number(amount);

        while (this.data.xp >= 1000) {

            this.data.xp -= 1000;

            this.data.level++;

        }

        this.save();

    },

    addAchievement(achievement) {

        achievement.id = Utils.uuid();

        achievement.created = Utils.formatDate();

        this.data.achievements.push(achievement);

        this.save();

    },

    addReward(reward) {

        reward.id = Utils.uuid();

        reward.created = Utils.formatDate();

        this.data.rewards.push(reward);

        this.save();

    },

    getLevel() {

        return this.data.level;

    },

    getXP() {

        return this.data.xp;

    },

    reset() {

        this.data = {

            level: 1,

            xp: 0,

            achievements: [],

            dailyMissions: [],

            rewards: []

        };

        this.save();

    }

};

window.Game = Game;
