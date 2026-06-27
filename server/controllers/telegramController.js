/**
 * =====================================================
 * AI Empire Pro V8
 * Telegram Controller
 * Datei: server/controllers/telegramController.js
 * =====================================================
 */

const TelegramBot = require("node-telegram-bot-api");

const TelegramSettings = require("../models/TelegramSettings");
const TelegramMessage = require("../models/TelegramMessage");

let bot = null;

class TelegramController {

    async init() {

        try {

            const settings = await TelegramSettings.findOne();

            if (!settings || !settings.token) {

                console.warn("Telegram Bot nicht konfiguriert.");

                return;

            }

            bot = new TelegramBot(

                settings.token,

                {

                    polling: true

                }

            );

            console.log("Telegram Bot gestartet.");

            bot.on("message", async (msg) => {

                await TelegramMessage.create({

                    chatId: msg.chat.id,

                    username: msg.from.username,

                    firstName: msg.from.first_name,

                    text: msg.text,

                    createdAt: new Date()

                });

            });

        }

        catch (error) {

            console.error(error);

        }

    }

    async status(req, res) {

        const settings = await TelegramSettings.findOne();

        return res.json({

            success: true,

            configured: !!settings,

            connected: bot !== null

        });

    }

    async send(req, res) {

        try {

            const {

                chatId,

                message

            } = req.body;

            if (!bot) {

                return res.status(400).json({

                    success: false,

                    message: "Bot nicht gestartet."

                });

            }

            await bot.sendMessage(

                chatId,

                message

            );

            return res.json({

                success: true,

                message: "Nachricht gesendet."

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Telegram Nachricht fehlgeschlagen."

            });

        }

    }

    async broadcast(req, res) {

        try {

            const {

                message

            } = req.body;

            const users = await TelegramMessage.distinct(

                "chatId"

            );

            let sent = 0;

            for (const chatId of users) {

                try {

                    await bot.sendMessage(

                        chatId,

                        message

                    );

                    sent++;

                }

                catch (err) {

                    console.error(

                        "Telegram Fehler:",

                        chatId

                    );

                }

            }

            return res.json({

                success: true,

                recipients: sent

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Broadcast fehlgeschlagen."

            });

        }

    }

    async history(req, res) {

        try {

            const messages = await TelegramMessage.find()

                .sort({

                    createdAt: -1

                })

                .limit(100);

            return res.json({

                success: true,

                messages

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Telegram Verlauf konnte nicht geladen werden."

            });

        }

    }

}

module.exports = new TelegramController();
