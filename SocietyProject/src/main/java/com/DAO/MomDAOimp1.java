package com.DAO;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;
import com.entity.Mom;

public class MomDAOimp1 implements MomDAO{
	private Connection conn;
	public MomDAOimp1(Connection conn) {
		super();
		this.conn=conn;
	}
	public boolean addMom(Mom b) {
		boolean f= false;
		try {
			String sql="insert into mom (content,date) values (?,?)";
			PreparedStatement pst=conn.prepareStatement(sql);
			pst.setString(1, b.getContent());
			pst.setString(2,b.getDate());
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


@Override
public List<Mom> getAllMoms() {
		List<Mom> list = new ArrayList<Mom>();
		Mom m =null;
		try {
			String sql="select * from mom";
			PreparedStatement pst=conn.prepareStatement(sql);
			ResultSet rs = pst.executeQuery();
			while(rs.next()) {
				m = new Mom();
				m.setMom_id(rs.getInt(1));
				m.setContent(rs.getString(2));
				m.setDate(rs.getString(3));
				list.add(m);
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		return list;
	}

@Override
public Mom getMomById(int id) {
	Mom m=null;
	try {
		String sql="select * from mom where mom_id=?";
		PreparedStatement pst=conn.prepareStatement(sql);
		pst.setInt(1,id);
		ResultSet rs = pst.executeQuery();
		while(rs.next()) {
			m = new Mom();
			m.setMom_id(rs.getInt(1));
			m.setContent(rs.getString(2));
			m.setDate(rs.getString(3));
		}
	}
	catch(Exception e) {
		e.printStackTrace();
	}
	return m;
}
@Override
public boolean updateEditMoms(Mom b) {
	boolean f =false;
	try {
		String sql="update mom set content=? where mom_id=?";
		PreparedStatement pst=conn.prepareStatement(sql);
		pst.setString(1, b.getContent());
		pst.setInt(2,b.getMom_id());
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
public boolean deleteMom(int id) {
	// TODO Auto-generated method stub
	return false;
}
}