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
@WebServlet("/register")
public class RegisterServlet extends HttpServlet{
	protected void doPost(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException{
		try {
			String email = req.getParameter("email");
			String psw = req.getParameter("psw");
			String pswrepeat = req.getParameter("psw-repeat");
			user us = new user();
			us.setEmail(email);
			us.setPsw(psw);
			us.setPswrepeat(pswrepeat);
			
			HttpSession session = req.getSession();
			
			userDAOimp1 dao=new userDAOimp1(DBConnect.getConn());
			boolean f = dao.userRegister(us);
			if(f) {
				//System.out.println("registered successfully");
				session.setAttribute("succMsg", "registered successfully");
				res.sendRedirect("register.jsp");
			}
			else {
				//System.out.println("something went wrong!");
				session.setAttribute("failedMsg", "something went wrong!");
				res.sendRedirect("register.jsp");
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}

}
