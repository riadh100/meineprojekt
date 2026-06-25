/* =======================================
   AI EMPIRE PRO V5 PREMIUM
   Riadh Edition
======================================= */

/* CLOCK */

function updateClock(){

    const now = new Date();

    const time =
        now.toLocaleTimeString(
            "de-DE"
        );

    const clock =
        document.getElementById(
            "clock"
        );

    if(clock){

        clock.innerHTML = time;

    }

}

setInterval(
    updateClock,
    1000
);

updateClock();

/* NOTES SYSTEM */

function saveNote(
    key,
    elementId
){

    const element =
        document.getElementById(
            elementId
        );

    if(!element) return;

    localStorage.setItem(
        key,
        element.value
    );

    showNotification(
        "Gespeichert: " + key
    );

}

function loadNote(
    key,
    elementId
){

    const element =
        document.getElementById(
            elementId
        );

    if(!element) return;

    const saved =
        localStorage.getItem(
            key
        );

    if(saved){

        element.value = saved;

    }

}

/* LOGOUT */

function logout(){

    const confirmLogout =
        confirm(
            "Wirklich ausloggen?"
        );

    if(confirmLogout){

        window.location.href =
            "login.html";

    }

}

/* ONLINE MODULES */

function getOnlineModules(){

    return 8;

}

/* NOTIFICATION SYSTEM */

function showNotification(
    message
){

    const old =
        document.getElementById(
            "empireNotification"
        );

    if(old){

        old.remove();

    }

    const notification =
        document.createElement(
            "div"
        );

    notification.id =
        "empireNotification";

    notification.innerHTML =
        message;

    notification.style.position =
        "fixed";

    notification.style.top =
        "20px";

    notification.style.right =
        "20px";

    notification.style.zIndex =
        "99999";

    notification.style.padding =
        "15px 20px";

    notification.style.background =
        "#d4af37";

    notification.style.color =
        "#000";

    notification.style.fontWeight =
        "bold";

    notification.style.borderRadius =
        "10px";

    notification.style.boxShadow =
        "0 0 20px rgba(212,175,55,0.4)";

    document.body.appendChild(
        notification
    );

    setTimeout(function(){

        notification.remove();

    },2500);

}

/* STORAGE INFO */

function getStorageCount(){

    return localStorage.length;

}

/* STORAGE SIZE */

function getStorageSize(){

    let total = 0;

    for(
        let key in localStorage
    ){

        if(
            localStorage.hasOwnProperty(
                key
            )
        ){

            total +=
                localStorage[key]
                .length;

        }

    }

    return (
        total / 1024
    ).toFixed(2);

}

/* SYSTEM INFO */

function getSystemInfo(){

    return {

        version:
            "V5 Premium",

        edition:
            "Riadh Edition",

        modules:
            8,

        storage:
            getStorageCount(),

        size:
            getStorageSize() + " KB"

    };

}

/* DASHBOARD ACTIVITY */

function addActivity(
    text
){

    const feed =
        document.getElementById(
            "activityFeed"
        );

    if(!feed) return;

    const item =
        document.createElement(
            "div"
        );

    item.className =
        "item";

    item.innerHTML =
        "<span>" +
        text +
        "</span><span class='online'>OK</span>";

    feed.prepend(
        item
    );

}

/* AUTO SAVE */

function enableAutoSave(
    key,
    elementId
){

    const element =
        document.getElementById(
            elementId
        );

    if(!element) return;

    element.addEventListener(
        "keyup",
        function(){

            localStorage.setItem(
                key,
                element.value
            );

        }
    );

}

/* RANDOM SYSTEM VALUES */

function randomCpu(){

    return Math.floor(
        Math.random() * 40
    ) + 20;

}

function randomMemory(){

    return Math.floor(
        Math.random() * 30
    ) + 50;

}

/* EXPORT DATA */

function exportEmpireData(){

    const data =
        JSON.stringify(
            localStorage,
            null,
            2
        );

    const blob =
        new Blob(
            [data],
            {
                type:
                "application/json"
            }
        );

    const link =
        document.createElement(
            "a"
        );

    link.href =
        URL.createObjectURL(
            blob
        );

    link.download =
        "ai-empire-pro-backup.json";

    link.click();

}

/* IMPORT DATA */

function importEmpireData(
    file
){

    const reader =
        new FileReader();

    reader.onload =
        function(event){

        const data =
            JSON.parse(
                event.target.result
            );

        Object.keys(data)
        .forEach(function(key){

            localStorage.setItem(
                key,
                data[key]
            );

        });

        showNotification(
            "Backup importiert"
        );

        setTimeout(
            function(){

                location.reload();

            },
            1000
        );

    };

    reader.readAsText(
        file
    );

}

/* WELCOME MESSAGE */

window.addEventListener(
    "load",
    function(){

    const user =
        localStorage.getItem(
            "empire_user"
        );

    if(user){

        console.log(
            "AI Empire Pro geladen: " +
            user
        );

    }

});

/* KEYBOARD SHORTCUTS */

document.addEventListener(
    "keydown",
    function(event){

    if(
        event.ctrlKey &&
        event.key === "s"
    ){

        event.preventDefault();

        showNotification(
            "Auto Save aktiviert"
        );

    }

});

/* AI GREETING */

function getGreeting(){

    const hour =
        new Date().getHours();

    if(hour < 12){

        return "Guten Morgen 👑";

    }

    if(hour < 18){

        return "Guten Tag 👑";

    }

    return "Guten Abend 👑";

}

/* STARTUP LOG */

console.log(
    "AI Empire Pro V5 Premium gestartet"
);

console.log(
    "Riadh Edition aktiv"
);
