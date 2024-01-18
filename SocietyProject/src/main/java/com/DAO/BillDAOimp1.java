package com.DAO;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

import com.entity.Bill;
import com.entity.Complaint;

public class BillDAOimp1 implements BillDAO{
	private Connection conn;
	public BillDAOimp1(Connection conn) {
		super();
		this.conn=conn;
	}
	public boolean addBill(Bill b) {
		boolean f= false;
		try {
			String sql="insert into bill (bill_desc,amount,status,flat_id) values (?,?,?,?)";
			PreparedStatement pst=conn.prepareStatement(sql);
			pst.setString(1, b.getBill_desc());
			pst.setInt(2,b.getAmount());
			pst.setString(3, b.getStatus());
			pst.setInt(4, b.getFlat_id());
			int i = pst.executeUpdate();
			if(i==1) {
				f=true;
			}
		}
		catch(Exception e) {
			e.printStackTrace();
			
		}
		return f;
	}

	public List<Bill> getAllBills() {
		List<Bill> list = new ArrayList<Bill>();
		Bill m =null;
		try {
			String sql="select * from bill";
			PreparedStatement pst=conn.prepareStatement(sql);
			ResultSet rs = pst.executeQuery();
			while(rs.next()) {
				m = new Bill();
				m.setBill_id(rs.getInt(1));
				m.setBill_desc(rs.getString(2));
				m.setAmount(rs.getInt(3));
				m.setStatus(rs.getString(4));
				m.setFlat_id(rs.getInt(5));
				list.add(m);
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		return list;
	}

	public Bill getBillById(int id) {
		Bill m=null;
		try {
			String sql="select * from bill where bill_id=?";
			PreparedStatement pst=conn.prepareStatement(sql);
			pst.setInt(1,id);
			ResultSet rs = pst.executeQuery();
			while(rs.next()) {
				m = new Bill();
				m.setBill_id(rs.getInt(1));
				m.setBill_desc(rs.getString(2));
				m.setAmount(rs.getInt(3));
				m.setStatus(rs.getString(4));
				m.setFlat_id(rs.getInt(5));
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		return m;
	}

	@Override
	public boolean updateEditBills(Bill b) {
		boolean f =false;
		try {
			String sql="update bill set status=? where bill_id=?";
			PreparedStatement pst=conn.prepareStatement(sql);
			pst.setString(1, b.getStatus());
			pst.setInt(4,b.getBill_id());
			int i = pst.executeUpdate();
			if(i==1) {
				f=true;
			}
			
		}catch(Exception e) {
			e.printStackTrace();
		}
		return f;
	}

	@Override
	public boolean deleteBill(int id) {
		// TODO Auto-generated method stub
		return false;
	}
	
}
