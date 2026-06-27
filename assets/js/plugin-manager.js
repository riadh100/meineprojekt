/**
 * =====================================================
 * AI Empire Pro V8
 * Plugin Manager
 * Datei: assets/js/plugin-manager.js
 * =====================================================
 */

const PluginManager = {

    plugins: [],

    init() {

        this.load();

        Logger.success("Plugin Manager gestartet.");

    },

    register(plugin) {

        if (!plugin || !plugin.name) {

            Logger.warn("Ungültiges Plugin.");

            return;

        }

        if (this.plugins.find(p => p.name === plugin.name)) {

            Logger.warn(

                `${plugin.name} bereits registriert.`

            );

            return;

        }

        this.plugins.push({

            enabled: true,

            ...plugin

        });

        if (typeof plugin.init === "function") {

            plugin.init();

        }

        Logger.success(

            `${plugin.name} registriert.`

        );

        this.save();

    },

    unregister(name) {

        this.plugins = this.plugins.filter(

            plugin => plugin.name !== name

        );

        Logger.info(

            `${name} entfernt.`

        );

        this.save();

    },

    enable(name) {

        const plugin = this.plugins.find(

            p => p.name === name

        );

        if (!plugin) return;

        plugin.enabled = true;

        Logger.success(

            `${name} aktiviert.`

        );

        this.save();

    },

    disable(name) {

        const plugin = this.plugins.find(

            p => p.name === name

        );

        if (!plugin) return;

        plugin.enabled = false;

        Logger.warn(

            `${name} deaktiviert.`

        );

        this.save();

    },

    getAll() {

        return this.plugins;

    },

    getEnabled() {

        return this.plugins.filter(

            plugin => plugin.enabled

        );

    },

    save() {

        localStorage.setItem(

            "plugins",

            JSON.stringify(this.plugins)

        );

    },

    load() {

        const data = localStorage.getItem(

            "plugins"

        );

        if (!data) return;

        try {

            this.plugins = JSON.parse(data);

        }

        catch {

            this.plugins = [];

        }

    }

};

window.PluginManager = PluginManager;
