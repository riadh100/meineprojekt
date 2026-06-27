/**
 * =====================================================
 * AI Empire Pro V8
 * Setup Controller
 * Datei: server/controllers/setupController.js
 * =====================================================
 */

const fs = require("fs");
const path = require("path");

const User = require("../models/User");

class SetupController {

    async dashboard(req, res) {

        try {

            const users = await User.countDocuments();

            return res.json({

                success: true,

                version: process.env.APP_VERSION || "8.0.0",

                environment: process.env.NODE_ENV || "development",

                users,

                setupComplete: true

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Setup konnte nicht geladen werden."

            });

        }

    }

    async settings(req, res) {

        try {

            return res.json({

                success: true,

                settings: {

                    appName: process.env.APP_NAME || "AI Empire Pro",

                    language: process.env.APP_LANG || "de",

                    timezone: process.env.TZ || "Europe/Berlin",

                    version: process.env.APP_VERSION || "8.0.0",

                    environment: process.env.NODE_ENV || "development"

                }

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Einstellungen konnten nicht geladen werden."

            });

        }

    }

    async saveSettings(req, res) {

        try {

            const settings = req.body;

            const file = path.join(

                process.cwd(),

                "config",

                "settings.json"

            );

            fs.writeFileSync(

                file,

                JSON.stringify(settings, null, 2)

            );

            return res.json({

                success: true,

                message: "Einstellungen gespeichert."

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Speichern fehlgeschlagen."

            });

        }

    }

    async backup(req, res) {

        try {

            const backupDir = path.join(

                process.cwd(),

                "backups"

            );

            if (!fs.existsSync(backupDir)) {

                fs.mkdirSync(

                    backupDir,

                    {

                        recursive: true

                    }

                );

            }

            const filename = `backup-${Date.now()}.json`;

            const filepath = path.join(

                backupDir,

                filename

            );

            fs.writeFileSync(

                filepath,

                JSON.stringify({

                    created: new Date(),

                    version: process.env.APP_VERSION || "8.0.0"

                }, null, 2)

            );

            return res.json({

                success: true,

                file: filename

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Backup konnte nicht erstellt werden."

            });

        }

    }

    async restore(req, res) {

        return res.json({

            success: true,

            message: "Restore-Funktion vorbereitet."

        });

    }

}

module.exports = new SetupController();
