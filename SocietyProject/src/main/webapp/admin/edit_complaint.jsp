<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isELIgnored="false" %>
<%@ page import="javax.servlet.http.HttpServletRequest" %>
<%@ page import=" com.entity.Complaint" %>
<%@ page import="com.DAO.ComplaintDAOimp1" %>
<%@ page import="com.DB.DBConnect" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Admin:Complaint</title>
<%@include file="allCss.jsp" %>
</head>
<body>
<%@include file="navbar.jsp" %>

<c:if test ="${empty userobj}">
	<c:redirect url="../login.jsp"/>
</c:if>

<%
int id=Integer.parseInt(request.getParameter("id"));
ComplaintDAOimp1 dao= new ComplaintDAOimp1(DBConnect.getConn());
Complaint m=dao.getComplaintById(id);
%>

<form action="../ComplaintsEdit" method="post">
  <div class="container">
    <h1 style="flaot:center;font-color:Blue;">Edit Complaint</h1>
    <label for="number"><b>Id</b></label>
    <input type="number" placeholder="Enter ID..." name="id" value = "<%=m.getComplaint_id()%>" readonly>
   
    
   
   <label for="text"><b>Complaint Desc</b></label>
    <input type="text" placeholder="Enter Complaint Desc..." name="complaint_desc" value = "<%=m.getComplaint_desc()%>" readonly>
   
   
    <label for="text"><b>Status</b></label>
    <input type="text" placeholder="Enter Status..." name="status" value = "<%=m.getStatus()%>" required>

    
    <label for="number"><b>Flat Id</b></label>
    <input type="number" placeholder="Enter Flat Number..." name="flat_id" value = "<%=m.getFlat_id()%>" readonly>

    <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn">Update</button>
    </div>
  </div>
</form>

</body>
</html>