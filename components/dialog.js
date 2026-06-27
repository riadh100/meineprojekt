/**
 * =====================================================
 * AI Empire Pro V8
 * Component - Dialog
 * Datei: components/dialog.js
 * =====================================================
 */

const Dialog = {

    current: null,

    confirm(title, message, onConfirm = null, onCancel = null) {

        this.close();

        const overlay = document.createElement("div");

        overlay.className = "dialog-overlay";

        overlay.innerHTML = `

            <div class="dialog">

                <div class="dialog-header">

                    <h2>${title}</h2>

                </div>

                <div class="dialog-body">

                    <p>${message}</p>

                </div>

                <div class="dialog-footer">

                    <button id="dialog-cancel">

                        Abbrechen

                    </button>

                    <button id="dialog-confirm">

                        OK

                    </button>

                </div>

            </div>

        `;

        document.body.appendChild(overlay);

        this.current = overlay;

        document
            .getElementById("dialog-confirm")
            .addEventListener("click", () => {

                if (typeof onConfirm === "function") {

                    onConfirm();

                }

                this.close();

            });

        document
            .getElementById("dialog-cancel")
            .addEventListener("click", () => {

                if (typeof onCancel === "function") {

                    onCancel();

                }

                this.close();

            });

    },

    alert(title, message) {

        this.confirm(title, message);

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

window.Dialog = Dialog;
