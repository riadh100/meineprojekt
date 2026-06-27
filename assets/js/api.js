/**
 * =====================================================
 * AI Empire Pro V8
 * API Client
 * Datei: assets/js/api.js
 * =====================================================
 */

const API = {

    baseURL: "http://localhost:3000/api",

    async request(endpoint, options = {}) {

        try {

            const response = await fetch(

                this.baseURL + endpoint,

                {

                    headers: {

                        "Content-Type": "application/json"

                    },

                    ...options

                }

            );

            if (!response.ok) {

                throw new Error(

                    "HTTP " + response.status

                );

            }

            return await response.json();

        }

        catch(error){

            console.error(error);

            Toast.error(error.message);

            return null;

        }

    },

    get(endpoint){

        return this.request(endpoint);

    },

    post(endpoint,data={}){

        return this.request(endpoint,{

            method:"POST",

            body:JSON.stringify(data)

        });

    },

    put(endpoint,data={}){

        return this.request(endpoint,{

            method:"PUT",

            body:JSON.stringify(data)

        });

    },

    delete(endpoint){

        return this.request(endpoint,{

            method:"DELETE"

        });

    },

    async health(){

        return await this.get("/health");

    },

    async dashboard(){

        return await this.get("/dashboard");

    },

    async trading(){

        return await this.get("/trading");

    },

    async assistant(){

        return await this.get("/assistant");

    },

    async telegram(){

        return await this.get("/telegram");

    },

    async video(){

        return await this.get("/video");

    },

    async game(){

        return await this.get("/game");

    }

};

window.API = API;
