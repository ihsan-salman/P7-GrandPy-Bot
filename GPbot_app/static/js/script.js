
let message = document.createElement('p');
message.id = "text_output";
document.getElementById('discussion').appendChild(message);


let button = document.getElementById('button')

button.addEventListener("click", () =>{
  let text_input = document.getElementById('text_input');
  console.log(text_input);
  let text_output = document.getElementById('text_output');
  text_output.innerText = text_input.value;
  text_input.value = "";
  console.log(text_input)

})

