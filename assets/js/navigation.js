/**
 * =====================================================
 * AI Empire Pro V8
 * Navigation Manager
 * Datei: assets/js/navigation.js
 * =====================================================
 */

const Navigation = {

    current: "dashboard",

    history: [],

    init() {

        this.bindSidebar();

        this.restore();

        console.log("✔ Navigation Manager gestartet.");

    },

    bindSidebar() {

        document.addEventListener("click", event => {

            const button = event.target.closest("[data-route]");

            if (!button) return;

            event.preventDefault();

            this.go(button.dataset.route);

        });

    },

    go(route) {

        if (!route) return;

        if (this.current !== route) {

            this.history.push(this.current);

        }

        this.current = route;

        if (typeof PageRouter !== "undefined") {

            PageRouter.navigate(route);

        }

        this.highlight(route);

        this.save();

    },

    back() {

        if (!this.history.length) return;

        const previous = this.history.pop();

        this.go(previous);

    },

    reload() {

        if (typeof PageRouter !== "undefined") {

            PageRouter.reload();

        }

    },

    highlight(route) {

        document.querySelectorAll(".sidebar-item").forEach(item => {

            item.classList.remove("active");

            if (item.dataset.route === route) {

                item.classList.add("active");

            }

        });

    },

    save() {

        localStorage.setItem(

            "current-page",

            this.current

        );

    },

    restore() {

        const page = localStorage.getItem(

            "current-page"

        );

        if (page) {

            this.current = page;

        }

        this.go(this.current);

    },

    getCurrent() {

        return this.current;

    }

};

window.Navigation = Navigation;
