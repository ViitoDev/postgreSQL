from post_connect import conn

cursor_obj = conn.cursor()
sql =  """
    DELETE FROM games
    WHERE ID = %s
"""

cursor_obj.execute(sql, (8, ))
conn.commit()
print("Data deleting successful")
conn.close()