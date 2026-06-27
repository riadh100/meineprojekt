/**
 * =====================================================
 * AI Empire Pro V8
 * Authentication Manager
 * Datei: assets/js/auth.js
 * =====================================================
 */

const Auth = {

    token: null,

    user: null,

    init() {

        this.token = localStorage.getItem("auth_token");

        const user = localStorage.getItem("auth_user");

        if (user) {

            this.user = JSON.parse(user);

        }

    },

    isLoggedIn() {

        return !!this.token;

    },

    async login(username, password) {

        try {

            Loader.show("Anmeldung...");

            const response = await API.post("/auth/login", {

                username,

                password

            });

            Loader.hide();

            if (!response || !response.token) {

                Toast.error("Login fehlgeschlagen.");

                return false;

            }

            this.token = response.token;

            this.user = response.user;

            localStorage.setItem(

                "auth_token",

                response.token

            );

            localStorage.setItem(

                "auth_user",

                JSON.stringify(response.user)

            );

            Toast.success("Erfolgreich angemeldet.");

            return true;

        }

        catch(error){

            Loader.hide();

            Toast.error(error.message);

            return false;

        }

    },

    logout() {

        this.token = null;

        this.user = null;

        localStorage.removeItem("auth_token");

        localStorage.removeItem("auth_user");

        Toast.info("Abgemeldet.");

        location.reload();

    },

    getToken() {

        return this.token;

    },

    getUser() {

        return this.user;

    },

    authorizationHeader() {

        if (!this.token) {

            return {};

        }

        return {

            Authorization:

                "Bearer " + this.token

        };

    }

};

window.Auth = Auth;
