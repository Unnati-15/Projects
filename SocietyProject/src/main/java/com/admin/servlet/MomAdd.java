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


@WebServlet("/MomAdd")
public class MomAdd extends HttpServlet{
	protected void doPost(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException{
		try {
			String content = req.getParameter("content");
			String date = req.getParameter("date");
			Mom b = new Mom(content,date);
			MomDAOimp1 dao=new MomDAOimp1(DBConnect.getConn());
			boolean f=dao.addMom(b);
			HttpSession session = req.getSession();
			if(f) {
			
				session.setAttribute("succMsg", "added successfully");
				res.sendRedirect("admin/add_mom.jsp");
			}
			else {
				
				session.setAttribute("failedMsg", "something went wrong!");
				res.sendRedirect("admin/add_mom.jsp");
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
}


