/**
 * =====================================================
 * AI Empire Pro V8
 * File Utilities
 * Datei: server/utils/file.js
 * =====================================================
 */

const fs = require("fs");
const path = require("path");

class FileUtil {

    static exists(file) {

        return fs.existsSync(file);

    }

    static read(file, encoding = "utf8") {

        try {

            return fs.readFileSync(

                file,

                encoding

            );

        }

        catch {

            return null;

        }

    }

    static write(file, content) {

        try {

            fs.mkdirSync(

                path.dirname(file),

                {

                    recursive: true

                }

            );

            fs.writeFileSync(

                file,

                content

            );

            return true;

        }

        catch {

            return false;

        }

    }

    static append(file, content) {

        try {

            fs.mkdirSync(

                path.dirname(file),

                {

                    recursive: true

                }

            );

            fs.appendFileSync(

                file,

                content

            );

            return true;

        }

        catch {

            return false;

        }

    }

    static remove(file) {

        try {

            if (

                fs.existsSync(file)

            ) {

                fs.unlinkSync(file);

            }

            return true;

        }

        catch {

            return false;

        }

    }

    static copy(source, destination) {

        try {

            fs.mkdirSync(

                path.dirname(destination),

                {

                    recursive: true

                }

            );

            fs.copyFileSync(

                source,

                destination

            );

            return true;

        }

        catch {

            return false;

        }

    }

    static move(source, destination) {

        try {

            fs.mkdirSync(

                path.dirname(destination),

                {

                    recursive: true

                }

            );

            fs.renameSync(

                source,

                destination

            );

            return true;

        }

        catch {

            return false;

        }

    }

    static list(directory) {

        try {

            return fs.readdirSync(directory);

        }

        catch {

            return [];

        }

    }

    static info(file) {

        try {

            const stat = fs.statSync(file);

            return {

                name: path.basename(file),

                extension: path.extname(file),

                size: stat.size,

                created: stat.birthtime,

                modified: stat.mtime,

                directory: stat.isDirectory(),

                file: stat.isFile()

            };

        }

        catch {

            return null;

        }

    }

    static ensureDirectory(directory) {

        if (

            !fs.existsSync(directory)

        ) {

            fs.mkdirSync(

                directory,

                {

                    recursive: true

                }

            );

        }

    }

}

module.exports = FileUtil;
