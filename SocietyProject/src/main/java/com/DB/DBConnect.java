package com.DB;
import java.sql.Connection;
import java.sql.DriverManager;
public class DBConnect {
	public static Connection getConn() {
		Connection conn = null;
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");	
			conn  = DriverManager.getConnection("jdbc:mysql:///societyproject","root","unnati@15");
		}
		catch(Exception e) {
			e.printStackTrace();		
		}
		return conn;
	}
}			
	


