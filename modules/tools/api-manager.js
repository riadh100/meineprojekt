/**
 * =====================================================
 * AI Empire Pro V8
 * Tools - API Manager
 * Datei: modules/tools/api-manager.js
 * =====================================================
 */

const APIManager = {

    apis: [],

    init() {

        this.load();

        console.log("✔ API Manager gestartet.");

    },

    add(name, url, apiKey = "") {

        const api = {

            id: Utils.uuid(),

            name: name,

            url: url,

            apiKey: apiKey,

            active: true,

            created: Utils.formatDate(),

            lastCheck: null

        };

        this.apis.push(api);

        this.save();

        return api;

    },

    update(id, data) {

        const api = this.get(id);

        if (!api) return false;

        Object.assign(api, data);

        this.save();

        return true;

    },

    remove(id) {

        this.apis = this.apis.filter(
            api => api.id !== id
        );

        this.save();

    },

    get(id) {

        return this.apis.find(
            api => api.id === id
        );

    },

    getAll() {

        return this.apis;

    },

    async test(id) {

        const api = this.get(id);

        if (!api) return false;

        try {

            const response = await fetch(api.url);

            api.lastCheck = Utils.formatDate();

            api.online = response.ok;

            this.save();

            return response.ok;

        } catch (error) {

            api.lastCheck = Utils.formatDate();

            api.online = false;

            this.save();

            return false;

        }

    },

    clear() {

        this.apis = [];

        this.save();

    },

    save() {

        StateManager.set(
            "tools.apis",
            this.apis
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "tools.apis"
        );

        if (Array.isArray(data)) {

            this.apis = data;

        }

    }

};

window.APIManager = APIManager;
