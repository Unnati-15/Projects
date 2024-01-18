package com.entity;

public class Complaint {
	
	private int complaint_id;
	private String complaint_desc;
	private String status;
	private int flat_id;
	
	public Complaint() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Complaint(String complaint_desc, String status, int flat_id) {
		super();
		this.complaint_desc = complaint_desc;
		this.status = status;
		this.flat_id = flat_id;
	}

	public int getComplaint_id() {
		return complaint_id;
	}

	public void setComplaint_id(int complaint_id) {
		this.complaint_id = complaint_id;
	}

	public String getComplaint_desc() {
		return complaint_desc;
	}

	public void setComplaint_desc(String complaint_desc) {
		this.complaint_desc = complaint_desc;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public int getFlat_id() {
		return flat_id;
	}

	public void setFlat_id(int flat_id) {
		this.flat_id = flat_id;
	}
}
