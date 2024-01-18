<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isELIgnored="false" %>
<%@ page import="java.util.*" %>
<%@ page import="com.DB.DBConnect" %>
<%@ page import=" com.entity.Complaint" %>
<%@ page import="com.DAO.ComplaintDAOimp1" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Admin:Complaint</title>
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
      <th scope="col">Complaint_id</th>
      <th scope="col">Complaint_desc</th>
      <th scope="col">Status</th>
      <th scope="col">Flat_id</th>
      <th scope="col">Edit Action</th>
    </tr>
  </thead>
  <tbody class="table-group-divider">
  <%
  ComplaintDAOimp1 dao= new ComplaintDAOimp1(DBConnect.getConn());
  List<Complaint> list=dao.getAllComplaints();
  for(Complaint m:list){
  %>
  <tr>
      <th scope="row"><%=m.getComplaint_id()%></th>
      <td><%=m.getComplaint_desc()%></td>
      <td><%=m.getStatus()%></td>
      <td><%=m.getFlat_id()%></td>
      <td><a href="edit_complaint.jsp?id=<%=m.getComplaint_id()%>" class="btn btn-info" role="button">Edit</a></td>
    </tr>
  <%
  }
  %>
    
    
  </tbody>
</table>

</body>
</html>