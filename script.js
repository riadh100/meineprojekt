function login(){

const username=document.getElementById("username").value;

const password=document.getElementById("password").value;

if(username==="Riadh" && password==="1234"){

window.location.href="index.html";

}

else{

alert("Falsche Anmeldedaten");

}

}
