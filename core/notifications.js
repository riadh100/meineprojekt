/**
 * =====================================================
 * AI Empire Pro V8
 * Core - Notification Manager
 * Datei: core/notifications.js
 * =====================================================
 */

const NotificationManager = {

    notifications: [],

    show(message, type = "info", duration = 3000) {

        const notification = {
            id: Date.now(),
            message,
            type,
            time: new Date().toLocaleTimeString()
        };

        this.notifications.push(notification);

        console.log(`[${type.toUpperCase()}] ${message}`);

        const container = this.getContainer();

        const element = document.createElement("div");

        element.className = `notification notification-${type}`;
        element.dataset.id = notification.id;
        element.textContent = message;

        container.appendChild(element);

        setTimeout(() => {
            element.remove();
            this.remove(notification.id);
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

    remove(id) {
        this.notifications = this.notifications.filter(
            item => item.id !== id
        );
    },

    clear() {

        this.notifications = [];

        const container = document.getElementById("notification-container");

        if (container) {
            container.innerHTML = "";
        }

    },

    getContainer() {

        let container = document.getElementById("notification-container");

        if (!container) {

            container = document.createElement("div");

            container.id = "notification-container";

            document.body.appendChild(container);

        }

        return container;

    }

};

window.NotificationManager = NotificationManager;
