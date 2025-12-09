from post_connect import conn

cusrsor_obj = conn.cursor()

sql = """
    UPDATE games
    SET name = %s
    WHERE ID = %s
"""

cusrsor_obj.execute(sql, ("Fifa 25", 2))
conn.commit()
print("Data update success")
conn.close()