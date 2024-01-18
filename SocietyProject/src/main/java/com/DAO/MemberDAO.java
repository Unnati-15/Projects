package com.DAO;

import java.util.List;

import com.entity.Member;

public interface MemberDAO {
	public boolean addMember(Member m);
	public List<Member> getAllMembers();
	public Member getMemberById(int id);
	public boolean updateEditMembers(Member m);
	public boolean deleteMember(int id);
}
