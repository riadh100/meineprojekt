/**
 * =====================================================
 * AI Empire Pro V8
 * Module Loader
 * Datei: assets/js/module-loader.js
 * =====================================================
 */

const ModuleLoader = {

    modules: [

        "Dashboard",
        "Assistant",
        "Trading",
        "Telegram",
        "Video",
        "Game",
        "Tools",
        "Setup"

    ],

    loaded: {},

    init() {

        Logger.info("Module Loader gestartet.");

        this.modules.forEach(module => {

            this.load(module);

        });

        this.report();

    },

    load(name) {

        try {

            const object = window[name];

            if (

                object &&

                typeof object.init === "function"

            ) {

                object.init();

                this.loaded[name] = true;

                Logger.success(

                    `${name} geladen.`

                );

            }

            else {

                this.loaded[name] = false;

                Logger.warn(

                    `${name} nicht gefunden.`

                );

            }

        }

        catch(error){

            this.loaded[name] = false;

            Logger.error(

                `${name} Fehler`,

                error

            );

        }

    },

    reload(name) {

        if (!window[name]) return;

        if (

            typeof window[name].init === "function"

        ) {

            window[name].init();

            Logger.info(

                `${name} neu geladen.`

            );

        }

    },

    report() {

        const total = this.modules.length;

        const loaded = Object.values(

            this.loaded

        ).filter(Boolean).length;

        Logger.info(

            `Module: ${loaded}/${total} geladen.`

        );

    },

    status() {

        return {

            total: this.modules.length,

            loaded: this.loaded

        };

    }

};

window.ModuleLoader = ModuleLoader;
