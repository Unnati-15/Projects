<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isELIgnored="false" %>
<%@ page import="javax.servlet.http.HttpServletRequest" %>
<%@ page import=" com.entity.Bill" %>
<%@ page import="com.DAO.BillDAOimp1" %>
<%@ page import="com.DB.DBConnect" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Admin:Complaint</title>
<%@include file="../all_component/allCss.jsp" %>
</head>
<body>
<%@include file="../all_component/navbar.jsp" %>

<c:if test ="${empty userobj}">
	<c:redirect url="../login.jsp"/>
</c:if>

<%
int id=Integer.parseInt(request.getParameter("id"));
BillDAOimp1 dao= new BillDAOimp1(DBConnect.getConn());
Bill m=dao.getBillById(id);
%>

<form action="../BillEdit" method="post">
  <div class="container">
    <h1 style="flaot:center;font-color:Blue;">Edit Bill</h1>
    <label for="hidden"><b>Id</b></label>
    <input type="hidden" placeholder="Enter ID..." name="id" value = "<%=m.getBill_id()%>" required>
   
    
   
   <label for="bill_desc"><b>Bill Desc</b></label>
    <input type="text" placeholder="Enter Bill Desc..." name="bill_desc" value = "<%=m.getBill_desc()%>" required>
   
   
   <label for="amount"><b>Amount</b></label>
    <input type="number" placeholder="Enter Amount..." name="amount" value = "<%=m.getAmount()%>" required>
   
    <label for="status"><b>Status</b></label>
    <input type="text" placeholder="Enter Status..." name="status" value = "<%=m.getStatus()%>" required>

    
    <label for="flat_id"><b>Flat Id</b></label>
    <input type="number" placeholder="Enter Flat Number..." name="flat_id" value = "<%=m.getFlat_id()%>" required>

    <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn">Update</button>
    </div>
  </div>
</form>

</body>
</html>