<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isELIgnored="false" %>
<%@ page import="java.util.*" %>
<%@ page import="com.DB.DBConnect" %>
<%@ page import=" com.entity.Member" %>
<%@ page import="com.DAO.MemberDAOimp1" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Admin:Home</title>
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
      <th scope="col">Member_id</th>
      <th scope="col">Name</th>
      <th scope="col">Email</th>
      <th scope="col">Number</th>
      <th scope="col">Role</th>
      <th scope="col">Edit Action</th>
      <th scope="col">Delete Action</th>
    </tr>
  </thead>
  <tbody class="table-group-divider">
  <%
  MemberDAOimp1 dao= new MemberDAOimp1(DBConnect.getConn());
  List<Member> list=dao.getAllMembers();
  for(Member m:list){
  %>
  <tr>
      <th scope="row"><%=m.getMember_id()%></th>
      <td><%=m.getName()%></td>
      <td><%=m.getEmail()%></td>
      <td><%=m.getNumber()%></td>
      <td><%=m.getRole()%></td>
      <td><a href="edit_member.jsp?id=<%=m.getMember_id()%>" class="btn btn-info" role="button">Edit</a></td>
      <td><a href="../delete?id=<%=m.getMember_id()%>" class="btn btn-info" role="button">Delete</a></td>
    </tr>
  <%
  }
  %>
    
    
  </tbody>
</table>

</body>
</html>