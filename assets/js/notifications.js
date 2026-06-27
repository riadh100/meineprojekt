/**
 * =====================================================
 * AI Empire Pro V8
 * Notification Center
 * Datei: assets/js/notifications.js
 * =====================================================
 */

const NotificationCenter = {

    notifications: [],

    init() {

        this.load();

        console.log("✔ Notification Center gestartet.");

    },

    add(title, message, type = "info") {

        const notification = {

            id: Helpers.uuid(),

            title,

            message,

            type,

            created: new Date().toISOString(),

            read: false

        };

        this.notifications.unshift(notification);

        this.save();

        Toast.show(message, type);

        this.updateBadge();

    },

    success(title, message) {

        this.add(title, message, "success");

    },

    warning(title, message) {

        this.add(title, message, "warning");

    },

    error(title, message) {

        this.add(title, message, "error");

    },

    info(title, message) {

        this.add(title, message, "info");

    },

    getAll() {

        return this.notifications;

    },

    unread() {

        return this.notifications.filter(

            item => !item.read

        );

    },

    markAsRead(id) {

        const item = this.notifications.find(

            n => n.id === id

        );

        if (!item) return;

        item.read = true;

        this.save();

        this.updateBadge();

    },

    clear() {

        this.notifications = [];

        this.save();

        this.updateBadge();

    },

    updateBadge() {

        const badge = document.getElementById(

            "notification-count"

        );

        if (!badge) return;

        badge.textContent = this.unread().length;

    },

    save() {

        localStorage.setItem(

            "notifications",

            JSON.stringify(this.notifications)

        );

    },

    load() {

        const data = localStorage.getItem(

            "notifications"

        );

        if (!data) return;

        this.notifications = JSON.parse(data);

    }

};

window.NotificationCenter = NotificationCenter;
