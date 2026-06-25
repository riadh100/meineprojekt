/* ==================================================
   AI EMPIRE PRO
   UNIFIED SCRIPT V4
   RIADH EDITION
================================================== */

/* ==================================================
   LIVE CLOCK
================================================== */

function startClock() {

    const clockElement =
    document.getElementById("clock");

    if (!clockElement) return;

    function updateClock() {

        const now = new Date();

        clockElement.innerHTML =
        now.toLocaleTimeString("de-DE");

    }

    updateClock();

    setInterval(updateClock, 1000);

}

/* ==================================================
   LOGOUT
================================================== */

function logout() {

    const confirmLogout =
    confirm("Wirklich ausloggen?");

    if(confirmLogout){

        window.location.href =
        "login.html";

    }

}

/* ==================================================
   NOTIFICATION SYSTEM
================================================== */

function showNotification(message) {

    const notification =
    document.createElement("div");

    notification.innerHTML =
    message;

    notification.style.position =
    "fixed";

    notification.style.top =
    "20px";

    notification.style.right =
    "20px";

    notification.style.padding =
    "15px 20px";

    notification.style.background =
    "#FFD700";

    notification.style.color =
    "#000";

    notification.style.borderRadius =
    "10px";

    notification.style.fontWeight =
    "bold";

    notification.style.zIndex =
    "9999";

    document.body.appendChild(
        notification
    );

    setTimeout(() => {

        notification.remove();

    }, 3000);

}

/* ==================================================
   NOTES SYSTEM
================================================== */

function saveNote(storageKey, elementId) {

    const element =
    document.getElementById(elementId);

    if(!element) return;

    localStorage.setItem(
        storageKey,
        element.value
    );

    showNotification(
        "Notiz gespeichert"
    );

}

function loadNote(storageKey, elementId) {

    const element =
    document.getElementById(elementId);

    if(!element) return;

    const saved =
    localStorage.getItem(storageKey);

    if(saved){

        element.value = saved;

    }

}

/* ==================================================
   STORAGE HELPER
================================================== */

function saveData(key, data){

    localStorage.setItem(
        key,
        JSON.stringify(data)
    );

}

function loadData(key){

    const data =
    localStorage.getItem(key);

    if(!data) return null;

    return JSON.parse(data);

}

function removeData(key){

    localStorage.removeItem(key);

}

/* ==================================================
   MODULE STATUS
================================================== */

const empireModules = {

    dashboard : true,
    assistant : true,
    trading : true,
    telegram : true,
    video : true,
    game : true,
    tools : true,
    setup : true

};

function getOnlineModules(){

    return Object.values(
        empireModules
    ).filter(Boolean).length;

}

function getModuleStatus(name){

    return empireModules[name]
    ? "ONLINE"
    : "OFFLINE";

}

/* ==================================================
   QUICK NAVIGATION
================================================== */

function openModule(page){

    window.location.href = page;

}

/* ==================================================
   USER PROFILE
================================================== */

const defaultProfile = {

    name : "Riadh",
    edition : "AI Empire Pro",
    level : "PRO"

};

function getProfile(){

    return loadData(
        "aiempire_profile"
    ) || defaultProfile;

}

function saveProfile(profile){

    saveData(
        "aiempire_profile",
        profile
    );

}

/* ==================================================
   ACTIVITY LOG
================================================== */

function addActivity(text){

    let activities =
    loadData(
        "aiempire_activity"
    ) || [];

    activities.unshift({

        text:text,

        time:
        new Date().toLocaleString("de-DE")

    });

    activities =
    activities.slice(0,50);

    saveData(
        "aiempire_activity",
        activities
    );

}

function getActivities(){

    return loadData(
        "aiempire_activity"
    ) || [];

}

/* ==================================================
   AI CHAT STORAGE
================================================== */

function saveChat(chatHtml){

    localStorage.setItem(
        "yasin_ai_chat",
        chatHtml
    );

}

function loadChat(){

    return localStorage.getItem(
        "yasin_ai_chat"
    );

}

function clearChat(){

    if(confirm(
        "Chat wirklich löschen?"
    )){

        localStorage.removeItem(
            "yasin_ai_chat"
        );

        location.reload();

    }

}

/* ==================================================
   IDEA GENERATOR
================================================== */

function getRandomIdea(array){

    return array[
        Math.floor(
            Math.random() *
            array.length
        )
    ];

}

/* ==================================================
   SYSTEM INFO
================================================== */

function getSystemInfo(){

    return {

        version : "V4",

        project :
        "AI Empire Pro",

        edition :
        "Riadh Edition",

        modules :
        getOnlineModules(),

        date :
        new Date()
        .toLocaleDateString("de-DE")

    };

}

/* ==================================================
   DASHBOARD COUNTERS
================================================== */

function updateCounter(
    elementId,
    value
){

    const element =
    document.getElementById(
        elementId
    );

    if(element){

        element.innerHTML =
        value;

    }

}

/* ==================================================
   EXPORT ALL NOTES
================================================== */

function exportNotes(){

    const data = {

        dashboard :
        localStorage.getItem(
        "aiempire_notes"
        ),

        trading :
        localStorage.getItem(
        "trading_notes"
        ),

        telegram :
        localStorage.getItem(
        "telegram_notes"
        ),

        video :
        localStorage.getItem(
        "video_notes"
        ),

        game :
        localStorage.getItem(
        "game_notes"
        ),

        setup :
        localStorage.getItem(
        "setup_admin_notes"
        )

    };

    const blob =
    new Blob(

        [
            JSON.stringify(
                data,
                null,
                2
            )
        ],

        {
            type:
            "application/json"
        }

    );

    const url =
    URL.createObjectURL(blob);

    const a =
    document.createElement("a");

    a.href = url;

    a.download =
    "ai-empire-backup.json";

    a.click();

    URL.revokeObjectURL(url);

}

/* ==================================================
   APP STARTUP
================================================== */

document.addEventListener(
    "DOMContentLoaded",
    function(){

        startClock();

        console.log(
        "AI Empire Pro V4 gestartet"
        );

    }
);
