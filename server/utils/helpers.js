/**
 * =====================================================
 * AI Empire Pro V8
 * Helper Utilities
 * Datei: server/utils/helpers.js
 * =====================================================
 */

const crypto = require("crypto");

class Helpers {

    static uuid() {

        return crypto.randomUUID();

    }

    static randomString(length = 32) {

        return crypto

            .randomBytes(length)

            .toString("hex")

            .substring(0, length);

    }

    static sleep(ms) {

        return new Promise(resolve =>

            setTimeout(resolve, ms)

        );

    }

    static formatCurrency(

        value,

        currency = "EUR"

    ) {

        return new Intl.NumberFormat(

            "de-DE",

            {

                style: "currency",

                currency

            }

        ).format(Number(value));

    }

    static formatNumber(value) {

        return new Intl.NumberFormat(

            "de-DE"

        ).format(Number(value));

    }

    static formatDate(date = new Date()) {

        return new Intl.DateTimeFormat(

            "de-DE",

            {

                dateStyle: "medium",

                timeStyle: "medium"

            }

        ).format(new Date(date));

    }

    static percentage(value, total) {

        if (!total) return 0;

        return Number(

            ((value / total) * 100)

            .toFixed(2)

        );

    }

    static clamp(value, min, max) {

        return Math.max(

            min,

            Math.min(max, value)

        );

    }

    static deepClone(object) {

        return JSON.parse(

            JSON.stringify(object)

        );

    }

    static isEmpty(value) {

        return (

            value === undefined ||

            value === null ||

            value === "" ||

            (Array.isArray(value) &&

                value.length === 0)

        );

    }

    static now() {

        return new Date().toISOString();

    }

}

module.exports = Helpers;
