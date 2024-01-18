<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isELIgnored="false" %>
<%@ page import="javax.servlet.http.HttpServletRequest" %>
<%@ page import=" com.entity.Flat" %>
<%@ page import="com.DAO.FlatDAOimp1" %>
<%@ page import="com.DB.DBConnect" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Admin:Flat</title>
<%@include file="allCss.jsp" %>
</head>
<body>
<%@include file="navbar.jsp" %>

<c:if test ="${empty userobj}">
	<c:redirect url="../login.jsp"/>
</c:if>

<%
int id=Integer.parseInt(request.getParameter("id"));
FlatDAOimp1 dao= new FlatDAOimp1(DBConnect.getConn());
Flat ft=dao.getFlatById(id);
%>

<form action="../FlatEdit" method="post">
  <div class="container">
    <h1 style="flaot:center;font-color:Blue;">Edit Flat</h1>
    <label for="number"><b>Id</b></label>
    <input type="number" placeholder="Enter ID..." name="id" value = "<%=ft.getFlat_id()%>" required>
   
    
   
   <label for="desc"><b>Flat Desc</b></label>
    <input type="text" placeholder="Enter Desc..." name="desc" value = "<%=ft.getFlat_desc()%>" required>
    
    <label for="number"><b>Member ID</b></label>
    <input type="number" placeholder="Enter Member ID..." name="member_id" value = "<%=ft.getMember_id()%>" required>
    
    
    
    <p>to view details click here-><a href="view_flat.jsp" style="color:dodgerblue">View</a></p>

    <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn">Update</button>
    </div>
  </div>
</form>

</body>
</html>