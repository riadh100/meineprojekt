/**
 * =====================================================
 * AI Empire Pro V8
 * CoinGecko Service
 * Datei: server/services/coingeckoService.js
 * =====================================================
 */

const axios = require("axios");

class CoinGeckoService {

    constructor() {

        this.client = axios.create({

            baseURL: "https://api.coingecko.com/api/v3",

            timeout: 10000,

            headers: {

                "Content-Type": "application/json"

            }

        });

    }

    async ping() {

        try {

            await this.client.get("/ping");

            return true;

        }

        catch {

            return false;

        }

    }

    async getPrice(ids = ["bitcoin"], currencies = ["usd"]) {

        try {

            const { data } = await this.client.get(

                "/simple/price",

                {

                    params: {

                        ids: ids.join(","),

                        vs_currencies: currencies.join(",")

                    }

                }

            );

            return {

                success: true,

                prices: data

            };

        }

        catch (error) {

            console.error(error);

            return {

                success: false,

                error: error.message

            };

        }

    }

    async getMarkets(currency = "usd") {

        try {

            const { data } = await this.client.get(

                "/coins/markets",

                {

                    params: {

                        vs_currency: currency,

                        order: "market_cap_desc",

                        per_page: 100,

                        page: 1,

                        sparkline: false

                    }

                }

            );

            return {

                success: true,

                markets: data

            };

        }

        catch (error) {

            console.error(error);

            return {

                success: false,

                error: error.message

            };

        }

    }

    async getCoin(id = "bitcoin") {

        try {

            const { data } = await this.client.get(

                `/coins/${id}`

            );

            return {

                success: true,

                coin: data

            };

        }

        catch (error) {

            console.error(error);

            return {

                success: false,

                error: error.message

            };

        }

    }

    async getTrending() {

        try {

            const { data } = await this.client.get(

                "/search/trending"

            );

            return {

                success: true,

                trending: data.coins

            };

        }

        catch (error) {

            console.error(error);

            return {

                success: false,

                error: error.message

            };

        }

    }

}

module.exports = new CoinGeckoService();
