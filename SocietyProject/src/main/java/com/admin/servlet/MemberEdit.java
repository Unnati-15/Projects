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
@WebServlet("/MemberEdit")
public class MemberEdit extends HttpServlet{
	protected void doPost(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException{
		try {
			int id=Integer.parseInt(req.getParameter("id"));
			String name = req.getParameter("name");
			String email = req.getParameter("email");
			int number = Integer.parseInt(req.getParameter("number"));
			String role = req.getParameter("role");
			Member m = new Member();
			m.setMember_id(id);
			m.setName(name);
			m.setEmail(email);
			m.setNumber(number);
			m.setRole(role);
			MemberDAOimp1 dao=new MemberDAOimp1(DBConnect.getConn());
			boolean f=dao.updateEditMembers(m);
			HttpSession session = req.getSession();
			if(f) {
			
				session.setAttribute("succMsg", "updated successfully");
				res.sendRedirect("admin/view_member.jsp");
			}
			else {
				System.out.println(f);
				session.setAttribute("failedMsg", "something went wrong!");
				res.sendRedirect("admin/view_member.jsp");
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
}
