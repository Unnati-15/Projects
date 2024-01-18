package com.DAO;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

import com.entity.Flat;

public class FlatDAOimp1 implements FlatDAO {

	private Connection conn;
	public FlatDAOimp1(Connection conn) {
		super();
		this.conn=conn;
	}
	public boolean addFlat(Flat ft) {
		boolean f= false;
		try {
			String sql="insert into flat (flat_id,flat_desc,member_id,status) values (?,?,?,?)";
			PreparedStatement pst=conn.prepareStatement(sql);
			pst.setInt(1, ft.getFlat_id());
			pst.setString(2, ft.getFlat_desc());
			pst.setInt(3, ft.getMember_id());
			pst.setString(4, ft.getStatus());
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

	public List<Flat> getAllFlats() {
		List<Flat> list = new ArrayList<Flat>();
		Flat ft =null;
		try {
			String sql="select * from flat";
			PreparedStatement pst=conn.prepareStatement(sql);
			ResultSet rs = pst.executeQuery();
			while(rs.next()) {
				ft = new Flat();
				ft.setFlat_id(rs.getInt(1));
				ft.setFlat_desc(rs.getString(2));
				ft.setMember_id(rs.getInt(3));
				ft.setStatus(rs.getString(4));
				list.add(ft);
			}
			
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		return list;
	}
	
	public Flat getFlatById(int id) {
		Flat ft=null;
		try {
			String sql="select * from flat where flat_id=?";
			PreparedStatement pst=conn.prepareStatement(sql);
			pst.setInt(1, id);
			ResultSet rs = pst.executeQuery();
			while(rs.next()) {
				ft = new Flat();
				ft.setFlat_id(rs.getInt(1));
				ft.setFlat_desc(rs.getString(2));
				ft.setMember_id(rs.getInt(3));
				ft.setStatus(rs.getString(4));
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		return ft;
	}

	public boolean updateEditFlats(Flat ft) {
		boolean f =false;
		try {
			String sql="update flat set flat_desc=?,member_id=?,status=? where flat_id=?";
			PreparedStatement pst=conn.prepareStatement(sql);
			pst.setString(1, ft.getFlat_desc());
			pst.setInt(2, ft.getMember_id());
			pst.setString(3, ft.getStatus());
			pst.setInt(4, ft.getFlat_id());
			int i = pst.executeUpdate();
			if(i==1) {
				f=true;
			}
			
		}catch(Exception e) {
			e.printStackTrace();
		}
		return f;
	}
	
	public boolean deleteFlat(int id) {
		boolean f =false;
		try {
			String sql="delete from  flat where flat_id=?";
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
