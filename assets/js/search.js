/**
 * =====================================================
 * AI Empire Pro V8
 * Global Search
 * Datei: assets/js/search.js
 * =====================================================
 */

const Search = {

    index: [],

    init() {

        this.buildIndex();

        this.bind();

        console.log("✔ Search gestartet.");

    },

    buildIndex() {

        this.index = [

            { type: "page", title: "Dashboard", route: "dashboard" },
            { type: "page", title: "AI Assistant", route: "assistant" },
            { type: "page", title: "Trading", route: "trading" },
            { type: "page", title: "Telegram", route: "telegram" },
            { type: "page", title: "Video Studio", route: "video" },
            { type: "page", title: "Games", route: "game" },
            { type: "page", title: "Tools", route: "tools" },
            { type: "page", title: "Einstellungen", route: "setup" }

        ];

    },

    bind() {

        const input = document.getElementById("global-search");

        if (!input) return;

        input.addEventListener("input", event => {

            this.run(event.target.value);

        });

    },

    run(query) {

        query = query.toLowerCase().trim();

        if (!query) {

            this.close();

            return;

        }

        const results = this.index.filter(item =>

            item.title.toLowerCase().includes(query)

        );

        this.render(results);

    },

    render(results) {

        this.close();

        const input = document.getElementById("global-search");

        if (!input) return;

        const box = document.createElement("div");

        box.id = "search-results";

        box.className = "search-results";

        if (!results.length) {

            box.innerHTML = `

                <div class="search-item">

                    Keine Ergebnisse

                </div>

            `;

        } else {

            results.forEach(item => {

                box.innerHTML += `

                    <div
                        class="search-item"
                        onclick="Search.open('${item.route}')">

                        <strong>${item.title}</strong>

                        <small>${item.type}</small>

                    </div>

                `;

            });

        }

        input.parentElement.appendChild(box);

    },

    open(route) {

        Router.navigate(route);

        this.close();

        const input = document.getElementById("global-search");

        if (input) {

            input.value = "";

        }

    },

    close() {

        const box = document.getElementById("search-results");

        if (box) {

            box.remove();

        }

    }

};

window.Search = Search;
