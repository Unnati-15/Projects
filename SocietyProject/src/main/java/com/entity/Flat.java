package com.entity;

public class Flat {
	
	private int flat_id;
	private String flat_desc;
	private int member_id;
	private String status;
	
	public Flat() {
		super();
	}

	public Flat(int flat_id,String flat_desc, int member_id,String status) {
		super();
		this.flat_id = flat_id;
		this.flat_desc = flat_desc;
		this.member_id = member_id;
		this.status=status;
	}

	public int getFlat_id() {
		return flat_id;
	}

	public void setFlat_id(int flat_id) {
		this.flat_id = flat_id;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public String getFlat_desc() {
		return flat_desc;
	}

	public void setFlat_desc(String flat_desc) {
		this.flat_desc = flat_desc;
	}

	public int getMember_id() {
		return member_id;
	}

	public void setMember_id(int member_id) {
		this.member_id = member_id;
	}
}
