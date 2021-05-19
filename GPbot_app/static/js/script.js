
let button = document.getElementById('button');
let an = document.createElement('p');
an.id = 'an';

button.addEventListener("click", (event) =>{
  event.preventDefault();
  let text_input = document.getElementById('text_input');
  fetch('/ask?question='+text_input.value)
    .then(function(response){
      return response.json();
    })
    .then(function(data){
      console.log(data);
      let text_output = document.getElementById('text_output');
      text_output.innerHTML += text_input.value + '</br>';
      document.body.appendChild(an);
    });
})
