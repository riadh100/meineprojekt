//////////////////////////////////////////////////////
// AI EMPIRE PRO V6 ULTIMATE - SCRIPT ENGINE
// Riadh Edition
//////////////////////////////////////////////////////

/* =========================
   CLOCK SYSTEM
========================= */

function updateClock(){

    const now = new Date();

    const h = String(now.getHours()).padStart(2,"0");
    const m = String(now.getMinutes()).padStart(2,"0");
    const s = String(now.getSeconds()).padStart(2,"0");

    const clock = document.getElementById("clock");
    if(clock){
        clock.innerText = `${h}:${m}:${s}`;
    }
}

setInterval(updateClock,1000);
updateClock();


/* =========================
   NOTIFICATION SYSTEM
========================= */

function showNotification(message){

    let note = document.createElement("div");

    note.innerText = message;

    note.style.position = "fixed";
    note.style.bottom = "20px";
    note.style.right = "20px";
    note.style.background = "#d4af37";
    note.style.color = "#000";
    note.style.padding = "12px 18px";
    note.style.borderRadius = "12px";
    note.style.fontWeight = "bold";
    note.style.zIndex = "9999";
    note.style.boxShadow = "0 0 20px rgba(212,175,55,0.4)";

    document.body.appendChild(note);

    setTimeout(()=>{
        note.remove();
    },2500);
}


/* =========================
   NOTE SYSTEM (LOCAL STORAGE)
========================= */

function saveNote(key, id){

    const el = document.getElementById(id);
    if(!el) return;

    localStorage.setItem(key, el.value);

    showNotification("Gespeichert ✔");
}

function loadNote(key, id){

    const el = document.getElementById(id);
    if(!el) return;

    const data = localStorage.getItem(key);

    if(data){
        el.value = data;
    }
}


/* =========================
   BACKUP SYSTEM
========================= */

function exportEmpireData(){

    const data = {
        ...localStorage
    };

    const blob = new Blob(
        [JSON.stringify(data,null,2)],
        {type:"application/json"}
    );

    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "AI_Empire_Backup_V6.json";
    a.click();

    URL.revokeObjectURL(url);

    showNotification("Backup exportiert ✔");
}

function importEmpireData(file){

    const reader = new FileReader();

    reader.onload = function(e){

        try{

            const data = JSON.parse(e.target.result);

            Object.keys(data).forEach(key=>{
                localStorage.setItem(key,data[key]);
            });

            showNotification("Backup importiert ✔");
            setTimeout(()=>location.reload(),1200);

        } catch(err){
            showNotification("Fehler beim Import ❌");
        }
    };

    reader.readAsText(file);
}


/* =========================
   BASIC UTIL
========================= */

function random(min,max){
    return Math.floor(Math.random()*(max-min+1))+min;
}

function formatEUR(value){
    return Number(value).toFixed(2) + " €";
}


/* =========================
   AUTO INIT
========================= */

document.addEventListener("DOMContentLoaded",()=>{

    updateClock();

});
