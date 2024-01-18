package com.DAO;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

import com.entity.Complaint;


public class ComplaintDAOimp1 implements ComplaintDAO {

	private Connection conn;
	public ComplaintDAOimp1(Connection conn) {
		super();
		this.conn=conn;
	}
	public boolean addComplaint(Complaint c) {
		boolean f= false;
		try {
			String sql="insert into complaint (complaint_desc,status,flat_id) values (?,?,?)";
			PreparedStatement pst=conn.prepareStatement(sql);
			pst.setString(1, c.getComplaint_desc());
			pst.setString(2, c.getStatus());
			pst.setInt(3, c.getFlat_id());
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

	public List<Complaint> getAllComplaints() {
		List<Complaint> list = new ArrayList<Complaint>();
		Complaint m =null;
		try {
			String sql="select * from complaint";
			PreparedStatement pst=conn.prepareStatement(sql);
			ResultSet rs = pst.executeQuery();
			while(rs.next()) {
				m = new Complaint();
				m.setComplaint_id(rs.getInt(1));
				m.setComplaint_desc(rs.getString(2));
				m.setStatus(rs.getString(3));
				m.setFlat_id(rs.getInt(4));
				list.add(m);
			}
			
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		return list;
	}
	
	public Complaint getComplaintById(int id) {
		Complaint m=null;
		try {
			String sql="select * from complaint where complaint_id=?";
			PreparedStatement pst=conn.prepareStatement(sql);
			pst.setInt(1,id);
			ResultSet rs = pst.executeQuery();
			while(rs.next()) {
				m = new Complaint();
				m.setComplaint_id(rs.getInt(1));
				m.setComplaint_desc(rs.getString(2));
				m.setStatus(rs.getString(3));
				m.setFlat_id(rs.getInt(4));
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		return m;
	}

	public boolean updateEditComplaints(Complaint c) {
		boolean f =false;
		try {
			String sql="update complaint set complaint_desc=?,status=?,flat_id=? where complaint_id=?";
			PreparedStatement pst=conn.prepareStatement(sql);
			pst.setString(1,c.getComplaint_desc());
			pst.setString(2, c.getStatus());
			pst.setInt(3,c.getFlat_id());
			pst.setInt(4,c.getComplaint_id());
			int i = pst.executeUpdate();
			if(i==1) {
				f=true;
			}
			
		}catch(Exception e) {
			e.printStackTrace();
		}
		return f;
	}
	
	public boolean deleteComplaint(int id) {
		boolean f =false;
		try {
			String sql="delete from  complaint where complaint_id=?";
			PreparedStatement pst=conn.prepareStatement(sql);
			pst.setInt(1,id);
			int i = pst.executeUpdate();
			if(i==1) {
				f=true;
			}
			
		}catch(Exception e) {
			e.printStackTrace();
		}
		return f;
	}
	
}
