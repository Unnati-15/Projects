package com.admin.servlet;
import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/Sample")
public class Sample extends HttpServlet 
{
	protected  void doPost(HttpServletRequest req,HttpServletResponse res) throws IOException, ServletException
	{
	
		String name = req.getParameter("username");
		String password = req.getParameter("password");
		PrintWriter out = res.getWriter();
		
		if(password.equals("username")) 
		{
			RequestDispatcher rd=req.getRequestDispatcher("/AddServlet");  
	        rd.forward(req, res);  
	    }  
	    else
	    {  
	        out.print("Sorry UserName or Password Error!");  
	        RequestDispatcher rd=req.getRequestDispatcher("aboutus.jsp");  
	        rd.include(req, res);  
	    }

	}
}	
	