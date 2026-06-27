/**
 * =====================================================
 * AI Empire Pro V8
 * Helper Functions
 * Datei: assets/js/helpers.js
 * =====================================================
 */

const Helpers = {

    formatCurrency(value, currency = "EUR") {

        return new Intl.NumberFormat("de-DE", {

            style: "currency",

            currency: currency

        }).format(Number(value));

    },

    formatNumber(value) {

        return new Intl.NumberFormat("de-DE").format(Number(value));

    },

    formatPercent(value) {

        return Number(value).toFixed(2) + "%";

    },

    formatDate(date = new Date()) {

        return new Date(date).toLocaleString("de-DE");

    },

    random(min, max) {

        return Math.floor(

            Math.random() * (max - min + 1)

        ) + min;

    },

    uuid() {

        return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(

            /[xy]/g,

            function(c) {

                const r = Math.random() * 16 | 0;

                const v = c === "x"

                    ? r

                    : (r & 0x3 | 0x8);

                return v.toString(16);

            }

        );

    },

    debounce(callback, delay = 300) {

        let timer;

        return (...args) => {

            clearTimeout(timer);

            timer = setTimeout(() => {

                callback(...args);

            }, delay);

        };

    },

    copy(text) {

        navigator.clipboard.writeText(text);

        Toast.success("In Zwischenablage kopiert.");

    },

    download(filename, content) {

        const blob = new Blob(

            [content],

            {

                type: "text/plain"

            }

        );

        const url = URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;

        link.download = filename;

        link.click();

        URL.revokeObjectURL(url);

    },

    sleep(ms) {

        return new Promise(resolve =>

            setTimeout(resolve, ms)

        );

    }

};

window.Helpers = Helpers;
