/**
 * =====================================================
 * AI Empire Pro V8
 * Task Manager
 * Datei: assets/js/task-manager.js
 * =====================================================
 */

const TaskManager = {

    tasks: [],

    init() {

        this.load();

        Logger.success("Task Manager gestartet.");

    },

    create(title, description = "", priority = "normal") {

        const task = {

            id: Helpers.uuid(),

            title,

            description,

            priority,

            status: "open",

            created: new Date().toISOString(),

            completed: null

        };

        this.tasks.unshift(task);

        this.save();

        NotificationCenter.success(

            "Neue Aufgabe",

            title

        );

        return task;

    },

    complete(id) {

        const task = this.tasks.find(

            t => t.id === id

        );

        if (!task) return;

        task.status = "completed";

        task.completed = new Date().toISOString();

        this.save();

        Logger.success(

            `Aufgabe erledigt: ${task.title}`

        );

    },

    reopen(id) {

        const task = this.tasks.find(

            t => t.id === id

        );

        if (!task) return;

        task.status = "open";

        task.completed = null;

        this.save();

    },

    remove(id) {

        this.tasks = this.tasks.filter(

            task => task.id !== id

        );

        this.save();

    },

    getAll() {

        return this.tasks;

    },

    getOpen() {

        return this.tasks.filter(

            task => task.status === "open"

        );

    },

    getCompleted() {

        return this.tasks.filter(

            task => task.status === "completed"

        );

    },

    save() {

        localStorage.setItem(

            "tasks",

            JSON.stringify(this.tasks)

        );

    },

    load() {

        const data = localStorage.getItem("tasks");

        if (!data) return;

        try {

            this.tasks = JSON.parse(data);

        }

        catch {

            this.tasks = [];

        }

    }

};

window.TaskManager = TaskManager;
