/**
 * =====================================================
 * AI Empire Pro V8
 * Mail Service
 * Datei: server/services/mailService.js
 * =====================================================
 */

const nodemailer = require("nodemailer");

class MailService {

    constructor() {

        this.transporter = nodemailer.createTransport({

            host: process.env.SMTP_HOST,

            port: Number(process.env.SMTP_PORT) || 587,

            secure: false,

            auth: {

                user: process.env.SMTP_USER,

                pass: process.env.SMTP_PASSWORD

            }

        });

    }

    async verify() {

        try {

            await this.transporter.verify();

            return {

                success: true

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

    async send({

        to,

        subject,

        text = "",

        html = ""

    }) {

        try {

            const result = await this.transporter.sendMail({

                from:

                    process.env.SMTP_FROM ||

                    process.env.SMTP_USER,

                to,

                subject,

                text,

                html

            });

            return {

                success: true,

                messageId: result.messageId

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

    async sendWelcome(user) {

        return this.send({

            to: user.email,

            subject: "Willkommen bei AI Empire Pro",

            html: `

                <h2>Willkommen ${user.username}</h2>

                <p>

                    Dein Konto wurde erfolgreich erstellt.

                </p>

            `

        });

    }

    async sendPasswordReset(user, token) {

        return this.send({

            to: user.email,

            subject: "Passwort zurücksetzen",

            html: `

                <h2>Passwort zurücksetzen</h2>

                <p>

                    Verwende folgenden Token:

                </p>

                <h3>${token}</h3>

            `

        });

    }

}

module.exports = new MailService();
