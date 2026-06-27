/**
 * =====================================================
 * AI Empire Pro V8
 * Cache Utilities
 * Datei: server/utils/cache.js
 * =====================================================
 */

class Cache {

    constructor() {

        this.store = new Map();

    }

    set(key, value, ttl = 300000) {

        this.store.set(key, {

            value,

            expires: Date.now() + ttl

        });

        return value;

    }

    get(key) {

        const item = this.store.get(key);

        if (!item) {

            return null;

        }

        if (Date.now() > item.expires) {

            this.store.delete(key);

            return null;

        }

        return item.value;

    }

    has(key) {

        return this.get(key) !== null;

    }

    remove(key) {

        this.store.delete(key);

    }

    clear() {

        this.store.clear();

    }

    cleanup() {

        const now = Date.now();

        for (const [key, item] of this.store) {

            if (item.expires <= now) {

                this.store.delete(key);

            }

        }

    }

    keys() {

        return [...this.store.keys()];

    }

    values() {

        return [...this.store.values()]

            .map(item => item.value);

    }

    size() {

        return this.store.size;

    }

    stats() {

        this.cleanup();

        return {

            entries: this.store.size,

            timestamp: new Date().toISOString()

        };

    }

}

module.exports = new Cache();
