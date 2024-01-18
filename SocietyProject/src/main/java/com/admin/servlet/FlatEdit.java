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
@WebServlet("/FlatEdit")
public class FlatEdit extends HttpServlet{
	protected void doPost(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException{
		try {
			int id=Integer.parseInt(req.getParameter("id"));
			String desc = req.getParameter("desc");
			int member_id = Integer.parseInt(req.getParameter("member_id"));
			String status=req.getParameter("status");
			Flat ft = new Flat();
			ft.setFlat_id(id);
			ft.setFlat_desc(desc);
			ft.setMember_id(member_id);
			ft.setStatus(status);
			FlatDAOimp1 dao=new FlatDAOimp1(DBConnect.getConn());
			boolean f=dao.updateEditFlats(ft);
			HttpSession session = req.getSession();
			if(f) {
			
				session.setAttribute("succMsg", "updated successfully");
				res.sendRedirect("admin/view_flat.jsp");
			}
			else {
				System.out.println(f);
				session.setAttribute("failedMsg", "something went wrong!");
				res.sendRedirect("admin/view_flat.jsp");
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
}
