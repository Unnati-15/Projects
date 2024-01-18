package com.DAO;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

import com.entity.Member;

public class MemberDAOimp1 implements MemberDAO {

	private Connection conn;
	public MemberDAOimp1(Connection conn) {
		super();
		this.conn=conn;
	}
	public boolean addMember(Member m) {
		boolean f= false;
		try {
			String sql="insert into member (name,email,number,role) values (?,?,?,?)";
			PreparedStatement pst=conn.prepareStatement(sql);
			pst.setString(1, m.getName());
			pst.setString(2, m.getEmail());
			pst.setInt(3, m.getNumber());
			pst.setString(4, m.getRole());
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

	public List<Member> getAllMembers() {
		List<Member> list = new ArrayList<Member>();
		Member m =null;
		try {
			String sql="select * from member";
			PreparedStatement pst=conn.prepareStatement(sql);
			ResultSet rs = pst.executeQuery();
			while(rs.next()) {
				m = new Member();
				m.setMember_id(rs.getInt(1));
				m.setName(rs.getString(2));
				m.setEmail(rs.getString(3));
				m.setNumber(rs.getInt(4));
				m.setRole(rs.getString(5));
				list.add(m);
			}
			
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		return list;
	}
	
	public Member getMemberById(int id) {
		Member m=null;
		try {
			String sql="select * from member where member_id=?";
			PreparedStatement pst=conn.prepareStatement(sql);
			pst.setInt(1, id);
			ResultSet rs = pst.executeQuery();
			while(rs.next()) {
				m = new Member();
				m.setMember_id(rs.getInt(1));
				m.setName(rs.getString(2));
				m.setEmail(rs.getString(3));
				m.setNumber(rs.getInt(4));
				m.setRole(rs.getString(5));
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		return m;
	}

	public boolean updateEditMembers(Member m) {
		boolean f =false;
		try {
			String sql="update member set name=?,email=?,number=?,role=? where member_id=?";
			PreparedStatement pst=conn.prepareStatement(sql);
			pst.setString(1, m.getName());
			pst.setString(2, m.getEmail());
			pst.setInt(3, m.getNumber());
			pst.setString(4, m.getRole());
			pst.setInt(5,m.getMember_id());
			
			int i = pst.executeUpdate();
			if(i==1) {
				f=true;
			}
			
		}catch(Exception e) {
			e.printStackTrace();
		}
		return f;
	}
	
	public boolean deleteMember(int id) {
		boolean f =false;
		try {
			String sql="delete from  member where member_id=?";
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
