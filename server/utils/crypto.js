/**
 * =====================================================
 * AI Empire Pro V8
 * Crypto Utilities
 * Datei: server/utils/crypto.js
 * =====================================================
 */

const crypto = require("crypto");

class CryptoUtil {

    static algorithm = "aes-256-cbc";

    static secret = crypto
        .createHash("sha256")
        .update(
            process.env.APP_SECRET ||
            "AI_EMPIRE_SECRET"
        )
        .digest();

    static encrypt(text = "") {

        const iv = crypto.randomBytes(16);

        const cipher = crypto.createCipheriv(

            this.algorithm,

            this.secret,

            iv

        );

        let encrypted = cipher.update(

            String(text),

            "utf8",

            "hex"

        );

        encrypted += cipher.final("hex");

        return {

            iv: iv.toString("hex"),

            value: encrypted

        };

    }

    static decrypt(data) {

        try {

            const decipher = crypto.createDecipheriv(

                this.algorithm,

                this.secret,

                Buffer.from(data.iv, "hex")

            );

            let decrypted = decipher.update(

                data.value,

                "hex",

                "utf8"

            );

            decrypted += decipher.final("utf8");

            return decrypted;

        }

        catch {

            return null;

        }

    }

    static hash(value = "") {

        return crypto

            .createHash("sha256")

            .update(String(value))

            .digest("hex");

    }

    static hmac(value = "") {

        return crypto

            .createHmac(

                "sha256",

                this.secret

            )

            .update(String(value))

            .digest("hex");

    }

    static random(length = 32) {

        return crypto

            .randomBytes(length)

            .toString("hex");

    }

    static compare(a, b) {

        return crypto.timingSafeEqual(

            Buffer.from(String(a)),

            Buffer.from(String(b))

        );

    }

}

module.exports = CryptoUtil;
