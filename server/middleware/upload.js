/**
 * =====================================================
 * AI Empire Pro V8
 * Upload Middleware
 * Datei: server/middleware/upload.js
 * =====================================================
 */

const multer = require("multer");
const path = require("path");
const fs = require("fs");

const UPLOAD_DIR = path.join(

    process.cwd(),

    "uploads"

);

if (!fs.existsSync(UPLOAD_DIR)) {

    fs.mkdirSync(

        UPLOAD_DIR,

        {

            recursive: true

        }

    );

}

const storage = multer.diskStorage({

    destination(req, file, cb) {

        cb(

            null,

            UPLOAD_DIR

        );

    },

    filename(req, file, cb) {

        const ext = path.extname(

            file.originalname

        );

        const name =

            Date.now() +

            "-" +

            Math.round(

                Math.random() * 1e9

            ) +

            ext;

        cb(

            null,

            name

        );

    }

});

const allowedTypes = [

    "image/png",

    "image/jpeg",

    "image/webp",

    "image/gif",

    "video/mp4",

    "video/webm",

    "video/quicktime",

    "application/pdf",

    "text/plain",

    "application/zip"

];

const upload = multer({

    storage,

    limits: {

        fileSize: 500 * 1024 * 1024

    },

    fileFilter(req, file, cb) {

        if (

            allowedTypes.includes(file.mimetype)

        ) {

            return cb(

                null,

                true

            );

        }

        cb(

            new Error(

                "Dateityp nicht erlaubt."

            )

        );

    }

});

module.exports = upload;
