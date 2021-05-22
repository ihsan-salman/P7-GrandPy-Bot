
let button = document.getElementById('button');

button.addEventListener("click", (event) =>{
  event.preventDefault();
  let text_input = document.getElementById('text_input');
  text_output.innerHTML += '</p>' + '<p id="text_output">' + text_input.value + '</p>';
  fetch('/ask?question='+text_input.value)
    .then(function(response){
      return response.json();
    })
    .then(function(data){
      console.log(data);
      let text_output = document.getElementById('text_output');
      let answer = document.getElementById('answer')
      let img = document.getElementById('img_gmap')
      wiki = data.wiki;
      console.log(wiki);
      answer.innerHTML += '</p>' + '<p id="answer">' + data.adress + '</p>' + '</br>';
      img.src = data.img_url;
    });
})
