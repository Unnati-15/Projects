<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>About Us</title>
</head>
<body>

	<form action="Sample" method="post">
  <div class="container">
    <h1 style="flaot:center;font-color:Blue;">Sample form</h1>
   
   <label for="text"><b>Username</b></label>
    <input type="text" placeholder="Enter Username..." name="username" required>
    
    <label for="text"><b>Password</b></label>
    <input type="password" placeholder="Enter Password..." name="password" required>
    

    <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn">ADD</button>
    </div>
  </div>
	</form>
	
	<form action="AddServlet" method="post">
  <div class="container">
    <h1 style="flaot:center;font-color:Blue;">Calculator</h1>
   
   <label for="text"><b>Number 1</b></label>
    <input type="number" placeholder="Enter num1..." name="n1" required>
    
    <label for="text"><b>Password</b></label>
    <input type="number" placeholder="Enter num2..." name="n2" required>
    

    <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn">Result</button>
    </div>
  </div>
	</form>

</body>
</html>