/**
 * =====================================================
 * AI Empire Pro V8
 * Backend - Database Index
 * Datei: backend/database/index.js
 * =====================================================
 */

const database = require("./database");

module.exports = {

    users() {

        return database.get("users");

    },

    trades() {

        return database.get("trades");

    },

    projects() {

        return database.get("projects");

    },

    bots() {

        return database.get("bots");

    },

    conversations() {

        return database.get("conversations");

    },

    achievements() {

        return database.get("achievements");

    },

    missions() {

        return database.get("missions");

    },

    rewards() {

        return database.get("rewards");

    },

    insert(collection, data) {

        return database.insert(collection, data);

    },

    update(collection, id, data) {

        return database.update(collection, id, data);

    },

    delete(collection, id) {

        return database.delete(collection, id);

    },

    find(collection, id) {

        return database.find(collection, id);

    },

    clear(collection) {

        return database.clear(collection);

    }

};
