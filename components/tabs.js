/**
 * =====================================================
 * AI Empire Pro V8
 * Component - Tabs
 * Datei: components/tabs.js
 * =====================================================
 */

const Tabs = {

    current: null,

    init(containerId, tabs = []) {

        const container = document.getElementById(containerId);

        if (!container) return;

        let html = `

            <div class="tabs">

                <div class="tabs-header">

        `;

        tabs.forEach((tab, index) => {

            html += `

                <button
                    class="tab-button ${index === 0 ? "active" : ""}"
                    data-tab="${tab.id}">

                    ${tab.title}

                </button>

            `;

        });

        html += `

                </div>

                <div class="tabs-content">

        `;

        tabs.forEach((tab, index) => {

            html += `

                <div
                    class="tab-panel"
                    id="${tab.id}"
                    style="display:${index === 0 ? "block" : "none"};">

                    ${tab.content || ""}

                </div>

            `;

        });

        html += `

                </div>

            </div>

        `;

        container.innerHTML = html;

        container.querySelectorAll(".tab-button").forEach(button => {

            button.addEventListener("click", () => {

                this.open(container, button.dataset.tab);

            });

        });

        this.current = tabs.length ? tabs[0].id : null;

    },

    open(container, tabId) {

        container.querySelectorAll(".tab-button").forEach(button => {

            button.classList.remove("active");

        });

        container.querySelectorAll(".tab-panel").forEach(panel => {

            panel.style.display = "none";

        });

        const activeButton = container.querySelector(
            `[data-tab="${tabId}"]`
        );

        const activePanel = container.querySelector(
            `#${tabId}`
        );

        if (activeButton) {

            activeButton.classList.add("active");

        }

        if (activePanel) {

            activePanel.style.display = "block";

        }

        this.current = tabId;

    },

    getCurrent() {

        return this.current;

    }

};

window.Tabs = Tabs;
