/**
 * =====================================================
 * AI Empire Pro V8
 * Core - Global State Manager
 * Datei: core/state.js
 * =====================================================
 */

const DEFAULT_STATE = {
    user: {
        loggedIn: false,
        username: "",
        role: "user"
    },

    dashboard: {
        kpis: {},
        activity: [],
        missions: []
    },

    assistant: {
        conversations: [],
        currentChat: null,
        promptLibrary: []
    },

    trading: {
        portfolio: [],
        signals: [],
        history: []
    },

    telegram: {
        connected: false,
        bots: [],
        broadcasts: []
    },

    video: {
        projects: [],
        renderQueue: [],
        exports: []
    },

    game: {
        level: 1,
        xp: 0,
        achievements: [],
        dailyMissions: [],
        rewards: []
    },

    tools: {
        logs: [],
        apiKeys: {},
        debug: {}
    },

    settings: {
        theme: "dark",
        language: "de",
        notifications: true
    }
};

/**
 * Erstellt eine unabhängige Kopie des Standardzustands.
 */
function createState() {
    return JSON.parse(JSON.stringify(DEFAULT_STATE));
}

/**
 * Globaler Zustand der Anwendung.
 */
let AppState = createState();

/**
 * State Manager
 */
const StateManager = {

    /**
     * Gesamten State zurückgeben
     */
    getState() {
        return AppState;
    },

    /**
     * Wert lesen
     * Beispiel:
     * StateManager.get("user.username")
     */
    get(path) {
        return path
            .split(".")
            .reduce((obj, key) => obj?.[key], AppState);
    },

    /**
     * Wert setzen
     * Beispiel:
     * StateManager.set("user.username", "Max")
     */
    set(path, value) {

        const keys = path.split(".");
        const lastKey = keys.pop();

        const target = keys.reduce((obj, key) => {

            if (!(key in obj)) {
                obj[key] = {};
            }

            return obj[key];

        }, AppState);

        target[lastKey] = value;
    },

    /**
     * Element zu Array hinzufügen
     */
    push(path, value) {

        const array = this.get(path);

        if (Array.isArray(array)) {
            array.push(value);
        } else {
            console.warn(path + " ist kein Array.");
        }

    },

    /**
     * Element aus Array entfernen
     */
    remove(path, index) {

        const array = this.get(path);

        if (Array.isArray(array)) {
            array.splice(index, 1);
        }

    },

    /**
     * Gesamten State zurücksetzen
     */
    reset() {

        AppState = createState();

        console.log("State wurde zurückgesetzt.");

    }

};

/**
 * Optional:
 * Im Browser global verfügbar machen.
 */
window.AppState = AppState;
window.StateManager = StateManager;
