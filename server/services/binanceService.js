/**
 * =====================================================
 * AI Empire Pro V8
 * Binance Service
 * Datei: server/services/binanceService.js
 * =====================================================
 */

const axios = require("axios");

class BinanceService {

    constructor() {

        this.baseURL = "https://api.binance.com";

        this.client = axios.create({

            baseURL: this.baseURL,

            timeout: 10000,

            headers: {

                "Content-Type": "application/json"

            }

        });

    }

    async ping() {

        try {

            await this.client.get("/api/v3/ping");

            return true;

        }

        catch {

            return false;

        }

    }

    async getTicker(symbol = "BTCUSDT") {

        try {

            const { data } = await this.client.get(

                "/api/v3/ticker/price",

                {

                    params: {

                        symbol

                    }

                }

            );

            return {

                success: true,

                symbol: data.symbol,

                price: Number(data.price)

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

    async get24h(symbol = "BTCUSDT") {

        try {

            const { data } = await this.client.get(

                "/api/v3/ticker/24hr",

                {

                    params: {

                        symbol

                    }

                }

            );

            return {

                success: true,

                data

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

    async getKlines(

        symbol = "BTCUSDT",

        interval = "1h",

        limit = 100

    ) {

        try {

            const { data } = await this.client.get(

                "/api/v3/klines",

                {

                    params: {

                        symbol,

                        interval,

                        limit

                    }

                }

            );

            return {

                success: true,

                candles: data.map(candle => ({

                    openTime: candle[0],

                    open: Number(candle[1]),

                    high: Number(candle[2]),

                    low: Number(candle[3]),

                    close: Number(candle[4]),

                    volume: Number(candle[5]),

                    closeTime: candle[6]

                }))

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

module.exports = new BinanceService();
