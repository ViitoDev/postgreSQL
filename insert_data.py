from post_connect import conn

cursor_obj = conn.cursor()
games = [
    ('The Last of Us 2', 2020, 9.0),
    ('Spider man 2', 2023, 10.0)
]

for game in games:
    cursor_obj.executemany(
        """
            INSERT INTO games(name, year, score)
            VALUES (%s, %s, %s)
        """, games
    )
conn.commit()
print("Data successfully entered.")
conn.close()