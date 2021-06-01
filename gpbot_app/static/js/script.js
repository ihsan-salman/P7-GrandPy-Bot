// init the button for the click function
let button = document.getElementById('button');
// Init 3 sentences for the answer of grandpy
let papy_sentences = ["Bien sûr mon poussin ! La voici : ",
                      "Laisse moi te donner plus de détails sur ta demande! ",
                      "Mes données ne trouvent pas d'information sur cette demande :("]


// click event to recover the value of the input text
button.addEventListener("click", (event) =>{

  // make sure that the event doesn't return to another url
  event.preventDefault();
  // init two html id
  let text_input = document.getElementById('text_input');
  let discussion = document.getElementById('discussion');
  // display the user's request 
  discussion.innerHTML += '<div>' + '<p id="text_output">' +text_input.value + '</p>' + '</div>';
  
  // send and recover data function into flask
  fetch('/ask?question='+text_input.value)
    // return the user's request
    .then(function(response){
      return response.json();
    })
    // recover the sorted data
    .then(function(data){
      let wiki = data.wiki;
      // condition to display the correct answer in accord with the recover data
      // just a sentence if wiki == null 
      // or a full information about the wiki api
      if (wiki == null) {
        discussion.innerHTML += '<div>' + '<p id="answer">' + papy_sentences[0] + data.adress + '</p>' + '<img src="' + data.img_url + '" id="img_gmap">' + '</div>' + '<p id="answer">' + papy_sentences[2] + '</p>';
        console.log(wiki)      
      } else {
        discussion.innerHTML += '<div>' + '<p id="answer">' + papy_sentences[0] + data.adress + '</p>' + '<img src="' + data.img_url + '" id="img_gmap">' + '</div>' + '<p id="answer">' + papy_sentences[1] + wiki + '</p>';
      };
    });
})
