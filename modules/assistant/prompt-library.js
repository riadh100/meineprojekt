/**
 * =====================================================
 * AI Empire Pro V8
 * Assistant - Prompt Library
 * Datei: modules/assistant/prompt-library.js
 * =====================================================
 */

const PromptLibrary = {

    prompts: [],

    init() {

        this.load();

        console.log("✔ Prompt Library geladen.");

    },

    add(title, category, content) {

        const prompt = {

            id: Utils.uuid(),

            title: title,

            category: category,

            content: content,

            created: Utils.formatDate()

        };

        this.prompts.push(prompt);

        this.save();

        return prompt;

    },

    update(id, data) {

        const prompt = this.prompts.find(
            item => item.id === id
        );

        if (!prompt) return false;

        Object.assign(prompt, data);

        this.save();

        return true;

    },

    remove(id) {

        this.prompts = this.prompts.filter(
            item => item.id !== id
        );

        this.save();

    },

    get(id) {

        return this.prompts.find(
            item => item.id === id
        );

    },

    getAll() {

        return this.prompts;

    },

    search(keyword) {

        keyword = keyword.toLowerCase();

        return this.prompts.filter(prompt =>

            prompt.title.toLowerCase().includes(keyword) ||

            prompt.category.toLowerCase().includes(keyword) ||

            prompt.content.toLowerCase().includes(keyword)

        );

    },

    clear() {

        this.prompts = [];

        this.save();

    },

    save() {

        StateManager.set(
            "assistant.promptLibrary",
            this.prompts
        );

        StorageManager.save();

    },

    load() {

        const data = StateManager.get(
            "assistant.promptLibrary"
        );

        if (Array.isArray(data)) {

            this.prompts = data;

        }

    }

};

window.PromptLibrary = PromptLibrary;
