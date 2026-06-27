/**
 * =====================================================
 * AI Empire Pro V8
 * Tools Controller
 * Datei: server/controllers/toolsController.js
 * =====================================================
 */

const os = require("os");
const fs = require("fs");
const path = require("path");

class ToolsController {

    async dashboard(req, res) {

        try {

            return res.json({

                success: true,

                system: {

                    platform: os.platform(),

                    release: os.release(),

                    hostname: os.hostname(),

                    uptime: os.uptime(),

                    cpus: os.cpus().length,

                    memory: {

                        total: os.totalmem(),

                        free: os.freemem()

                    }

                }

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Systeminformationen konnten nicht geladen werden."

            });

        }

    }

    async logs(req, res) {

        try {

            const logfile = path.join(

                process.cwd(),

                "logs",

                "system.log"

            );

            if (!fs.existsSync(logfile)) {

                return res.json({

                    success: true,

                    logs: []

                });

            }

            const data = fs

                .readFileSync(logfile, "utf8")

                .split("\n")

                .filter(Boolean)

                .slice(-500);

            return res.json({

                success: true,

                logs: data

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Logs konnten nicht geladen werden."

            });

        }

    }

    async clearLogs(req, res) {

        try {

            const logfile = path.join(

                process.cwd(),

                "logs",

                "system.log"

            );

            fs.writeFileSync(logfile, "");

            return res.json({

                success: true,

                message: "Logs gelöscht."

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Logs konnten nicht gelöscht werden."

            });

        }

    }

    async health(req, res) {

        return res.json({

            success: true,

            status: "online",

            timestamp: new Date(),

            node: process.version,

            memory: process.memoryUsage(),

            uptime: process.uptime()

        });

    }

    async environment(req, res) {

        return res.json({

            success: true,

            environment: {

                node: process.version,

                platform: process.platform,

                arch: process.arch,

                pid: process.pid,

                cwd: process.cwd(),

                timezone: Intl.DateTimeFormat().resolvedOptions().timeZone

            }

        });

    }

}

module.exports = new ToolsController();
