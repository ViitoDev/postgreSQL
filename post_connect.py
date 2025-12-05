import psycopg2

conn = psycopg2.connect(
    database = 'db_games',
    user = 'postgres',
    password = 'admin123',
    host = 'localhost',
    port = '5432'
)