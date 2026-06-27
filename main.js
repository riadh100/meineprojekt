/**
 * =====================================================
 * AI Empire Pro V8
 * Main Application
 * Datei: main.js
 * =====================================================
 */

document.addEventListener("DOMContentLoaded", () => {

    console.log("==========================================");
    console.log("AI Empire Pro V8");
    console.log("Initialisierung...");
    console.log("==========================================");

    /* Core */

    App.init();

    ThemeManager.init();

    SettingsManager.init();

    /* Module */

    Dashboard.init();

    DashboardKPI.init();

    DashboardActivity.init();

    DashboardMissions.init();

    Assistant.init();

    PromptLibrary.init();

    ConversationHistory.init();

    Trading.init();

    Portfolio.init();

    SignalEngine.init();

    TradeHistory.init();

    Telegram.init();

    BotManager.init();

    BroadcastSystem.init();

    WebhookManager.load();

    Video.init();

    ProjectManager.init();

    RenderQueue.init();

    ExportManager.init();

    Game.init();

    XPEngine.init();

    AchievementSystem.init();

    DailyMissions.init();

    Rewards.init();

    Tools.init();

    APIManager.init();

    LogManager.init();

    DebugCenter.init();

    Setup.init();

    ProfileManager.init();

    SecurityManager.init();

    BackupManager.init();

    SystemConfig.init();

    /* UI */

    Sidebar.render();

    Navbar.render();

    PageRouter.init();

    Toast.success("AI Empire Pro V8 gestartet");

    console.log("==========================================");
    console.log("System bereit");
    console.log("==========================================");

});
