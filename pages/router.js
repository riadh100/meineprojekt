/**
 * =====================================================
 * AI Empire Pro V8
 * Page Router
 * Datei: pages/router.js
 * =====================================================
 */

const PageRouter = {

    routes: {

        dashboard: DashboardPage,

        assistant: AssistantPage,

        trading: TradingPage,

        telegram: TelegramPage,

        video: VideoPage,

        game: GamePage,

        tools: ToolsPage,

        setup: SetupPage

    },

    current: "dashboard",

    init() {

        Object.keys(this.routes).forEach(route => {

            Router.register(route, () => {

                this.navigate(route);

            });

        });

        this.navigate(this.current);

    },

    navigate(route) {

        if (!this.routes[route]) {

            console.error("Seite nicht gefunden:", route);

            return;

        }

        this.current = route;

        StateManager.set("app.currentPage", route);

        const page = this.routes[route];

        page.render("app");

        this.updateSidebar(route);

        document.title = `AI Empire Pro • ${route}`;

    },

    updateSidebar(active) {

        document
            .querySelectorAll(".sidebar-item")
            .forEach(item => {

                item.classList.remove("active");

            });

        const button = document.querySelector(

            `.sidebar-item[onclick="Router.navigate('${active}')"]`

        );

        if (button) {

            button.classList.add("active");

        }

    },

    reload() {

        this.navigate(this.current);

    },

    getCurrent() {

        return this.current;

    }

};

window.PageRouter = PageRouter;
