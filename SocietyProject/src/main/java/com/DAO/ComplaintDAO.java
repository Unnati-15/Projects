package com.DAO;

import java.util.List;

import com.entity.Complaint;


public interface ComplaintDAO {
	
	public boolean addComplaint(Complaint c);
	public List<Complaint> getAllComplaints();
	public Complaint getComplaintById(int id);
	public boolean updateEditComplaints(Complaint c);
	public boolean deleteComplaint(int id);
}
