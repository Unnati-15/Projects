<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isELIgnored="false" %>
<%@ page import="java.util.*" %>
<%@ page import="com.DB.DBConnect" %>
<%@ page import=" com.entity.Bill" %>
<%@ page import="com.DAO.BillDAOimp1" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Admin:Bill</title>
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
      <th scope="col">Bill_id</th>
      <th scope="col">Bill_desc</th>
      <th scope="col">Amount</th>
      <th scope="col">Status</th>
      <th scope="col">Flat_id</th>
    </tr>
  </thead>
  <tbody class="table-group-divider">
  <%
  BillDAOimp1 dao= new BillDAOimp1(DBConnect.getConn());
  List<Bill> list=dao.getAllBills();
  for(Bill m:list){
  %>
  <tr>
      <th scope="row"><%=m.getBill_id()%></th>
      <td><%=m.getBill_desc()%></td>
      <td><%=m.getStatus()%></td>
      <td><%=m.getAmount()%></td>
      <td><%=m.getFlat_id()%></td>
    </tr>
  <%
  }
  %>
    
    
  </tbody>
</table>

</body>
</html>