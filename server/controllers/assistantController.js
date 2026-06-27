/**
 * =====================================================
 * AI Empire Pro V8
 * Assistant Controller
 * Datei: server/controllers/assistantController.js
 * =====================================================
 */

const OpenAI = require("openai");
const Conversation = require("../models/Conversation");

const client = new OpenAI({

    apiKey: process.env.OPENAI_API_KEY

});

class AssistantController {

    async chat(req, res) {

        try {

            const {

                prompt,

                conversationId

            } = req.body;

            if (!prompt) {

                return res.status(400).json({

                    success: false,

                    message: "Prompt fehlt."

                });

            }

            const response = await client.chat.completions.create({

                model: process.env.OPENAI_MODEL || "gpt-4.1",

                messages: [

                    {

                        role: "system",

                        content:
                            "Du bist AI Empire Pro, ein intelligenter Business-, Trading- und Automatisierungs-Assistent."

                    },

                    {

                        role: "user",

                        content: prompt

                    }

                ],

                temperature: 0.7

            });

            const answer = response.choices[0].message.content;

            let conversation = null;

            if (conversationId) {

                conversation = await Conversation.findById(conversationId);

            }

            if (!conversation) {

                conversation = await Conversation.create({

                    title: prompt.substring(0, 40),

                    messages: []

                });

            }

            conversation.messages.push({

                role: "user",

                content: prompt,

                createdAt: new Date()

            });

            conversation.messages.push({

                role: "assistant",

                content: answer,

                createdAt: new Date()

            });

            await conversation.save();

            return res.json({

                success: true,

                conversationId: conversation._id,

                answer

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "OpenAI-Anfrage fehlgeschlagen."

            });

        }

    }

    async history(req, res) {

        try {

            const conversations = await Conversation.find()

                .sort({

                    updatedAt: -1

                })

                .limit(50);

            return res.json({

                success: true,

                conversations

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Verlauf konnte nicht geladen werden."

            });

        }

    }

    async conversation(req, res) {

        try {

            const conversation = await Conversation.findById(

                req.params.id

            );

            if (!conversation) {

                return res.status(404).json({

                    success: false,

                    message: "Konversation nicht gefunden."

                });

            }

            return res.json({

                success: true,

                conversation

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Konversation konnte nicht geladen werden."

            });

        }

    }

}

module.exports = new AssistantController();
