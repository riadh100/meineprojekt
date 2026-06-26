/* ==========================================================
   AI Empire Pro V7 Ultimate
   File: script.js
   Version: V7 Ultimate
========================================================== */

"use strict";

/* ==========================================================
   APP
========================================================== */

const App = {

    version: "7.0 Ultimate",

    initialized: false,

    data: {

        empireScore: 0,

        level: 1,

        xp: 0,

        missions: [],

        projects: [],

        notifications: [],

        settings: {

            darkMode: true

        }

    }

};

/* ==========================================================
   DOM
========================================================== */

const DOM = {

    score: document.getElementById("empireScore"),

    level: document.getElementById("level"),

    missionCounter: document.getElementById("missionsDone"),

    projectCounter: document.getElementById("projectsCount"),

    notificationPanel: document.getElementById("notificationPanel"),

    notificationBtn: document.getElementById("notificationBtn"),

    themeBtn: document.getElementById("themeBtn"),

    fab: document.getElementById("fab"),

    aiPanel: document.getElementById("aiCommandCenter")

};

/* ==========================================================
   INIT
========================================================== */

document.addEventListener("DOMContentLoaded", initApp);

function initApp() {

    console.log("AI Empire Pro V7 gestartet");

    loadStorage();

    initNavigation();

    initTheme();

    initNotifications();

    updateDashboard();

    App.initialized = true;

}
