package com.entity;

public class Member {
	
	private int member_id;
	private String name;
	private String email;
	private int number;
	private String role;
	public Member() {
		super();
		// TODO Auto-generated constructor stub
	}
		public Member(String name, String email, int number,String role) {
		super();
		this.name = name;
		this.email = email;
		this.number = number;
		this.role=role;
	}
		public int getMember_id() {
			return member_id;
		}
		public void setMember_id(int member_id) {
			this.member_id = member_id;
		}
		public String getName() {
			return name;
		}
		public void setName(String name) {
			this.name = name;
		}
		public String getEmail() {
			return email;
		}
		public void setEmail(String email) {
			this.email = email;
		}
		public int getNumber() {
			return number;
		}
		public void setNumber(int number) {
			this.number = number;
		}
		public String getRole() {
			return role;
		}
		public void setRole(String role) {
			this.role = role;
		}
		
		
}
