/**
 * =====================================================
 * AI Empire Pro V8
 * Game - Achievement System
 * Datei: modules/game/achievement-system.js
 * =====================================================
 */

const AchievementSystem = {

    achievements: [],

    init() {

        this.load();

        console.log("✔ Achievement System gestartet.");

    },

    add(title, description, xp = 100) {

        const achievement = {

            id: Utils.uuid(),

            title: title,

            description: description,

            xp: Number(xp),

            unlocked: false,

            unlockedAt: null,

            created: Utils.formatDate()

        };

        this.achievements.push(achievement);

        this.save();

        return achievement;

    },

    unlock(id) {

        const achievement = this.get(id);

        if (!achievement) return false;

        if (achievement.unlocked) return true;

        achievement.unlocked = true;

        achievement.unlockedAt = Utils.formatDate();

        XPEngine.add(achievement.xp);

        this.save();

        return true;

    },

    remove(id) {

        this.achievements = this.achievements.filter(
            item => item.id !== id
        );

        this.save();

    },

    get(id) {

        return this.achievements.find(
            item => item.id === id
        );

    },

    getAll() {

        return this.achievements;

    },

    getUnlocked() {

        return this.achievements.filter(
            item => item.unlocked
        );

    },

    getLocked() {

        return this.achievements.filter(
            item => !item.unlocked
        );

    },

    clear() {

        this.achievements = [];

        this.save();

    },

    save() {

        StateManager.set(
            "game.achievements",
            this.achievements
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "game.achievements"
        );

        if (Array.isArray(data)) {

            this.achievements = data;

        }

    }

};

window.AchievementSystem = AchievementSystem;
