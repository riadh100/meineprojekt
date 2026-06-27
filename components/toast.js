/**
 * =====================================================
 * AI Empire Pro V8
 * Component - Toast
 * Datei: components/toast.js
 * =====================================================
 */

const Toast = {

    container: null,

    init() {

        if (this.container) return;

        this.container = document.createElement("div");

        this.container.id = "toast-container";

        document.body.appendChild(this.container);

    },

    show(message, type = "info", duration = 3000) {

        this.init();

        const toast = document.createElement("div");

        toast.className = `toast toast-${type}`;

        toast.innerHTML = `

            <div class="toast-content">

                ${message}

            </div>

        `;

        this.container.appendChild(toast);

        setTimeout(() => {

            toast.classList.add("toast-hide");

            setTimeout(() => {

                toast.remove();

            }, 300);

        }, duration);

    },

    success(message) {

        this.show(message, "success");

    },

    error(message) {

        this.show(message, "error");

    },

    warning(message) {

        this.show(message, "warning");

    },

    info(message) {

        this.show(message, "info");

    },

    clear() {

        if (!this.container) return;

        this.container.innerHTML = "";

    }

};

window.Toast = Toast;
