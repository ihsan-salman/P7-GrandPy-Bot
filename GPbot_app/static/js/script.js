
let message = document.createElement('p');
message.id = "text_output";
document.getElementById('discussion').appendChild(message);

let button = document.getElementById('button')
let myRequest = new Request('http://127.0.0.1:5000/');


button.addEventListener("click", () =>{
  let text_input = document.getElementById('text_input');
  let text_output = document.getElementById('text_output');
  text_output.innerText = text_input.value;
  text_input.value = '';
  let init = {method: 'POST'}
  let request = fetch('/', init);
  request
    .then(function(response){
      console.log(response);
    });
  event.preventDefault();
})
