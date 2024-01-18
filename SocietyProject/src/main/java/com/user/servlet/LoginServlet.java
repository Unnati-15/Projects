package com.user.servlet;
import java.io.IOException;
import com.DAO.userDAOimp1;
import com.DB.DBConnect;
import com.entity.user;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/loginservlet")

public class LoginServlet extends HttpServlet{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	protected void doPost(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException{
		
		try {
			userDAOimp1 dao= new userDAOimp1(DBConnect.getConn());
			HttpSession session = req.getSession();
			
			String email = req.getParameter("email");
			String psw = req.getParameter("psw");
			
			if("admin@gmail.com".equals(email) && "admin".equals(psw)) {
				user us = new user();
				session.setAttribute("userobj", us);
				res.sendRedirect("admin/home.jsp");
			}
			else {
				user us=dao.login(email, psw);
				if(us!=null) {
					session.setAttribute("userobj", us);
					res.sendRedirect("home.jsp");
				}
				else {
					session.setAttribute("failedMsg", "Email and password invalid");
					res.sendRedirect("login.jsp");
				}
				res.sendRedirect("home.jsp");
			}
		}
		catch(Exception e) {
			e.printStackTrace();	
			}
   }
}

