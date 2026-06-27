/**
 * =====================================================
 * AI Empire Pro V8
 * Theme Switcher
 * Datei: assets/js/theme-switcher.js
 * =====================================================
 */

const ThemeSwitcher = {

    current: "dark",

    init() {

        const saved = localStorage.getItem("theme");

        if (saved) {

            this.current = saved;

        }

        this.apply();

        this.bind();

        console.log("✔ Theme Switcher gestartet.");

    },

    bind() {

        const button = document.getElementById("theme-toggle");

        if (!button) return;

        button.addEventListener("click", () => {

            this.toggle();

        });

    },

    toggle() {

        this.current = this.current === "dark"

            ? "light"

            : "dark";

        this.apply();

        localStorage.setItem(

            "theme",

            this.current

        );

        Toast.info(

            "Theme",

            this.current === "dark"

                ? "Dark Mode aktiviert"

                : "Light Mode aktiviert"

        );

    },

    apply() {

        document.documentElement.setAttribute(

            "data-theme",

            this.current

        );

        const button = document.getElementById("theme-toggle");

        if (button) {

            button.textContent =

                this.current === "dark"

                    ? "🌙"

                    : "☀️";

        }

    },

    isDark() {

        return this.current === "dark";

    },

    isLight() {

        return this.current === "light";

    }

};

window.ThemeSwitcher = ThemeSwitcher;
