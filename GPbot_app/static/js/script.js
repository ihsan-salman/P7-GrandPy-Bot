
let button = document.getElementById('button');

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
      let answer = document.getElementById('answer')
      wiki = data.wiki;
      console.log(wiki);
      text_output.innerHTML += text_input.value + '</br>';
      //answer.innerHTML += '</br>' + wiki;
    });
})
