/**
 * =====================================================
 * AI Empire Pro V8
 * Core - Theme Manager
 * Datei: core/theme.js
 * =====================================================
 */

const ThemeManager = {

    current: "dark",

    init() {

        const savedTheme = StateManager.get("settings.theme");

        if (savedTheme) {
            this.current = savedTheme;
        }

        this.apply(this.current);

    },

    apply(theme) {

        this.current = theme;

        document.documentElement.setAttribute("data-theme", theme);

        StateManager.set("settings.theme", theme);

        StorageManager.save();

        console.log("Theme:", theme);

    },

    toggle() {

        if (this.current === "dark") {
            this.apply("light");
        } else {
            this.apply("dark");
        }

    },

    getTheme() {

        return this.current;

    },

    isDark() {

        return this.current === "dark";

    },

    isLight() {

        return this.current === "light";

    }

};

window.ThemeManager = ThemeManager;
