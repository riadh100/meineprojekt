/**
 * =====================================================
 * AI Empire Pro V8
 * Setup - Backup Manager
 * Datei: modules/setup/backup-manager.js
 * =====================================================
 */

const BackupManager = {

    init() {

        console.log("✔ Backup Manager gestartet.");

    },

    createBackup() {

        const backup = {

            version: "8.0.0",

            created: Utils.formatDate(),

            data: StateManager.getState()

        };

        localStorage.setItem(
            "AIEmpireProV8_Backup",
            JSON.stringify(backup)
        );

        StateManager.set(
            "setup.backup.lastBackup",
            backup.created
        );

        StorageManager.save();

        return backup;

    },

    restoreBackup() {

        const backup = localStorage.getItem(
            "AIEmpireProV8_Backup"
        );

        if (!backup) {

            console.error("Kein Backup gefunden.");

            return false;

        }

        try {

            const data = JSON.parse(backup);

            Object.assign(AppState, data.data);

            StorageManager.save();

            return true;

        } catch (error) {

            console.error(error);

            return false;

        }

    },

    exportBackup() {

        return JSON.stringify({

            version: "8.0.0",

            created: Utils.formatDate(),

            data: StateManager.getState()

        }, null, 2);

    },

    importBackup(json) {

        try {

            const backup = JSON.parse(json);

            Object.assign(AppState, backup.data);

            StorageManager.save();

            return true;

        } catch (error) {

            console.error(error);

            return false;

        }

    },

    deleteBackup() {

        localStorage.removeItem(
            "AIEmpireProV8_Backup"
        );

    }

};

window.BackupManager = BackupManager;
