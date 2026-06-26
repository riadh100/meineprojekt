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
/* ==========================================================
   NAVIGATION
========================================================== */

function initNavigation() {

    const links = document.querySelectorAll(".sidebar a");

    links.forEach(link => {

        link.addEventListener("click", function(e){

            e.preventDefault();

            const target = this.getAttribute("href");

            const section = document.querySelector(target);

            if(section){

                section.scrollIntoView({

                    behavior:"smooth"

                });

            }

        });

    });

}
/* ==========================================================
   DASHBOARD
========================================================== */

function updateDashboard(){

    if(DOM.score){

        DOM.score.textContent = App.data.empireScore;

    }

    if(DOM.level){

        DOM.level.textContent = App.data.level;

    }

    if(DOM.missionCounter){

        DOM.missionCounter.textContent =
        App.data.missions.length;

    }

    if(DOM.projectCounter){

        DOM.projectCounter.textContent =
        App.data.projects.length;

    }

}
/* ==========================================================
   STORAGE
========================================================== */

function saveStorage(){

    localStorage.setItem(

        "AI_EMPIRE_V7",

        JSON.stringify(App.data)

    );

}

function loadStorage(){

    const data = localStorage.getItem("AI_EMPIRE_V7");

    if(data){

        App.data = JSON.parse(data);

    }

}
/* ==========================================================
   THEME
========================================================== */

function initTheme(){

    if(!DOM.themeBtn) return;

    DOM.themeBtn.addEventListener("click",toggleTheme);

}

function toggleTheme(){

    document.body.classList.toggle("light");

    saveStorage();

}
/* ==========================================================
   NOTIFICATIONS
========================================================== */

function initNotifications(){

    if(!DOM.notificationBtn) return;

    DOM.notificationBtn.addEventListener(

        "click",

        toggleNotifications

    );

}

function toggleNotifications(){

    DOM.notificationPanel.classList.toggle("active");

}

function addNotification(title,text){

    App.data.notifications.push({

        title,

        text,

        date:new Date()

    });

    saveStorage();

}
/* ==========================================================
   AI PANEL
========================================================== */

if(DOM.fab){

    DOM.fab.addEventListener("click",()=>{

        DOM.aiPanel.classList.toggle("active");

    });

}
