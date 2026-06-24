function login() {

const username = document.getElementById("username");

const password = document.getElementById("password");

if (!username || !password) {

return;

}

const user = username.value.trim();

const pass = password.value.trim();

if (user === "Riadh" && pass === "1234") {

window.location.href = "index.html";

} else {

alert("Falscher Benutzername oder Passwort");

}

}
