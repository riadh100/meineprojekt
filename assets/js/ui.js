/**
 * =====================================================
 * AI Empire Pro V8
 * UI Manager
 * Datei: assets/js/ui.js
 * =====================================================
 */

const UI = {

    init() {

        this.updateClock();

        this.startClock();

        this.initTooltips();

        this.initDropdowns();

        this.initShortcuts();

        console.log("✔ UI Manager gestartet.");

    },

    updateClock() {

        const clock = document.getElementById("ui-clock");

        if (!clock) return;

        clock.textContent = new Date().toLocaleTimeString("de-DE");

    },

    startClock() {

        setInterval(() => {

            this.updateClock();

        }, 1000);

    },

    initTooltips() {

        document.querySelectorAll("[data-tooltip]").forEach(element => {

            element.addEventListener("mouseenter", () => {

                element.setAttribute(

                    "title",

                    element.dataset.tooltip

                );

            });

        });

    },

    initDropdowns() {

        document.querySelectorAll(".dropdown-toggle").forEach(button => {

            button.addEventListener("click", () => {

                const menu = button.nextElementSibling;

                if (!menu) return;

                menu.classList.toggle("hidden");

            });

        });

    },

    initShortcuts() {

        document.addEventListener("keydown", event => {

            if (event.ctrlKey && event.key === "k") {

                event.preventDefault();

                const search = document.getElementById("global-search");

                if (search) {

                    search.focus();

                }

            }

        });

    },

    show(elementId) {

        const element = document.getElementById(elementId);

        if (element) {

            element.classList.remove("hidden");

        }

    },

    hide(elementId) {

        const element = document.getElementById(elementId);

        if (element) {

            element.classList.add("hidden");

        }

    },

    toggle(elementId) {

        const element = document.getElementById(elementId);

        if (element) {

            element.classList.toggle("hidden");

        }

    },

    setTitle(title) {

        document.title = `AI Empire Pro • ${title}`;

    },

    loading(show = true, text = "Lade...") {

        if (show) {

            Loader.show(text);

        } else {

            Loader.hide();

        }

    }

};

window.UI = UI;
