/**
 * =====================================================
 * AI Empire Pro V8
 * Global Events
 * Datei: assets/js/events.js
 * =====================================================
 */

const Events = {

    init() {

        this.keyboard();

        this.window();

        this.buttons();

        console.log("✔ Events initialisiert.");

    },

    keyboard() {

        document.addEventListener("keydown", (event) => {

            switch (event.key) {

                case "Escape":

                    if (Modal.isOpen()) {

                        Modal.close();

                    }

                    if (Dialog.isOpen()) {

                        Dialog.close();

                    }

                    break;

                case "F5":

                    event.preventDefault();

                    PageRouter.reload();

                    Toast.info("Seite aktualisiert");

                    break;

            }

        });

    },

    window() {

        window.addEventListener("resize", () => {

            console.log(

                "Fenster:",

                window.innerWidth,

                "x",

                window.innerHeight

            );

        });

        window.addEventListener("beforeunload", () => {

            if (typeof StorageManager !== "undefined") {

                StorageManager.save();

            }

        });

    },

    buttons() {

        document.addEventListener("click", (event) => {

            const button = event.target.closest("[data-action]");

            if (!button) return;

            const action = button.dataset.action;

            switch (action) {

                case "refresh":

                    PageRouter.reload();

                    Toast.success("Aktualisiert");

                    break;

                case "theme":

                    ThemeManager.toggle();

                    break;

                case "backup":

                    BackupManager.createBackup();

                    Toast.success("Backup erstellt");

                    break;

                case "logout":

                    Dialog.confirm(

                        "Abmelden",

                        "Möchtest du dich wirklich abmelden?",

                        () => {

                            location.reload();

                        }

                    );

                    break;

                default:

                    console.warn(

                        "Unbekannte Aktion:",

                        action

                    );

            }

        });

    }

};

window.Events = Events;
