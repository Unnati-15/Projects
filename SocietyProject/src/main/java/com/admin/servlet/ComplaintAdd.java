package com.admin.servlet;
import java.io.IOException;

import com.DAO.ComplaintDAOimp1;
import com.DB.DBConnect;
import com.entity.Complaint;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/ComplaintAdd")
public class ComplaintAdd extends HttpServlet{
	protected void doPost(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException{
		try {
			String complaint = req.getParameter("complaint");
			String status = req.getParameter("status");
			int flat_id = Integer.parseInt(req.getParameter("flat_id"));
			Complaint c = new Complaint(complaint,status,flat_id);
			ComplaintDAOimp1 dao=new ComplaintDAOimp1(DBConnect.getConn());
			boolean f=dao.addComplaint(c);
			HttpSession session = req.getSession();
			if(f) {
			
				session.setAttribute("succMsg", "added successfully");
				res.sendRedirect("add_complaint.jsp");
			}
			else {
				
				session.setAttribute("failedMsg", "something went wrong!");
				res.sendRedirect("add_complaint.jsp");
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
}
