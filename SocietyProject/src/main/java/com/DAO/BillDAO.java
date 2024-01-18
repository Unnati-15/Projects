package com.DAO;

import java.util.List;

import com.entity.Bill;

public interface BillDAO {
	public boolean addBill(Bill b);
	public List<Bill> getAllBills();
	public Bill getBillById(int id);
	public boolean updateEditBills(Bill b);
	public boolean deleteBill(int id);
}
