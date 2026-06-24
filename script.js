function login() {

let username = document.getElementById("username").value;

let password = document.getElementById("password").value;

if(username === "Riadh" && password === "1234"){

window.location.href = "index.html";

}else{

alert("Benutzername oder Passwort falsch");

}

}
