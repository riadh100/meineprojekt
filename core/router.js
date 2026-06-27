/**
 * =====================================================
 * AI Empire Pro V8
 * Core - Router
 * Datei: core/router.js
 * =====================================================
 */

const Router = {

    current: null,

    routes: {},

    register(name, callback) {

        this.routes[name] = callback;

    },

    navigate(name) {

        if (!this.routes[name]) {

            console.error("Route nicht gefunden:", name);

            return;

        }

        this.current = name;

        StateManager.set("app.currentRoute", name);

        this.routes[name]();

        console.log("Route:", name);

    },

    getCurrent() {

        return this.current;

    },

    exists(name) {

        return this.routes.hasOwnProperty(name);

    },

    remove(name) {

        delete this.routes[name];

    },

    list() {

        return Object.keys(this.routes);

    }

};

window.Router = Router;
