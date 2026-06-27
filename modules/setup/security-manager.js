/**
 * =====================================================
 * AI Empire Pro V8
 * Setup - Security Manager
 * Datei: modules/setup/security-manager.js
 * =====================================================
 */

const SecurityManager = {

    settings: {

        twoFactor: false,

        autoLock: false,

        sessionTimeout: 30,

        loginNotifications: true

    },

    init() {

        this.load();

        console.log("✔ Security Manager gestartet.");

    },

    enable2FA() {

        this.settings.twoFactor = true;

        this.save();

    },

    disable2FA() {

        this.settings.twoFactor = false;

        this.save();

    },

    enableAutoLock() {

        this.settings.autoLock = true;

        this.save();

    },

    disableAutoLock() {

        this.settings.autoLock = false;

        this.save();

    },

    setSessionTimeout(minutes) {

        this.settings.sessionTimeout = Number(minutes);

        this.save();

    },

    enableLoginNotifications() {

        this.settings.loginNotifications = true;

        this.save();

    },

    disableLoginNotifications() {

        this.settings.loginNotifications = false;

        this.save();

    },

    get() {

        return this.settings;

    },

    reset() {

        this.settings = {

            twoFactor: false,

            autoLock: false,

            sessionTimeout: 30,

            loginNotifications: true

        };

        this.save();

    },

    save() {

        StateManager.set(
            "setup.security",
            this.settings
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "setup.security"
        );

        if (data) {

            this.settings = {

                ...this.settings,

                ...data

            };

        }

    }

};

window.SecurityManager = SecurityManager;
