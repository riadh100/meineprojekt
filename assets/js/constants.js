/**
 * =====================================================
 * AI Empire Pro V8
 * Global Constants
 * Datei: assets/js/constants.js
 * =====================================================
 */

const Constants = Object.freeze({

    APP_NAME: "AI Empire Pro",

    VERSION: "8.0.0",

    STORAGE_PREFIX: "aiempire-",

    DEFAULT_LANGUAGE: "de",

    DEFAULT_THEME: "dark",

    DEFAULT_CURRENCY: "EUR",

    API_TIMEOUT: 10000,

    AUTO_SAVE_INTERVAL: 30000,

    DASHBOARD_REFRESH: 10000,

    TRADING_REFRESH: 5000,

    NOTIFICATION_DURATION: 4000,

    MAX_LOG_ENTRIES: 1000,

    MAX_CHAT_HISTORY: 100,

    MAX_CACHE_ITEMS: 500,

    STATUS: {

        ACTIVE: "active",

        INACTIVE: "inactive",

        ONLINE: "online",

        OFFLINE: "offline",

        RUNNING: "running",

        STOPPED: "stopped",

        SUCCESS: "success",

        WARNING: "warning",

        ERROR: "error"

    },

    PRIORITY: {

        LOW: "low",

        NORMAL: "normal",

        HIGH: "high",

        CRITICAL: "critical"

    },

    USER_ROLE: {

        ADMIN: "admin",

        USER: "user",

        GUEST: "guest"

    },

    MODULES: [

        "dashboard",

        "assistant",

        "trading",

        "telegram",

        "video",

        "game",

        "tools",

        "setup"

    ]

});

window.Constants = Constants;
