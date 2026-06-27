/**
 * =====================================================
 * AI Empire Pro V8
 * Component - Modal
 * Datei: components/modal.js
 * =====================================================
 */

const Modal = {

    current: null,

    open(options = {}) {

        this.close();

        const {

            title = "Dialog",

            content = "",

            width = "600px",

            closable = true

        } = options;

        const overlay = document.createElement("div");

        overlay.className = "modal-overlay";

        overlay.innerHTML = `

            <div class="modal-window" style="max-width:${width};">

                <div class="modal-header">

                    <h2>${title}</h2>

                    ${closable ? '<button class="modal-close">&times;</button>' : ''}

                </div>

                <div class="modal-content">

                    ${content}

                </div>

            </div>

        `;

        document.body.appendChild(overlay);

        this.current = overlay;

        if (closable) {

            overlay.querySelector(".modal-close").addEventListener("click", () => {

                this.close();

            });

            overlay.addEventListener("click", (event) => {

                if (event.target === overlay) {

                    this.close();

                }

            });

        }

    },

    close() {

        if (!this.current) return;

        this.current.remove();

        this.current = null;

    },

    isOpen() {

        return this.current !== null;

    }

};

window.Modal = Modal;
