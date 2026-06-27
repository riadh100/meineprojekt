/**
 * =====================================================
 * AI Empire Pro V8
 * Session Manager
 * Datei: assets/js/session-manager.js
 * =====================================================
 */

const SessionManager = {

    session: null,

    timeout: 30 * 60 * 1000,

    timer: null,

    init() {

        this.restore();

        this.bind();

        Logger.success("Session Manager gestartet.");

    },

    create(user = {}) {

        this.session = {

            id: Helpers.uuid(),

            user,

            started: new Date().toISOString(),

            lastActivity: Date.now(),

            authenticated: true

        };

        this.save();

        this.resetTimer();

    },

    destroy() {

        this.session = null;

        clearTimeout(this.timer);

        StorageManager.remove("session");

        NotificationCenter.info(

            "Sitzung",

            "Abgemeldet"

        );

    },

    bind() {

        [

            "click",

            "mousemove",

            "keydown",

            "scroll",

            "touchstart"

        ].forEach(eventName => {

            document.addEventListener(eventName, () => {

                this.touch();

            });

        });

    },

    touch() {

        if (!this.session) return;

        this.session.lastActivity = Date.now();

        this.save();

        this.resetTimer();

    },

    resetTimer() {

        clearTimeout(this.timer);

        this.timer = setTimeout(() => {

            this.expire();

        }, this.timeout);

    },

    expire() {

        Logger.warn("Session abgelaufen.");

        NotificationCenter.warning(

            "Session",

            "Die Sitzung ist abgelaufen."

        );

        this.destroy();

        location.reload();

    },

    save() {

        StorageManager.set(

            "session",

            this.session

        );

    },

    restore() {

        this.session = StorageManager.get(

            "session"

        );

        if (this.session) {

            this.resetTimer();

        }

    },

    isAuthenticated() {

        return !!(

            this.session &&

            this.session.authenticated

        );

    },

    getUser() {

        return this.session

            ? this.session.user

            : null;

    }

};

window.SessionManager = SessionManager;
