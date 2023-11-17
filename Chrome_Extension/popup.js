document.getElementById("summarizeButton").addEventListener("click", sendCode);
async function sendCode() {
  var codeSegment = document.getElementById('codeInput').value;
  const outputDiv= document.getElementById('output')
  // Send the code segment to the Flask backend
  fetch('http://127.0.0.1:5000/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json, application/xml, text/plain, text/html, *.*',
      'Access-Control-Allow-Origin': '*',
    },
    body: JSON.stringify({ code_segment: codeSegment }),
  })
  .then(response =>  {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
  return response.json();
  })
  .then(data => {
      // Display the output in the extension popup
      outputDiv.innerText = `Code Summarization: ${data.result}`;
  })
  .catch(error => {
    console.error('Error:', error);
    outputDiv.innerText = 'An error occurred.';
  });
}


  