
let message = document.createElement('p');
message.id = "text_output";
document.getElementById('discussion').appendChild(message);


let button = document.getElementById('button')
let myRequest = new Request('http://127.0.0.1:5000/');


button.addEventListener("click", () =>{
  let text_input = document.getElementById('text_input');
  console.log(text_input);
  let text_output = document.getElementById('text_output');
  text_output.innerText = text_input.value;
  gngn = text_output.value;
  fetch('/')
      .then(function (response) {
          console.log()
      })
})