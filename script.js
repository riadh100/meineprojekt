function addTask(){

const input=document.getElementById("taskInput");

const text=input.value.trim();

if(text==="") return;

const list=document.getElementById("taskList");

const li=document.createElement("li");

li.innerHTML="✅ "+text;

list.appendChild(li);

input.value="";

}
