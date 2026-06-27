/**
 * =====================================================
 * AI Empire Pro V8
 * Setup - Profile Manager
 * Datei: modules/setup/profile-manager.js
 * =====================================================
 */

const ProfileManager = {

    profile: {

        username: "",

        email: "",

        avatar: "",

        role: "User"

    },

    init() {

        this.load();

        console.log("✔ Profile Manager gestartet.");

    },

    set(data) {

        this.profile = {

            ...this.profile,

            ...data

        };

        this.save();

    },

    get() {

        return this.profile;

    },

    update(key, value) {

        this.profile[key] = value;

        this.save();

    },

    reset() {

        this.profile = {

            username: "",

            email: "",

            avatar: "",

            role: "User"

        };

        this.save();

    },

    save() {

        StateManager.set(
            "setup.profile",
            this.profile
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "setup.profile"
        );

        if (data) {

            this.profile = {

                ...this.profile,

                ...data

            };

        }

    }

};

window.ProfileManager = ProfileManager;
