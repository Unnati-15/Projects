package com.entity;

public class Bill {
	private int bill_id;
	private String bill_desc;
	private int amount;
	private String status;
	private int flat_id;
	

public Bill() {
	super();
}


public Bill(String bill_desc, int amount, String status, int flat_id) {
	super();
	this.bill_desc = bill_desc;
	this.amount = amount;
	this.status = status;
	this.flat_id = flat_id;
}


public int getBill_id() {
	return bill_id;
}


public void setBill_id(int bill_id) {
	this.bill_id = bill_id;
}


public String getBill_desc() {
	return bill_desc;
}


public void setBill_desc(String bill_desc) {
	this.bill_desc = bill_desc;
}


public int getAmount() {
	return amount;
}


public void setAmount(int amount) {
	this.amount = amount;
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