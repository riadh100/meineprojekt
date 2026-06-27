/**
 * =====================================================
 * AI Empire Pro V8
 * Formatter Utilities
 * Datei: server/utils/formatter.js
 * =====================================================
 */

class Formatter {

    static currency(value, currency = "EUR") {

        return new Intl.NumberFormat(

            "de-DE",

            {

                style: "currency",

                currency

            }

        ).format(Number(value));

    }

    static number(value, decimals = 2) {

        return Number(value).toLocaleString(

            "de-DE",

            {

                minimumFractionDigits: decimals,

                maximumFractionDigits: decimals

            }

        );

    }

    static percent(value, decimals = 2) {

        return `${Number(value).toFixed(decimals)} %`;

    }

    static date(date = new Date()) {

        return new Intl.DateTimeFormat(

            "de-DE",

            {

                dateStyle: "medium"

            }

        ).format(new Date(date));

    }

    static datetime(date = new Date()) {

        return new Intl.DateTimeFormat(

            "de-DE",

            {

                dateStyle: "medium",

                timeStyle: "medium"

            }

        ).format(new Date(date));

    }

    static time(date = new Date()) {

        return new Intl.DateTimeFormat(

            "de-DE",

            {

                timeStyle: "medium"

            }

        ).format(new Date(date));

    }

    static filesize(bytes) {

        if (bytes === 0) return "0 B";

        const sizes = [

            "B",

            "KB",

            "MB",

            "GB",

            "TB"

        ];

        const i = Math.floor(

            Math.log(bytes) /

            Math.log(1024)

        );

        return (

            (bytes / Math.pow(1024, i))

            .toFixed(2) +

            " " +

            sizes[i]

        );

    }

    static duration(seconds) {

        const h = Math.floor(seconds / 3600);

        const m = Math.floor(

            (seconds % 3600) / 60

        );

        const s = Math.floor(

            seconds % 60

        );

        return [

            h.toString().padStart(2, "0"),

            m.toString().padStart(2, "0"),

            s.toString().padStart(2, "0")

        ].join(":");

    }

    static capitalize(text = "") {

        return text.charAt(0)

            .toUpperCase() +

            text.slice(1);

    }

    static slug(text = "") {

        return text

            .toLowerCase()

            .trim()

            .replace(/\s+/g, "-")

            .replace(/[^\w-]/g, "");

    }

    static truncate(text = "", length = 100) {

        if (text.length <= length) {

            return text;

        }

        return text.substring(

            0,

            length

        ) + "...";

    }

}

module.exports = Formatter;
