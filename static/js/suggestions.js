const suggestionForm = document.getElementById('suggestion-form');
const response = document.getElementById('response');

suggestionForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const suggestion = document.getElementById('suggestion').value;

  // You can use AJAX or fetch to send the data to the server
  // In this example, we're just logging the data to the console
  console.log(`Name: ${name}\nEmail: ${email}\nSuggestion: ${suggestion}`);
  name.value = '';
  email.value = '';
  // Display a success message
  response.innerHTML = 'Thanks for your suggestion!';
  // Clear the input fields
  document.getElementById('name').value = '';
  document.getElementById('email').value = '';
  document.getElementById('suggestion').value = '';
});
