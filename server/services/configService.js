/**
 * =====================================================
 * AI Empire Pro V8
 * Configuration Service
 * Datei: server/services/configService.js
 * =====================================================
 */

const fs = require("fs");
const path = require("path");

class ConfigService {

    constructor() {

        this.configPath = path.join(

            process.cwd(),

            "config",

            "settings.json"

        );

        this.defaults = {

            app: {

                name: "AI Empire Pro",

                version: "8.0.0",

                language: "de"

            },

            server: {

                port: 3000,

                host: "0.0.0.0"

            },

            security: {

                jwtExpires: "12h",

                rateLimit: 300

            },

            dashboard: {

                refreshInterval: 10000

            },

            trading: {

                defaultPair: "BTCUSDT",

                autoRefresh: true

            }

        };

        this.config = {};

    }

    init() {

        if (!fs.existsSync(this.configPath)) {

            this.config = structuredClone(

                this.defaults

            );

            this.save();

        }

        else {

            this.load();

        }

    }

    load() {

        try {

            this.config = JSON.parse(

                fs.readFileSync(

                    this.configPath,

                    "utf8"

                )

            );

        }

        catch {

            this.config = structuredClone(

                this.defaults

            );

        }

    }

    save() {

        fs.mkdirSync(

            path.dirname(this.configPath),

            {

                recursive: true

            }

        );

        fs.writeFileSync(

            this.configPath,

            JSON.stringify(

                this.config,

                null,

                2

            )

        );

    }

    get(section, key = null) {

        if (!this.config[section]) {

            return null;

        }

        return key === null

            ? this.config[section]

            : this.config[section][key];

    }

    set(section, key, value) {

        if (!this.config[section]) {

            this.config[section] = {};

        }

        this.config[section][key] = value;

        this.save();
    }

    export() {

        return structuredClone(this.config);

    }

    reset() {

        this.config = structuredClone(

            this.defaults

        );

        this.save();

        return this.config;

    }

}

module.exports = new ConfigService();
