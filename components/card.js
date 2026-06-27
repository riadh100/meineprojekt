/**
 * =====================================================
 * AI Empire Pro V8
 * Component - Card
 * Datei: components/card.js
 * =====================================================
 */

const Card = {

    create(options = {}) {

        const {

            title = "",

            value = "",

            subtitle = "",

            icon = "",

            color = "",

            id = ""

        } = options;

        return `

            <div class="card ${color}" id="${id}">

                <div class="card-header">

                    <div class="card-icon">

                        ${icon}

                    </div>

                    <div class="card-title">

                        ${title}

                    </div>

                </div>

                <div class="card-body">

                    <div class="card-value">

                        ${value}

                    </div>

                    <div class="card-subtitle">

                        ${subtitle}

                    </div>

                </div>

            </div>

        `;

    },

    update(id, value) {

        const card = document.getElementById(id);

        if (!card) return;

        const element = card.querySelector(".card-value");

        if (element) {

            element.textContent = value;

        }

    },

    updateSubtitle(id, subtitle) {

        const card = document.getElementById(id);

        if (!card) return;

        const element = card.querySelector(".card-subtitle");

        if (element) {

            element.textContent = subtitle;

        }

    },

    remove(id) {

        const card = document.getElementById(id);

        if (card) {

            card.remove();

        }

    }

};

window.Card = Card;
