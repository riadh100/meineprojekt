/**
 * =====================================================
 * AI Empire Pro V8
 * Component - Loader
 * Datei: components/loader.js
 * =====================================================
 */

const Loader = {

    element: null,

    show(message = "Lade...") {

        this.hide();

        this.element = document.createElement("div");

        this.element.className = "loader-overlay";

        this.element.innerHTML = `

            <div class="loader-box">

                <div class="loader-spinner"></div>

                <div class="loader-text">

                    ${message}

                </div>

            </div>

        `;

        document.body.appendChild(this.element);

    },

    hide() {

        if (!this.element) return;

        this.element.remove();

        this.element = null;

    },

    update(message) {

        if (!this.element) return;

        const text = this.element.querySelector(".loader-text");

        if (text) {

            text.textContent = message;

        }

    },

    isVisible() {

        return this.element !== null;

    }

};

window.Loader = Loader;
