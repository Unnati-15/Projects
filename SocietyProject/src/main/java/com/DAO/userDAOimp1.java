package com.DAO;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import com.entity.user;

public class userDAOimp1 implements userDAO{
	private Connection conn;
	public userDAOimp1(Connection conn) {
		super();
		this.conn = conn;
	}
	@Override
	public boolean userRegister(user us) {
		boolean f = false;
		try {
			String sql = "insert into register values(?,?,?)";
			PreparedStatement pst = conn.prepareStatement(sql);
			pst.setString(1, us.getEmail());
			pst.setString(2, us.getPsw());
			pst.setString(3, us.getPswrepeat());
			int i= pst.executeUpdate();
			if(i==1) {
				f=true;
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
		return f;
	}
	@Override
	public user login(String email, String psw) {
		user us=null;
		try {
			String sql = "select * from register where email=? and psw=?";
			PreparedStatement pst = conn.prepareStatement(sql);
			pst.setString(1, email);
			pst.setString(2, psw);
			ResultSet rs=pst.executeQuery();
			while(rs.next()) {
				us=new user();
				us.setEmail(rs.getString(1));
				us.setPsw(rs.getString(2));
				us.setPswrepeat(rs.getString(3));
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
		return us;
	}

	
	

}
