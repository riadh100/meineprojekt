/**
 * =====================================================
 * AI Empire Pro V8
 * OpenAI Service
 * Datei: server/services/openaiService.js
 * =====================================================
 */

const OpenAI = require("openai");

class OpenAIService {

    constructor() {

        this.client = new OpenAI({

            apiKey: process.env.OPENAI_API_KEY

        });

        this.model =

            process.env.OPENAI_MODEL ||

            "gpt-4.1";

    }

    async chat(messages, options = {}) {

        try {

            const response = await this.client.chat.completions.create({

                model: options.model || this.model,

                messages,

                temperature:

                    options.temperature ?? 0.7,

                max_tokens:

                    options.maxTokens ?? 2000

            });

            return {

                success: true,

                content:

                    response.choices[0].message.content,

                usage:

                    response.usage

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

    async completion(prompt) {

        return this.chat([

            {

                role: "user",

                content: prompt

            }

        ]);

    }

    async summarize(text) {

        return this.chat([

            {

                role: "system",

                content:

                    "Fasse den folgenden Text prägnant zusammen."

            },

            {

                role: "user",

                content: text

            }

        ]);

    }

    async translate(text, language = "Deutsch") {

        return this.chat([

            {

                role: "system",

                content:

                    `Übersetze den Text nach ${language}.`

            },

            {

                role: "user",

                content: text

            }

        ]);

    }

}

module.exports = new OpenAIService();
