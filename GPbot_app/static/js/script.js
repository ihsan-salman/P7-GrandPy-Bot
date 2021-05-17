
let button = document.getElementById('button')

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
    });
  fetch('/answer')
    .then(function(data){
      console.log(data);
      let answer = document.getElementById('answer');
    })
})
