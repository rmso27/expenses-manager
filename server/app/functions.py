## IMPORTS ##

# Import modules
import psycopg2

## FUNCTIONS ##

# Check DB connection
def test_db_conn(db_host, db, db_user, db_password, db_conn_timeout):

    try:
        conn = psycopg2.connect(
            host = db_host,
            database = db,
            user = db_user,
            password = db_password,
            connect_timeout = db_conn_timeout
        )
        conn.close()
        return "OK"
    except:
        return "FAILED"