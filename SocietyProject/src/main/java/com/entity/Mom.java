package com.entity;

public class Mom {
	
	private int mom_id;
	private String content;
	private String date;
	public Mom() {
		super();
		// TODO Auto-generated constructor stub
	}
	public Mom(String content, String date) {
		super();
		this.content = content;
		this.date = date;
	}
	public int getMom_id() {
		return mom_id;
	}
	public void setMom_id(int mom_id) {
		this.mom_id = mom_id;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	public String getDate() {
		return date;
	}
	public void setDate(String date) {
		this.date = date;
	}
}
