function SignIn() {
  var user_input = document.getElementById('username').value;
  var pass_input = document.getElementById('password').value;

  if (user_input === 'Admin@1234' && pass_input === 'Password@1234') {
      alert('Access Granted. Redirecting to the home page...');
      window.location.href = "Home.html";  // Redirect to Home.html
      return false; // Prevent default form submission behavior
  }
 else {
      alert('Incorrect Username or Password.');
      return false;  // Prevent form submission
  }
}
