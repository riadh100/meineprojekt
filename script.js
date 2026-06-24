function addTask() {

const input = document.getElementById("taskInput");

const task = input.value.trim();

if(task === "") return;

const list = document.getElementById("taskList");

const li = document.createElement("li");

li.innerHTML = `
<input type="checkbox">
<span>${task}</span>
`;

list.appendChild(li);

input.value = "";

}
