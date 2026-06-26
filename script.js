/* =======================================================
   AI Empire Pro V7 Ultimate
   script.js
   Teil 1
======================================================= */

"use strict";

/* =======================================================
   App Initialisierung
======================================================= */

document.addEventListener("DOMContentLoaded", () => {

    console.log("AI Empire Pro V7 gestartet.");

    initGreeting();
    initClock();
    initNavigation();
    animateCounters();
    showWelcomeNotification();

});

/* =======================================================
   Begrüßung
======================================================= */

function initGreeting(){

    const heroTitle = document.querySelector(".hero-left h2");

    if(!heroTitle) return;

    const hour = new Date().getHours();

    let greeting = "Willkommen";

    if(hour >= 5 && hour < 12){

        greeting = "Guten Morgen ☀️";

    }else if(hour >= 12 && hour < 18){

        greeting = "Guten Tag 🌤️";

    }else{

        greeting = "Guten Abend 🌙";

    }

    heroTitle.textContent = greeting;

}

/* =======================================================
   Live Uhr
======================================================= */

function initClock(){

    const clock = document.createElement("div");

    clock.id = "liveClock";

    clock.style.fontWeight = "600";

    clock.style.fontSize = "15px";

    clock.style.color = "#60a5fa";

    const topbar = document.querySelector(".topbar-right");

    if(topbar){

        topbar.prepend(clock);

    }

    function updateClock(){

        const now = new Date();

        clock.textContent = now.toLocaleTimeString("de-DE");

    }

    updateClock();

    setInterval(updateClock,1000);

}

/* =======================================================
   Navigation
======================================================= */

function initNavigation(){

    const current = window.location.pathname.split("/").pop();

    document.querySelectorAll(".sidebar a").forEach(link=>{

        const href = link.getAttribute("href");

        if(href===current){

            link.parentElement.classList.add("active");

        }

    });

}

/* =======================================================
   Statistik Animation
======================================================= */

function animateCounters(){

    const counters=document.querySelectorAll(".number");

    counters.forEach(counter=>{

        const raw=counter.textContent;

        const target=parseInt(raw.replace(/\D/g,""));

        if(isNaN(target)) return;

        let value=0;

        const step=Math.max(1,Math.ceil(target/120));

        const timer=setInterval(()=>{

            value+=step;

            if(value>=target){

                value=target;

                clearInterval(timer);

            }

            if(raw.includes("€")){

                counter.textContent=
                "+"+
                value.toLocaleString("de-DE")+
                " €";

            }else{

                counter.textContent=value;

            }

        },15);

    });

}

/* =======================================================
   Benachrichtigung
======================================================= */

function showWelcomeNotification(){

    createNotification(

        "AI Empire Pro V7 erfolgreich gestartet.",

        "success"

    );

}

/* =======================================================
   Notification System
======================================================= */

function createNotification(message,type="info"){

    const note=document.createElement("div");

    note.className="toast "+type;

    note.textContent=message;

    note.style.position="fixed";

    note.style.right="25px";

    note.style.bottom="25px";

    note.style.padding="15px 20px";

    note.style.borderRadius="12px";

    note.style.zIndex="9999";

    note.style.color="#fff";

    note.style.fontWeight="600";

    note.style.boxShadow="0 12px 30px rgba(0,0,0,.35)";

    switch(type){

        case "success":
            note.style.background="#22c55e";
            break;

        case "error":
            note.style.background="#ef4444";
            break;

        case "warning":
            note.style.background="#f59e0b";
            break;

        default:
            note.style.background="#3b82f6";

    }

    document.body.appendChild(note);

    setTimeout(()=>{

        note.style.opacity="0";

        note.style.transition=".4s";

    },3000);

    setTimeout(()=>{

        note.remove();

    },3400);

}
/* =======================================================
   AI Empire Pro V7 Ultimate
   script.js
   Teil 2
======================================================= */

/* =======================================================
   Suchfunktion für Module
======================================================= */

function initSearch(){

    const search = document.querySelector(".search-box");

    if(!search) return;

    search.addEventListener("keyup",function(){

        const value = this.value.toLowerCase();

        const cards = document.querySelectorAll(".module-card");

        cards.forEach(card=>{

            const text = card.innerText.toLowerCase();

            if(text.includes(value)){

                card.style.display="block";

            }else{

                card.style.display="none";

            }

        });

    });

}

/* =======================================================
   Sidebar ein-/ausblenden
======================================================= */

function initSidebar(){

    const sidebar=document.querySelector(".sidebar");

    if(!sidebar) return;

    const button=document.createElement("button");

    button.innerHTML="☰";

    button.className="menu-button";

    document.body.appendChild(button);

    button.addEventListener("click",()=>{

        sidebar.classList.toggle("collapsed");

        localStorage.setItem(

            "sidebarCollapsed",

            sidebar.classList.contains("collapsed")

        );

    });

    const collapsed=

        localStorage.getItem("sidebarCollapsed");

    if(collapsed==="true"){

        sidebar.classList.add("collapsed");

    }

}

/* =======================================================
   Theme Vorbereitung
======================================================= */

function initTheme(){

    const saved=

        localStorage.getItem("theme");

    if(saved){

        document.body.dataset.theme=saved;

    }

}

/* =======================================================
   Theme wechseln
======================================================= */

function toggleTheme(){

    const current=

        document.body.dataset.theme==="light"

        ? "dark"

        : "light";

    document.body.dataset.theme=current;

    localStorage.setItem(

        "theme",

        current

    );

}

/* =======================================================
   Karten Hover Effekt
======================================================= */

function initCards(){

    const cards=document.querySelectorAll(

        ".module-card,.stat-card,.performance-card"

    );

    cards.forEach(card=>{

        card.addEventListener("mouseenter",()=>{

            card.style.transform="translateY(-8px) scale(1.02)";

        });

        card.addEventListener("mouseleave",()=>{

            card.style.transform="";

        });

    });

}

/* =======================================================
   Einstellungen speichern
======================================================= */

function saveSetting(key,value){

    localStorage.setItem(key,JSON.stringify(value));

}

function loadSetting(key){

    const data=localStorage.getItem(key);

    if(!data) return null;

    return JSON.parse(data);

}

/* =======================================================
   Dashboard Status merken
======================================================= */

function saveDashboardState(){

    saveSetting(

        "lastVisit",

        new Date().toLocaleString("de-DE")

    );

}

function showLastVisit(){

    const last=loadSetting("lastVisit");

    if(last){

        console.log("Letzter Besuch:",last);

    }

}

/* =======================================================
   Initialisierung Teil 2
======================================================= */

document.addEventListener("DOMContentLoaded",()=>{

    initSearch();

    initSidebar();

    initTheme();

    initCards();

    showLastVisit();

    saveDashboardState();

});
/* =======================================================
   AI Empire Pro V7 Ultimate
   script.js
   Teil 3
=======================================================*/

/* =======================================================
   Live System Status
======================================================= */

function initLiveStatus(){

    const bars=document.querySelectorAll(".progress-bar");

    if(!bars.length) return;

    setInterval(()=>{

        bars.forEach(bar=>{

            const value=Math.floor(Math.random()*35)+50;

            bar.style.width=value+"%";

            const label=bar.parentElement.nextElementSibling;

            if(label){

                label.textContent=value+"%";

            }

        });

    },5000);

}

/* =======================================================
   Live Aktivitätsfeed
======================================================= */

const liveEvents=[

    "Trading Signal empfangen",
    "Telegram Nachricht versendet",
    "KI Analyse abgeschlossen",
    "Video Rendering beendet",
    "Cloud Backup erfolgreich",
    "Neuer Benutzer angemeldet",
    "Portfolio aktualisiert",
    "Systemprüfung abgeschlossen"

];

function initActivityFeed(){

    const list=document.querySelector(".activity-card");

    if(!list) return;

    setInterval(()=>{

        const item=document.createElement("div");

        item.className="activity-item";

        const now=new Date().toLocaleTimeString("de-DE",{
            hour:"2-digit",
            minute:"2-digit"
        });

        const text=liveEvents[
            Math.floor(Math.random()*liveEvents.length)
        ];

        item.innerHTML=`
            <span class="activity-time">${now}</span>
            <span>${text}</span>
        `;

        list.prepend(item);

        while(list.children.length>8){

            list.removeChild(list.lastElementChild);

        }

    },8000);

}

/* =======================================================
   Dashboard Daten aktualisieren
======================================================= */

function refreshDashboard(){

    const numbers=document.querySelectorAll(".number");

    numbers.forEach(number=>{

        const current=parseInt(
            number.textContent.replace(/\D/g,"")
        );

        if(isNaN(current)) return;

        const next=current+Math.floor(Math.random()*5);

        if(number.textContent.includes("€")){

            number.textContent=
            "+"+next.toLocaleString("de-DE")+" €";

        }else{

            number.textContent=next;

        }

    });

}

/* =======================================================
   API Platzhalter
======================================================= */

const API={

    trading:null,

    telegram:null,

    assistant:null,

    video:null,

    game:null

};

function connectModules(){

    console.log("Trading API:",API.trading);

    console.log("Telegram API:",API.telegram);

    console.log("Assistant API:",API.assistant);

    console.log("Video API:",API.video);

    console.log("Game API:",API.game);

}

/* =======================================================
   Hilfsfunktionen
======================================================= */

function formatDate(){

    return new Date().toLocaleDateString("de-DE");

}

function formatTime(){

    return new Date().toLocaleTimeString("de-DE");

}

function random(min,max){

    return Math.floor(Math.random()*(max-min+1))+min;

}

/* =======================================================
   Dashboard Start
======================================================= */

function startDashboard(){

    initLiveStatus();

    initActivityFeed();

    connectModules();

    setInterval(refreshDashboard,10000);

    console.log("Dashboard gestartet.");

}

/* =======================================================
   Initialisierung Teil 3
======================================================= */

document.addEventListener("DOMContentLoaded",()=>{

    startDashboard();

});
