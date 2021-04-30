document
  .getElementById("text_input")
  .addEventListener("input", function(e) {
    document
      .getElementById("text_output")
      .innerText = e.target.value;
});

let text_input = document.getElementByI('text_input');
let text_output = document.getElementById('text_output');
let button = document.getElementById('button')

button.addEventListener("click", () =>{
  document
  .getElementById("text_input")
  .addEventListener("input", function(e) {
    document
      .getElementById("text_output")
      .innerText = e.target.value;
  });

})

