package com.DAO;

import java.util.List;

import com.entity.Flat;

public interface FlatDAO {
	public boolean addFlat(Flat ft);
	public List<Flat> getAllFlats();
	public Flat getFlatById(int id);
	public boolean updateEditFlats(Flat ft);
	public boolean deleteFlat(int id);
}
