package com.admin.servlet;
import java.io.IOException;

import com.DAO.MemberDAOimp1;
import com.DB.DBConnect;
import com.entity.Member;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/MemberAdd")
public class MemberAdd extends HttpServlet{
	protected void doPost(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException{
		try {
			String name = req.getParameter("name");
			String email = req.getParameter("email");
			int number = Integer.parseInt(req.getParameter("number"));
			String role = req.getParameter("role");
			Member m = new Member(name,email,number,role);
			MemberDAOimp1 dao=new MemberDAOimp1(DBConnect.getConn());
			boolean f=dao.addMember(m);
			HttpSession session = req.getSession();
			if(f) {
			
				session.setAttribute("succMsg", "added successfully");
				res.sendRedirect("admin/add_member.jsp");
			}
			else {
				
				session.setAttribute("failedMsg", "something went wrong!");
				res.sendRedirect("admin/add_member.jsp");
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
}
