//sprava na lavo, odpoved od chatbota
$(document).ready(function(){
    $("#form").submit(function(e){
      e.preventDefault();

      let val = $("#input").val();
      
      axios.post('http://localhost:5005/webhooks/rest/webhook',{
        'sender': 'test_user',
        'message': val
      }).then(response => {
        console.log(response);
        const responseParagraphs = $("#response-paragraphs");
          //responseParagraphs.empty(); // Clear the paragraphs

          response.data.forEach(item => {
              const newDivBot = document.createElement("div");
              newDivBot.className = "d-flex flex-row justify-content-start";
              const paragraph = document.createElement("p");
              paragraph.innerHTML = item.text;
              paragraph.className = "small p-2 ms-3 mb-1 rounded-3";
              paragraph.style.backgroundColor = "#f5f6f7";
              newDivBot.appendChild(paragraph)
              targetDiv.append(newDivBot);
              targetDiv.scrollTop = targetDiv.scrollHeight;
          });
      })

    });
  });

  //sprava napravo, moja sprava

  const inputElement = document.getElementById('input');
  const targetDiv = document.getElementById('targetDiv');

  inputElement.addEventListener('keyup', function (event) {
    if (event.key === 'Enter' || event.keyCode === 13) {
      event.preventDefault(); // Prevent the default line break in the input
      const inputValue = inputElement.value;
      if (inputValue.trim() !== '') {
        const newDiv = document.createElement('div');
        newDiv.className = 'd-flex flex-row justify-content-end mb-4 pt-1';
        const newParagraph = document.createElement('p');
        newParagraph.className = 'small p-2 me-3 mb-1 text-white rounded-3 bg-primary';
        newParagraph.textContent = inputValue;
        targetDiv.appendChild(newDiv);
        newDiv.appendChild(newParagraph);
        inputElement.value = ''; // Clear the input field
        targetDiv.scrollTop = targetDiv.scrollHeight;
      }
    }
  });
