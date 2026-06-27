/**
 * =====================================================
 * AI Empire Pro V8
 * Game - Rewards System
 * Datei: modules/game/rewards.js
 * =====================================================
 */

const Rewards = {

    rewards: [],

    init() {

        this.load();

        console.log("✔ Rewards System gestartet.");

    },

    add(title, description, cost = 0) {

        const reward = {

            id: Utils.uuid(),

            title: title,

            description: description,

            cost: Number(cost),

            claimed: false,

            created: Utils.formatDate(),

            claimedAt: null

        };

        this.rewards.push(reward);

        this.save();

        return reward;

    },

    claim(id) {

        const reward = this.get(id);

        if (!reward) return false;

        if (reward.claimed) return true;

        reward.claimed = true;

        reward.claimedAt = Utils.formatDate();

        this.save();

        return true;

    },

    remove(id) {

        this.rewards = this.rewards.filter(
            reward => reward.id !== id
        );

        this.save();

    },

    get(id) {

        return this.rewards.find(
            reward => reward.id === id
        );

    },

    getAll() {

        return this.rewards;

    },

    getClaimed() {

        return this.rewards.filter(
            reward => reward.claimed
        );

    },

    getAvailable() {

        return this.rewards.filter(
            reward => !reward.claimed
        );

    },

    clear() {

        this.rewards = [];

        this.save();

    },

    save() {

        StateManager.set(
            "game.rewards",
            this.rewards
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "game.rewards"
        );

        if (Array.isArray(data)) {

            this.rewards = data;

        }

    }

};

window.Rewards = Rewards;
