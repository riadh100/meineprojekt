/**
 * =====================================================
 * AI Empire Pro V8
 * Assistant Page
 * Datei: pages/assistant.js
 * =====================================================
 */

const AssistantPage = {

    render(containerId = "app") {

        const app = document.getElementById(containerId);

        if (!app) return;

        app.innerHTML = `

            <div class="page assistant-page">

                <div class="assistant-header">

                    <h1>AI Assistant</h1>

                </div>

                <div
                    id="assistant-chat"
                    class="assistant-chat">
                </div>

                <div class="assistant-input">

                    <textarea
                        id="assistant-message"
                        placeholder="Nachricht eingeben..."
                        rows="3">
                    </textarea>

                    <button id="assistant-send">

                        Senden

                    </button>

                </div>

            </div>

        `;

        this.renderMessages();

        document
            .getElementById("assistant-send")
            .addEventListener("click", () => {

                this.send();

            });

    },

    renderMessages() {

        const container = document.getElementById("assistant-chat");

        if (!container) return;

        const messages = ChatEngine.getMessages();

        container.innerHTML = "";

        messages.forEach(message => {

            container.innerHTML += `

                <div class="chat-message ${message.role}">

                    <strong>${message.role}</strong>

                    <p>${message.content}</p>

                    <small>${message.timestamp}</small>

                </div>

            `;

        });

        container.scrollTop = container.scrollHeight;

    },

    async send() {

        const input = document.getElementById("assistant-message");

        const text = input.value.trim();

        if (!text) return;

        ChatEngine.user(text);

        input.value = "";

        this.renderMessages();

        try {

            Loader.show("AI denkt...");

            const reply = await OpenAIAPI.ask(text);

            Loader.hide();

            Toast.success("Antwort erhalten");

            this.renderMessages();

        } catch (error) {

            Loader.hide();

            ChatEngine.assistant("API nicht verbunden.");

            Toast.error(error.message);

            this.renderMessages();

        }

    }

};

window.AssistantPage = AssistantPage;
