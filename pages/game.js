/**
 * =====================================================
 * AI Empire Pro V8
 * Game Page
 * Datei: pages/game.js
 * =====================================================
 */

const GamePage = {

    render(containerId = "app") {

        const app = document.getElementById(containerId);

        if (!app) return;

        app.innerHTML = `

            <div class="page game-page">

                <div class="page-header">

                    <h1>Game Hub</h1>

                </div>

                <div class="dashboard-cards">

                    ${Card.create({
                        id: "game-level",
                        title: "Level",
                        value: XPEngine.getLevel(),
                        subtitle: "Aktuelles Level",
                        icon: "🏆"
                    })}

                    ${Card.create({
                        id: "game-xp",
                        title: "XP",
                        value: XPEngine.getXP(),
                        subtitle: XPEngine.getProgress() + "% Fortschritt",
                        icon: "⭐"
                    })}

                    ${Card.create({
                        id: "game-achievements",
                        title: "Achievements",
                        value: AchievementSystem.getUnlocked().length,
                        subtitle: "Freigeschaltet",
                        icon: "🎖️"
                    })}

                </div>

                <h2>Daily Missions</h2>
                <div id="missions-table"></div>

                <h2>Achievements</h2>
                <div id="achievements-table"></div>

                <h2>Rewards</h2>
                <div id="rewards-table"></div>

            </div>

        `;

        this.renderMissions();
        this.renderAchievements();
        this.renderRewards();

    },

    renderMissions() {

        const rows = DailyMissions.getAll().map(mission => [
            mission.title,
            mission.rewardXP,
            mission.completed ? "Erledigt" : "Offen",
            mission.created
        ]);

        Table.render(
            "missions-table",
            ["Mission", "XP", "Status", "Erstellt"],
            rows
        );

    },

    renderAchievements() {

        const rows = AchievementSystem.getAll().map(item => [
            item.title,
            item.xp,
            item.unlocked ? "Freigeschaltet" : "Gesperrt",
            item.created
        ]);

        Table.render(
            "achievements-table",
            ["Achievement", "XP", "Status", "Erstellt"],
            rows
        );

    },

    renderRewards() {

        const rows = Rewards.getAll().map(reward => [
            reward.title,
            reward.cost,
            reward.claimed ? "Eingelöst" : "Verfügbar",
            reward.created
        ]);

        Table.render(
            "rewards-table",
            ["Belohnung", "Kosten", "Status", "Erstellt"],
            rows
        );

    }

};

window.GamePage = GamePage;
