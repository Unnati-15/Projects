package com.admin.servlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/AddServlet")
public class AddServlet extends HttpServlet
{
	

	public void service(HttpServletRequest req,HttpServletResponse res) throws IOException
	{
		int i = Integer.parseInt(req.getParameter("n1"));
		int j = Integer.parseInt(req.getParameter("n2"));
		int k = i + j;
		int k1 = i - j;
		int k2 = i * j;
		int k3 = i / j;
		PrintWriter out  = res.getWriter();
		out.println("addition result is : " + k);
		out.println("substraction result is : " + k1);
		out.println("multiplication result is : " + k2);
		out.println("division result is : " + k3);
	}
}
