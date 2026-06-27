/**
 * =====================================================
 * AI Empire Pro V8
 * Core - Utilities
 * Datei: core/utils.js
 * =====================================================
 */

const Utils = {

    uuid() {

        return crypto.randomUUID();

    },

    timestamp() {

        return Date.now();

    },

    formatDate(date = new Date()) {

        return new Intl.DateTimeFormat("de-DE", {
            dateStyle: "medium",
            timeStyle: "medium"
        }).format(date);

    },

    clone(object) {

        return JSON.parse(JSON.stringify(object));

    },

    debounce(callback, delay = 300) {

        let timer;

        return (...args) => {

            clearTimeout(timer);

            timer = setTimeout(() => {

                callback(...args);

            }, delay);

        };

    },

    capitalize(text = "") {

        if (!text.length) return "";

        return text.charAt(0).toUpperCase() + text.slice(1);

    },

    random(min, max) {

        return Math.floor(Math.random() * (max - min + 1)) + min;

    },

    sleep(ms) {

        return new Promise(resolve => setTimeout(resolve, ms));

    },

    isEmpty(value) {

        if (value === null || value === undefined) return true;

        if (Array.isArray(value)) return value.length === 0;

        if (typeof value === "string") return value.trim() === "";

        if (typeof value === "object") return Object.keys(value).length === 0;

        return false;

    }

};

window.Utils = Utils;
