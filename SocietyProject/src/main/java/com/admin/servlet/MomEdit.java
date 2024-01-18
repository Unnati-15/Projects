package com.admin.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.DAO.MomDAOimp1;
import com.DB.DBConnect;
import com.entity.Mom;
@WebServlet("/MomEdit")
public class MomEdit extends HttpServlet{
	protected void doPost(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException{
		try {
			int id=Integer.parseInt(req.getParameter("id"));
			String content = req.getParameter("content");
			String date = req.getParameter("date");
			Mom b = new Mom();
			b.setMom_id(id);
			b.setContent(content);
			b.setDate(date);
			MomDAOimp1 dao=new MomDAOimp1(DBConnect.getConn());
			boolean f=dao.updateEditMoms(b);
			HttpSession session = req.getSession();
			if(f) {
			
				session.setAttribute("succMsg", "updated successfully");
				res.sendRedirect("view_mom.jsp");
			}
			else {
				System.out.println(f);
				session.setAttribute("failedMsg", "something went wrong!");
				res.sendRedirect("view_mom.jsp");
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
}


