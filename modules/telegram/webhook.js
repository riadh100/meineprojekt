/**
 * =====================================================
 * AI Empire Pro V8
 * Telegram - Webhook Manager
 * Datei: modules/telegram/webhook.js
 * =====================================================
 */

const WebhookManager = {

    url: "",

    enabled: false,

    lastUpdate: null,

    setUrl(url) {

        this.url = url;

        this.save();

    },

    getUrl() {

        return this.url;

    },

    enable() {

        this.enabled = true;

        this.lastUpdate = Utils.formatDate();

        this.save();

    },

    disable() {

        this.enabled = false;

        this.lastUpdate = Utils.formatDate();

        this.save();

    },

    isEnabled() {

        return this.enabled;

    },

    async test() {

        if (!this.url) {

            console.error("Keine Webhook-URL gesetzt.");

            return false;

        }

        try {

            const response = await fetch(this.url, {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    event: "test",

                    timestamp: Date.now()

                })

            });

            return response.ok;

        } catch (error) {

            console.error(error);

            return false;

        }

    },

    save() {

        StateManager.set("telegram.webhook", {

            url: this.url,

            enabled: this.enabled,

            lastUpdate: this.lastUpdate

        });

        StorageManager.save();

    },

    load() {

        const data = StateManager.get("telegram.webhook");

        if (!data) return;

        this.url = data.url || "";

        this.enabled = data.enabled || false;

        this.lastUpdate = data.lastUpdate || null;

    }

};

window.WebhookManager = WebhookManager;
