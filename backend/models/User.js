/**
 * =====================================================
 * AI Empire Pro V8
 * Backend - User Model
 * Datei: backend/models/User.js
 * =====================================================
 */

class User {

    constructor(data = {}) {

        this.id = data.id || Date.now();

        this.username = data.username || "";

        this.email = data.email || "";

        this.password = data.password || "";

        this.role = data.role || "user";

        this.avatar = data.avatar || "";

        this.twoFactor = data.twoFactor || false;

        this.createdAt = data.createdAt || new Date().toISOString();

        this.updatedAt = data.updatedAt || new Date().toISOString();

    }

    update(data = {}) {

        Object.assign(this, data);

        this.updatedAt = new Date().toISOString();

    }

    toJSON() {

        return {

            id: this.id,

            username: this.username,

            email: this.email,

            role: this.role,

            avatar: this.avatar,

            twoFactor: this.twoFactor,

            createdAt: this.createdAt,

            updatedAt: this.updatedAt

        };

    }

}

module.exports = User;
