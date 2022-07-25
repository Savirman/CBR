import psycopg2

con = psycopg2.connect(
    database = "cbr",
    user = "postgres",
    password = "111111",
    host = "127.0.0.1",
    port = "5432"
)

print("Database opened succesfully")