<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isELIgnored="false" %>
<%@ page import="java.util.*" %>
<%@ page import="com.DB.DBConnect" %>
<%@ page import=" com.entity.Mom" %>
<%@ page import="com.DAO.MomDAOimp1" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Admin:Mom</title>
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
      <th scope="col">Mom_id</th>
      <th scope="col">Content</th>
      <th scope="col">Date</th>
    </tr>
  </thead>
  <tbody class="table-group-divider">
  <%
  MomDAOimp1 dao= new MomDAOimp1(DBConnect.getConn());
  List<Mom> list=dao.getAllMoms();
  for(Mom m:list){
  %>
  <tr>
      <th scope="row"><%=m.getMom_id()%></th>
      <td><%=m.getContent()%></td>
      <td><%=m.getDate()%></td>
    </tr>
  <%
  }
  %>
    
    
  </tbody>
</table>

</body>
</html>