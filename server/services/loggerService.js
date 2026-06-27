/**
 * =====================================================
 * AI Empire Pro V8
 * Logger Service
 * Datei: server/services/loggerService.js
 * =====================================================
 */

const fs = require("fs");
const path = require("path");

class LoggerService {

    constructor() {

        this.logDirectory = path.join(

            process.cwd(),

            "logs"

        );

        if (!fs.existsSync(this.logDirectory)) {

            fs.mkdirSync(

                this.logDirectory,

                {

                    recursive: true

                }

            );

        }

    }

    log(level, message, data = null) {

        const entry = {

            timestamp: new Date().toISOString(),

            level,

            message,

            data

        };

        const file = path.join(

            this.logDirectory,

            `${level.toLowerCase()}.log`

        );

        try {

            fs.appendFileSync(

                file,

                JSON.stringify(entry) + "\n"

            );

        }

        catch (error) {

            console.error(error);

        }

        console.log(

            `[${level}]`,

            message

        );

    }

    info(message, data = null) {

        this.log(

            "INFO",

            message,

            data

        );

    }

    success(message, data = null) {

        this.log(

            "SUCCESS",

            message,

            data

        );

    }

    warn(message, data = null) {

        this.log(

            "WARN",

            message,

            data

        );

    }

    error(message, data = null) {

        this.log(

            "ERROR",

            message,

            data

        );

    }

    read(level = "info") {

        try {

            const file = path.join(

                this.logDirectory,

                `${level.toLowerCase()}.log`

            );

            if (!fs.existsSync(file)) {

                return [];

            }

            return fs.readFileSync(

                file,

                "utf8"

            )

            .split("\n")

            .filter(Boolean)

            .map(line => JSON.parse(line));

        }

        catch {

            return [];

        }

    }

    clear(level = null) {

        try {

            if (level) {

                const file = path.join(

                    this.logDirectory,

                    `${level.toLowerCase()}.log`

                );

                if (fs.existsSync(file)) {

                    fs.unlinkSync(file);

                }

                return true;

            }

            fs.readdirSync(

                this.logDirectory

            ).forEach(file => {

                fs.unlinkSync(

                    path.join(

                        this.logDirectory,

                        file

                    )

                );

            });

            return true;

        }

        catch {

            return false;

        }

    }

}

module.exports = new LoggerService();
