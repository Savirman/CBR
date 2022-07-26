import psycopg2


# Function connection to database
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print("Database opened succesfully")
    except OperationalError as e:
        print(f"The error {e} occurred")
    return connection

connection = create_connection("postgres", "postgres", "111111", "127.0.0.1", "5432")

# Function creation of database "cbr"
def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT COUNT(*) = 0 FROM pg_catalog.pg_database WHERE datname = 'cbr'")
        not_exists, = cursor.fetchone()
        if not_exists:
            cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

create_database_query = "CREATE DATABASE cbr"
create_database(connection, create_database_query)

connection = create_connection("cbr", "postgres", "111111", "127.0.0.1", "5432")

# Function creation of table "valutes"
def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

create_valutes_table = """
CREATE TABLE IF NOT EXISTS valutes (
  valuteid VARCHAR(5) PRIMARY KEY NOT NULL,
  numcode INTEGER NOT NULL, 
  charcode VARCHAR(3) NOT NULL,
  nominal INTEGER NOT NULL,
  name VARCHAR(50) NOT NULL,
  value REAL NOT NULL
)
"""

execute_query(connection, create_valutes_table)
