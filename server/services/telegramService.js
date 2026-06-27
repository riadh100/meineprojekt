/**
 * =====================================================
 * AI Empire Pro V8
 * Telegram Service
 * Datei: server/services/telegramService.js
 * =====================================================
 */

const TelegramBot = require("node-telegram-bot-api");

class TelegramService {

    constructor() {

        this.bot = null;

        this.connected = false;

    }

    init() {

        const token = process.env.TELEGRAM_BOT_TOKEN;

        if (!token) {

            console.warn("Telegram Token fehlt.");

            return false;

        }

        this.bot = new TelegramBot(token, {

            polling: true

        });

        this.connected = true;

        console.log("Telegram Service gestartet.");

        this.bot.on("polling_error", error => {

            console.error(error);

        });

        return true;

    }

    async send(chatId, message) {

        if (!this.connected) {

            return {

                success: false,

                message: "Bot nicht verbunden."

            };

        }

        try {

            const result = await this.bot.sendMessage(

                chatId,

                message,

                {

                    parse_mode: "HTML"

                }

            );

            return {

                success: true,

                result

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

    async sendPhoto(chatId, photo, caption = "") {

        try {

            const result = await this.bot.sendPhoto(

                chatId,

                photo,

                {

                    caption

                }

            );

            return {

                success: true,

                result

            };

        }

        catch (error) {

            return {

                success: false,

                error: error.message

            };

        }

    }

    async broadcast(chatIds = [], message = "") {

        const results = [];

        for (const chatId of chatIds) {

            const response = await this.send(

                chatId,

                message

            );

            results.push({

                chatId,

                success: response.success

            });

        }

        return {

            success: true,

            total: chatIds.length,

            delivered: results.filter(

                r => r.success

            ).length,

            results

        };

    }

    isConnected() {

        return this.connected;

    }

}

module.exports = new TelegramService();
