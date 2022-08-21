import { initializeApp } from "https://www.gstatic.com/firebasejs/9.9.3/firebase-app.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  const firebaseConfig = {
    apiKey: "AIzaSyA9XE1UJ4l5-6hCyinlfbKAwjrnxQVcVQo",
    authDomain: "healthify-de8b2.firebaseapp.com",
    projectId: "healthify-de8b2",
    storageBucket: "healthify-de8b2.appspot.com",
    messagingSenderId: "995622981984",
    appId: "1:995622981984:web:26a574d7d91d25b755ce05"
  };

  const app = initializeApp(firebaseConfig);

  const auth = firebase.auth()
  const database = firebase.database()
  
  function register () {
  // Get all our input fields
  email = document.getElementById('email').value
  password = document.getElementById('password').value
  full_name = document.getElementById('full_name').value
    
  if (validate_email(email) == false || validate_password(password) == false) {
    alert('Email or Password is incorrect')
    return
  }
    
  auth.createUserWithEmailAndPassword(email, password)
    .then(function() {
    
    	var user = auth.currentUser
      alert('User Created!')
    
      var database_ref = database.ref()
      
      var user_data = {
        email : email, 
        full_name : full_name
        last_login : Date.now()  
      }
        
      database_ref.child('users/' + user.uid).update(user_data)

  })
    .catch(function(error)) {
           var error_code = error.code
           var error_message = error.message
           
           alert(error_message)

  function login () {
      email = document.getElementById('email').value
      password = document.getElementById('password').value
    
      if (validate_email(email) == false || validate_password(password) == false) {
        alert('Email or Password is incorrect')
        return
      }
      
      auth.signInWithEmailAndPassword(email, password)
      .then(function() {
        var user = auth.currentUser
        
        var database_ref = database.ref()
        
        var user_data = {
          last_login : Date.now()
        }
        
        database_ref.child('users/' + user.uid).update(user_data)
        
        alert('User Logged In!')

      })
      .catch(function(error) {
        var error_code = error.code
        var error_message = error.message

        
      })
  }
   
  function validate_email(email) {
    expression = /^[^@]+@\w+(\.\w+)+\w$/
  if (expression.test(email) == true) {
    return true
  } else {
    return false
  }
}
    
  function validate_password(password) {
    // Firebase only accepts lengths greater than 6
    if (password < 6) {
      return false
    } else {
      return true
  }
}
    
  function validate_field(field) {
    if (field == null) {
      return false
  }
    
    if (field.length <= 0) {	
      return false
    } else {
      return true
  }
}
