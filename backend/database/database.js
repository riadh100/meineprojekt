/**
 * =====================================================
 * AI Empire Pro V8
 * Backend - Database Manager
 * Datei: backend/database/database.js
 * =====================================================
 */

const fs = require("fs");
const path = require("path");

class Database {

    constructor(filename = "database.json") {

        this.file = path.join(__dirname, filename);

        this.data = {

            users: [],
            trades: [],
            projects: [],
            bots: [],
            conversations: [],
            achievements: [],
            missions: [],
            rewards: []

        };

        this.load();

    }

    load() {

        try {

            if (fs.existsSync(this.file)) {

                const content = fs.readFileSync(
                    this.file,
                    "utf8"
                );

                this.data = JSON.parse(content);

            } else {

                this.save();

            }

        } catch (error) {

            console.error("Database Load Error:", error);

        }

    }

    save() {

        try {

            fs.writeFileSync(
                this.file,
                JSON.stringify(this.data, null, 2)
            );

            return true;

        } catch (error) {

            console.error("Database Save Error:", error);

            return false;

        }

    }

    get(collection) {

        return this.data[collection] || [];

    }

    find(collection, id) {

        return this.get(collection).find(
            item => item.id == id
        );

    }

    insert(collection, item) {

        if (!this.data[collection]) {

            this.data[collection] = [];

        }

        this.data[collection].push(item);

        this.save();

        return item;

    }

    update(collection, id, updates) {

        const item = this.find(collection, id);

        if (!item) return null;

        Object.assign(item, updates);

        this.save();

        return item;

    }

    delete(collection, id) {

        if (!this.data[collection]) return false;

        this.data[collection] = this.data[collection].filter(

            item => item.id != id

        );

        this.save();

        return true;

    }

    clear(collection) {

        if (!this.data[collection]) return;

        this.data[collection] = [];

        this.save();

    }

}

module.exports = new Database();
