package com.admin.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.DAO.FlatDAOimp1;
import com.DB.DBConnect;

@WebServlet("/deleteflat")
public class FlatDelete extends HttpServlet{
	protected void doGet(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException{
		try {
			int id= Integer.parseInt(req.getParameter("id"));
			FlatDAOimp1 dao=new FlatDAOimp1(DBConnect.getConn());
			boolean f=dao.deleteFlat(id);
			HttpSession session = req.getSession();
			if(f) {
			
				session.setAttribute("succMsg", "deleted successfully");
				res.sendRedirect("admin/view_flat.jsp");
			}
			else {
				
				session.setAttribute("failedMsg", "something went wrong!");
				res.sendRedirect("admin/view_flat.jsp");
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
}
