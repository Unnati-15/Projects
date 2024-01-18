<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isELIgnored="false" %>
<%@ page import="java.util.*" %>
<%@ page import="com.DB.DBConnect" %>
<%@ page import=" com.entity.Flat" %>
<%@ page import="com.DAO.FlatDAOimp1" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Admin:Flat</title>
<%@include file="allCss.jsp" %>
</head>
<body>
<%@include file="navbar.jsp" %>

<c:if test ="${not empty succMsg }">
	<p class="text-center text-success">${succMsg}</p>
	<c:remove var="succMsg" scope="session"/>
</c:if>
<c:if test ="${not empty failedMsg }">
	<p class="text-center text-danger">${failedMsg}</p>
	<c:remove var="failedMsg" scope="session"/>
</c:if>
<c:if test ="${empty userobj}">
	<c:redirect url="../login.jsp"/>
</c:if>
<table class="table">
  <thead>
    <tr>
      <th scope="col">Flat_id</th>
      <th scope="col">Flat_desc</th>
      <th scope="col">Member_id</th>
      
       <th scope="col">Action</th>
       <th scope="col">Edit Action</th>
      <th scope="col">Delete Action</th>
    </tr>
  </thead>
  <tbody class="table-group-divider">
  <%
  FlatDAOimp1 dao= new FlatDAOimp1(DBConnect.getConn());
  List<Flat> list=dao.getAllFlats();
  for(Flat m:list){
  %>
  <tr>
      <th scope="row"><%=m.getFlat_id()%></th>
      <td><%=m.getFlat_desc()%></td>
      <td><%=m.getMember_id()%></td>
      
      <td><%=m.getStatus()%></td>
      <td><a href="edit_flat.jsp?id=<%=m.getFlat_id()%>" class="btn btn-info" role="button">Edit</a></td>
      <td><a href="../deleteflat?id=<%=m.getFlat_id()%>" class="btn btn-info" role="button">Delete</a></td>
    </tr>
  <%
  }
  %>
    
    
  </tbody>
</table>

</body>
</html>