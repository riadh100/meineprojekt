/**
 * =====================================================
 * AI Empire Pro V8
 * Assistant - OpenAI API
 * Datei: modules/assistant/openai-api.js
 * =====================================================
 */

const OpenAIAPI = {

    apiKey: "",

    model: "gpt-4.1",

    endpoint: "https://api.openai.com/v1/chat/completions",

    setApiKey(key) {

        this.apiKey = key;

        StateManager.set("tools.apiKeys.openai", key);

        StorageManager.save();

    },

    getApiKey() {

        return this.apiKey ||
            StateManager.get("tools.apiKeys.openai") ||
            "";

    },

    async send(messages = []) {

        const key = this.getApiKey();

        if (!key) {

            throw new Error("OpenAI API Key fehlt.");

        }

        const response = await fetch(this.endpoint, {

            method: "POST",

            headers: {

                "Content-Type": "application/json",

                "Authorization": `Bearer ${key}`

            },

            body: JSON.stringify({

                model: this.model,

                messages: messages

            })

        });

        if (!response.ok) {

            throw new Error("API Fehler: " + response.status);

        }

        const data = await response.json();

        return data.choices[0].message.content;

    },

    async ask(prompt) {

        const reply = await this.send([

            {

                role: "user",

                content: prompt

            }

        ]);

        ChatEngine.user(prompt);

        ChatEngine.assistant(reply);

        return reply;

    }

};

window.OpenAIAPI = OpenAIAPI;
