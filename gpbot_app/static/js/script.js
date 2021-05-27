let button = document.getElementById('button');
let papy_sentences = ["Bien sûr mon poussin ! La voici : ",
                      "Laisse moi te donner plus de détails sur ta demande! ",
                      "Mes données ne trouvent pas d'information sur cette demande :("]

button.addEventListener("click", (event) =>{
  event.preventDefault();
  let text_input = document.getElementById('text_input');
  let discussion = document.getElementById('discussion');
  discussion.innerHTML += '<div>' + '<p id="text_output">' +text_input.value + '</p>' + '</div>';
  fetch('/ask?question='+text_input.value)
    .then(function(response){
      return response.json();
    })
    .then(function(data){
      console.log(data);
      wiki = data.wiki;
      discussion.innerHTML += '<div>' + '<p id="answer">' + papy_sentences[0] + data.adress + '</p>' + '<img src="' + data.img_url + '" id="img_gmap">' + '</div>' + '<p id="answer">' + papy_sentences[1] + wiki + '</p>';
    });
})
