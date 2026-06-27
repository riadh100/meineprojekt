/**
 * =====================================================
 * AI Empire Pro V8
 * Game - XP Engine
 * Datei: modules/game/xp-engine.js
 * =====================================================
 */

const XPEngine = {

    level: 1,

    xp: 0,

    xpPerLevel: 1000,

    init() {

        this.load();

        console.log("✔ XP Engine gestartet.");

    },

    add(amount) {

        this.xp += Number(amount);

        while (this.xp >= this.xpPerLevel) {

            this.xp -= this.xpPerLevel;

            this.level++;

        }

        this.save();

    },

    remove(amount) {

        this.xp = Math.max(0, this.xp - Number(amount));

        this.save();

    },

    setLevel(level) {

        this.level = Number(level);

        this.save();

    },

    getLevel() {

        return this.level;

    },

    getXP() {

        return this.xp;

    },

    getProgress() {

        return Math.floor(
            (this.xp / this.xpPerLevel) * 100
        );

    },

    reset() {

        this.level = 1;

        this.xp = 0;

        this.save();

    },

    save() {

        StateManager.set("game.level", this.level);

        StateManager.set("game.xp", this.xp);

        StorageManager.save();

    },

    load() {

        const level = StateManager.get("game.level");

        const xp = StateManager.get("game.xp");

        if (level !== undefined) this.level = level;

        if (xp !== undefined) this.xp = xp;

    }

};

window.XPEngine = XPEngine;
