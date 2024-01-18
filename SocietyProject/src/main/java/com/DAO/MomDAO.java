package com.DAO;

import java.util.List;

import com.entity.Mom;

public interface MomDAO {
	public boolean addMom(Mom m);
	public List<Mom> getAllMoms();
	public Mom getMomById(int id);
	public boolean updateEditMoms(Mom b);
	public boolean deleteMom(int id);
}
