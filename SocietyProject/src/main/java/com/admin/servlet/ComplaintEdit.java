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
@WebServlet("/ComplaintsEdit")
public class ComplaintEdit extends HttpServlet{
	protected void doPost(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException{
		try {
			int id=Integer.parseInt(req.getParameter("id"));
			String complaint_desc = req.getParameter("complaint_desc");
			String status = req.getParameter("status");
			int flat_id = Integer.parseInt(req.getParameter("flat_id"));
			Complaint m = new Complaint();
			m.setComplaint_id(id);
			m.setComplaint_desc(complaint_desc);
			m.setStatus(status);
			m.setFlat_id(flat_id);
			ComplaintDAOimp1 dao=new ComplaintDAOimp1(DBConnect.getConn());
			boolean f=dao.updateEditComplaints(m);
			HttpSession session = req.getSession();
			if(f) {
			
				session.setAttribute("succMsg", "updated successfully");
				res.sendRedirect("admin/view_complaint.jsp");
			}
			else {
				System.out.println(f);
				session.setAttribute("failedMsg", "something went wrong!");
				res.sendRedirect("admin/view_complaint.jsp");
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
}
