/**
 * =====================================================
 * AI Empire Pro V8
 * Backup Service
 * Datei: server/services/backupService.js
 * =====================================================
 */

const fs = require("fs");
const path = require("path");

class BackupService {

    constructor() {

        this.backupDir = path.join(

            process.cwd(),

            "backups"

        );

        if (!fs.existsSync(this.backupDir)) {

            fs.mkdirSync(

                this.backupDir,

                {

                    recursive: true

                }

            );

        }

    }

    create(data = {}) {

        try {

            const filename =

                `backup-${Date.now()}.json`;

            const filepath = path.join(

                this.backupDir,

                filename

            );

            const backup = {

                application: "AI Empire Pro",

                version:

                    process.env.APP_VERSION ||

                    "8.0.0",

                createdAt:

                    new Date().toISOString(),

                data

            };

            fs.writeFileSync(

                filepath,

                JSON.stringify(

                    backup,

                    null,

                    2

                )

            );

            return {

                success: true,

                filename,

                filepath

            };

        }

        catch (error) {

            console.error(error);

            return {

                success: false,

                error: error.message

            };

        }

    }

    restore(filename) {

        try {

            const filepath = path.join(

                this.backupDir,

                filename

            );

            if (!fs.existsSync(filepath)) {

                throw new Error(

                    "Backup nicht gefunden."

                );

            }

            const data = JSON.parse(

                fs.readFileSync(

                    filepath,

                    "utf8"

                )

            );

            return {

                success: true,

                backup: data

            };

        }

        catch (error) {

            console.error(error);

            return {

                success: false,

                error: error.message

            };

        }

    }

    list() {

        const files = fs

            .readdirSync(this.backupDir)

            .filter(file =>

                file.endsWith(".json")

            )

            .map(file => {

                const stat = fs.statSync(

                    path.join(

                        this.backupDir,

                        file

                    )

                );

                return {

                    filename: file,

                    size: stat.size,

                    createdAt: stat.birthtime

                };

            })

            .sort(

                (a, b) =>

                    b.createdAt - a.createdAt

            );

        return {

            success: true,

            files

        };

    }

    remove(filename) {

        try {

            fs.unlinkSync(

                path.join(

                    this.backupDir,

                    filename

                )

            );

            return {

                success: true

            };

        }

        catch (error) {

            return {

                success: false,

                error: error.message

            };

        }

    }

}

module.exports = new BackupService();
