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
@WebServlet("/BillEdit")
public class BillEdit extends HttpServlet{
	protected void doPost(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException{
		try {
			int id=Integer.parseInt(req.getParameter("id"));
			String bill_desc = req.getParameter("bill_desc");
			int amount = Integer.parseInt(req.getParameter("amount"));
			String status = req.getParameter("status");
			int flat_id = Integer.parseInt(req.getParameter("flat_id"));
			Bill b = new Bill();
			b.setBill_id(id);
			b.setBill_desc(bill_desc);
			b.setStatus(status);
			b.setFlat_id(flat_id);
			BillDAOimp1 dao=new BillDAOimp1(DBConnect.getConn());
			boolean f=dao.updateEditBills(b);
			HttpSession session = req.getSession();
			if(f) {
			
				session.setAttribute("succMsg", "updated successfully");
				res.sendRedirect("view_bill.jsp");
			}
			else {
				System.out.println(f);
				session.setAttribute("failedMsg", "something went wrong!");
				res.sendRedirect("view_bill.jsp");
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
}

