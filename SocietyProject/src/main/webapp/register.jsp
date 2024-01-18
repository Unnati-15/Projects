<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
 <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
 <%@ page isELIgnored="false" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Registration</title>
<%@include file="all_component/allCss.jsp"%>
</head>
<body>
<%@include file="all_component/navbar.jsp"%>
<c:if test ="${not empty succMsg }">
	<p class="text-center text-success">${succMsg}</p>
</c:if>
<c:if test ="${not empty failedMsg }">
	<p class="text-center text-danger">${failedMsg}</p>
</c:if>
  <form action="register" method="post">
  <div class="container">
    <h1 style="flaot:center">Registration Form</h1>
    <p>Please fill in this form to create an account.</p>
   
    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>

    <label for="psw-repeat"><b>Repeat Password</b></label>
    <input type="password" placeholder="Repeat Password" name="psw-repeat" required>
    
    
    
    <p>Already have an account?<a href="login.jsp" style="color:dodgerblue">Sign In</a>.</p>

    <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn">Sign Up</button>
    </div>
  </div>
</form>


  

</body>
</html>

