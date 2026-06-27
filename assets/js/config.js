/**
 * =====================================================
 * AI Empire Pro V8
 * Global Configuration
 * Datei: assets/js/config.js
 * =====================================================
 */

const Config = {

    app: {

        name: "AI Empire Pro",

        version: "8.0.0",

        environment: "development"

    },

    api: {

        baseURL: "http://localhost:3000/api",

        timeout: 10000,

        retryAttempts: 3

    },

    websocket: {

        url: "ws://localhost:3000",

        reconnectDelay: 5000,

        heartbeat: 30000

    },

    ui: {

        theme: "dark",

        language: "de",

        animations: true,

        compactMode: false,

        pageSize: 20

    },

    dashboard: {

        refreshInterval: 10000,

        chartPoints: 30

    },

    trading: {

        currency: "EUR",

        autoRefresh: true,

        refreshInterval: 5000

    },

    assistant: {

        model: "gpt-5",

        maxHistory: 100,

        temperature: 0.7

    },

    notifications: {

        enabled: true,

        duration: 4000

    },

    backup: {

        autoBackup: false,

        interval: 86400000

    },

    get(section, key = null) {

        if (!this[section]) {

            return null;

        }

        return key === null

            ? this[section]

            : this[section][key];

    },

    set(section, key, value) {

        if (!this[section]) {

            this[section] = {};

        }

        this[section][key] = value;

    },

    export() {

        return structuredClone(this);

    }

};

window.Config = Config;
