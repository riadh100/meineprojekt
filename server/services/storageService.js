/**
 * =====================================================
 * AI Empire Pro V8
 * Storage Service
 * Datei: server/services/storageService.js
 * =====================================================
 */

const fs = require("fs");
const path = require("path");

class StorageService {

    constructor() {

        this.basePath = path.join(

            process.cwd(),

            "storage"

        );

        if (!fs.existsSync(this.basePath)) {

            fs.mkdirSync(

                this.basePath,

                {

                    recursive: true

                }

            );

        }

    }

    resolve(file) {

        return path.join(

            this.basePath,

            file

        );

    }

    exists(file) {

        return fs.existsSync(

            this.resolve(file)

        );

    }

    read(file) {

        try {

            return fs.readFileSync(

                this.resolve(file),

                "utf8"

            );

        }

        catch (error) {

            console.error(error);

            return null;

        }

    }

    readJSON(file) {

        try {

            return JSON.parse(

                this.read(file)

            );

        }

        catch {

            return null;

        }

    }

    write(file, content) {

        try {

            fs.writeFileSync(

                this.resolve(file),

                content

            );

            return true;

        }

        catch (error) {

            console.error(error);

            return false;

        }

    }

    writeJSON(file, data) {

        return this.write(

            file,

            JSON.stringify(

                data,

                null,

                2

            )

        );

    }

    append(file, content) {

        try {

            fs.appendFileSync(

                this.resolve(file),

                content

            );

            return true;

        }

        catch (error) {

            console.error(error);

            return false;

        }

    }

    remove(file) {

        try {

            fs.unlinkSync(

                this.resolve(file)

            );

            return true;

        }

        catch {

            return false;

        }

    }

    list(directory = "") {

        try {

            const folder = path.join(

                this.basePath,

                directory

            );

            return fs.readdirSync(folder);

        }

        catch {

            return [];

        }

    }

    info(file) {

        try {

            const stat = fs.statSync(

                this.resolve(file)

            );

            return {

                size: stat.size,

                created: stat.birthtime,

                modified: stat.mtime,

                isDirectory: stat.isDirectory()

            };

        }

        catch {

            return null;

        }

    }

}

module.exports = new StorageService();
