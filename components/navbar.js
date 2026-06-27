/**
 * =====================================================
 * AI Empire Pro V8
 * Component - Navbar
 * Datei: components/navbar.js
 * =====================================================
 */

const Navbar = {

    render(containerId = "navbar") {

        const container = document.getElementById(containerId);

        if (!container) return;

        container.innerHTML = `

            <div class="navbar">

                <div class="navbar-left">

                    <input
                        type="search"
                        id="global-search"
                        placeholder="Suche..."
                        autocomplete="off">

                </div>

                <div class="navbar-right">

                    <button
                        id="theme-toggle"
                        class="navbar-btn"
                        title="Theme wechseln">

                        🌙

                    </button>

                    <button
                        id="notification-btn"
                        class="navbar-btn"
                        title="Benachrichtigungen">

                        🔔

                    </button>

                    <div class="navbar-user">

                        <span>👑</span>

                        <span id="navbar-username">

                            Empire Pro

                        </span>

                    </div>

                </div>

            </div>

        `;

        this.bindEvents();

    },

    bindEvents() {

        const themeButton = document.getElementById("theme-toggle");

        if (themeButton) {

            themeButton.addEventListener("click", () => {

                ThemeManager.toggle();

            });

        }

        const search = document.getElementById("global-search");

        if (search) {

            search.addEventListener("input", (event) => {

                console.log("Suche:", event.target.value);

            });

        }

        this.refresh();

    },

    refresh() {

        const username = StateManager.get("user.username");

        const element = document.getElementById("navbar-username");

        if (element && username) {

            element.textContent = username;

        }

    }

};

window.Navbar = Navbar;
