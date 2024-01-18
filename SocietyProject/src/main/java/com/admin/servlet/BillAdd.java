package com.admin.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.DAO.BillDAOimp1;
import com.DB.DBConnect;
import com.entity.Bill;

@WebServlet("/BillAdd")
public class BillAdd extends HttpServlet{
	protected void doPost(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException{
		try {
			String bill = req.getParameter("bill_desc");
			int amount = Integer.parseInt(req.getParameter("amount"));
			String status = req.getParameter("status");
			int flat_id = Integer.parseInt(req.getParameter("flat_id"));
			Bill b = new Bill(bill,amount,status,flat_id);
			BillDAOimp1 dao=new BillDAOimp1(DBConnect.getConn());
			boolean f=dao.addBill(b);
			HttpSession session = req.getSession();
			if(f) {
			
				session.setAttribute("succMsg", "added successfully");
				res.sendRedirect("admin/add_bill.jsp");
			}
			else {
				
				session.setAttribute("failedMsg", "something went wrong!");
				res.sendRedirect("admin/add_bill.jsp");
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
}

