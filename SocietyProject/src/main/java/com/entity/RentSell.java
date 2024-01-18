package com.entity;

public class RentSell {
	private int flat_id;
	private String flat_desc;
	private String status;
	private int member_id;
	public RentSell() {
		super();
	}
	public RentSell(int flat_id, String flat_desc, String status, int member_id) {
		super();
		this.flat_id = flat_id;
		this.flat_desc = flat_desc;
		this.status = status;
		this.member_id = member_id;
	}
	public int getFlat_id() {
		return flat_id;
	}
	public void setFlat_id(int flat_id) {
		this.flat_id = flat_id;
	}
	public String getFlat_desc() {
		return flat_desc;
	}
	public void setFlat_desc(String flat_desc) {
		this.flat_desc = flat_desc;
	}
	public String getStatus() {
		return status;
	}
	public void setStatus(String status) {
		this.status = status;
	}
	public int getMember_id() {
		return member_id;
	}
	public void setMember_id(int member_id) {
		this.member_id = member_id;
	}
}
