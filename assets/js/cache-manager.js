/**
 * =====================================================
 * AI Empire Pro V8
 * Cache Manager
 * Datei: assets/js/cache-manager.js
 * =====================================================
 */

const CacheManager = {

    prefix: "aiempire-cache-",

    defaultTTL: 300000,

    init() {

        this.cleanup();

        Logger.success("Cache Manager gestartet.");

    },

    set(key, value, ttl = this.defaultTTL) {

        const item = {

            value,

            expires: Date.now() + ttl

        };

        localStorage.setItem(

            this.prefix + key,

            JSON.stringify(item)

        );

    },

    get(key) {

        const data = localStorage.getItem(

            this.prefix + key

        );

        if (!data) return null;

        try {

            const item = JSON.parse(data);

            if (Date.now() > item.expires) {

                this.remove(key);

                return null;

            }

            return item.value;

        }

        catch {

            this.remove(key);

            return null;

        }

    },

    has(key) {

        return this.get(key) !== null;

    },

    remove(key) {

        localStorage.removeItem(

            this.prefix + key

        );

    },

    clear() {

        Object.keys(localStorage).forEach(key => {

            if (key.startsWith(this.prefix)) {

                localStorage.removeItem(key);

            }

        });

    },

    cleanup() {

        Object.keys(localStorage).forEach(key => {

            if (!key.startsWith(this.prefix)) return;

            try {

                const item = JSON.parse(

                    localStorage.getItem(key)

                );

                if (Date.now() > item.expires) {

                    localStorage.removeItem(key);

                }

            }

            catch {

                localStorage.removeItem(key);

            }

        });

    },

    stats() {

        const keys = Object.keys(localStorage)

            .filter(key =>

                key.startsWith(this.prefix)

            );

        return {

            items: keys.length,

            keys

        };

    }

};

window.CacheManager = CacheManager;
