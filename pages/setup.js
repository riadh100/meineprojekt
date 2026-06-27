/**
 * =====================================================
 * AI Empire Pro V8
 * Setup Page
 * Datei: pages/setup.js
 * =====================================================
 */

const SetupPage = {

    render(containerId = "app") {

        const app = document.getElementById(containerId);

        if (!app) return;

        app.innerHTML = `

            <div class="page setup-page">

                <div class="page-header">

                    <h1>Einstellungen</h1>

                </div>

                <div class="dashboard-cards">

                    ${Card.create({
                        id: "profile-card",
                        title: "Benutzer",
                        value: ProfileManager.get().username || "Nicht gesetzt",
                        subtitle: "Profil",
                        icon: "👤"
                    })}

                    ${Card.create({
                        id: "security-card",
                        title: "2FA",
                        value: SecurityManager.get().twoFactor ? "Aktiv" : "Inaktiv",
                        subtitle: "Sicherheit",
                        icon: "🔒"
                    })}

                    ${Card.create({
                        id: "backup-card",
                        title: "Backup",
                        value: "Bereit",
                        subtitle: "Datensicherung",
                        icon: "💾"
                    })}

                    ${Card.create({
                        id: "system-card",
                        title: "Version",
                        value: SystemConfig.get("version"),
                        subtitle: "System",
                        icon: "⚙️"
                    })}

                </div>

                <h2>Benutzerprofil</h2>

                <div id="profile-table"></div>

                <h2>Sicherheit</h2>

                <div id="security-table"></div>

                <h2>System</h2>

                <div id="system-table"></div>

            </div>

        `;

        this.renderProfile();
        this.renderSecurity();
        this.renderSystem();

    },

    renderProfile() {

        const profile = ProfileManager.get();

        Table.render(

            "profile-table",

            ["Feld", "Wert"],

            [

                ["Benutzername", profile.username],

                ["E-Mail", profile.email],

                ["Rolle", profile.role],

                ["Avatar", profile.avatar]

            ]

        );

    },

    renderSecurity() {

        const security = SecurityManager.get();

        Table.render(

            "security-table",

            ["Option", "Status"],

            [

                ["2-Faktor", security.twoFactor ? "Aktiv" : "Inaktiv"],

                ["Auto Lock", security.autoLock ? "Aktiv" : "Inaktiv"],

                ["Session Timeout", security.sessionTimeout + " Min"],

                ["Login Hinweise", security.loginNotifications ? "Aktiv" : "Inaktiv"]

            ]

        );

    },

    renderSystem() {

        const config = SystemConfig.getAll();

        Table.render(

            "system-table",

            ["Einstellung", "Wert"],

            [

                ["App", config.appName],

                ["Version", config.version],

                ["Sprache", config.language],

                ["Theme", config.theme],

                ["Zeitzone", config.timezone],

                ["AutoSave", config.autoSave ? "Ja" : "Nein"]

            ]

        );

    }

};

window.SetupPage = SetupPage;
