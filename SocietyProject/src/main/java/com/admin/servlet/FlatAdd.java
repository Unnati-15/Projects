package com.admin.servlet;
import java.io.IOException;

import com.DAO.FlatDAOimp1;
import com.DB.DBConnect;
import com.entity.Flat;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/FlatAdd")
public class FlatAdd extends HttpServlet{
	protected void doPost(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException{
		try {
			int flat_id = Integer.parseInt(req.getParameter("flat_id"));
			String desc = req.getParameter("desc");
			int member_id = Integer.parseInt(req.getParameter("member_id"));
			String status=req.getParameter("status");
			Flat ft = new Flat(flat_id,desc,member_id,status);
			FlatDAOimp1 dao=new FlatDAOimp1(DBConnect.getConn());
			boolean f=dao.addFlat(ft);
			HttpSession session = req.getSession();
			if(f) {
			
				session.setAttribute("succMsg", "added successfully");
				res.sendRedirect("admin/add_flat.jsp");
			}
			else {
				
				session.setAttribute("failedMsg", "something went wrong!");
				res.sendRedirect("admin/add_flat.jsp");
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
}
