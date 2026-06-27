/**
 * =====================================================
 * AI Empire Pro V8
 * Layout Manager
 * Datei: assets/js/layout.js
 * =====================================================
 */

const Layout = {

    sidebarCollapsed: false,

    init() {

        this.restore();

        this.bind();

        console.log("✔ Layout Manager gestartet.");

    },

    bind() {

        const toggle = document.getElementById("sidebar-toggle");

        if (toggle) {

            toggle.addEventListener("click", () => {

                this.toggleSidebar();

            });

        }

        window.addEventListener("resize", () => {

            this.handleResize();

        });

    },

    toggleSidebar() {

        this.sidebarCollapsed = !this.sidebarCollapsed;

        const sidebar = document.getElementById("sidebar");

        const layout = document.querySelector(".main-layout");

        if (!sidebar) return;

        sidebar.classList.toggle(

            "sidebar-collapsed",

            this.sidebarCollapsed

        );

        if (layout) {

            layout.classList.toggle(

                "sidebar-collapsed",

                this.sidebarCollapsed

            );

        }

        this.save();

    },

    expandSidebar() {

        this.sidebarCollapsed = false;

        this.apply();

    },

    collapseSidebar() {

        this.sidebarCollapsed = true;

        this.apply();

    },

    apply() {

        const sidebar = document.getElementById("sidebar");

        const layout = document.querySelector(".main-layout");

        if (!sidebar) return;

        sidebar.classList.toggle(

            "sidebar-collapsed",

            this.sidebarCollapsed

        );

        if (layout) {

            layout.classList.toggle(

                "sidebar-collapsed",

                this.sidebarCollapsed

            );

        }

        this.save();

    },

    handleResize() {

        if (window.innerWidth < 900) {

            this.collapseSidebar();

        }

    },

    save() {

        localStorage.setItem(

            "sidebar-collapsed",

            this.sidebarCollapsed

        );

    },

    restore() {

        this.sidebarCollapsed =

            localStorage.getItem(

                "sidebar-collapsed"

            ) === "true";

        this.apply();

    }

};

window.Layout = Layout;
