"""
Setup for the different relations in the database.

The details of the connection are as follows
DBName : hydra
User : hydrus
Password : hydra
Host : localhost
"""
import psycopg2 as psql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def setup_initial_db():
    # Connect with default postgres credentials
    db_credentials = "dbname='postgres' user='postgres' host='localhost' password=''"
    con = psql.connect(db_credentials)
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Create hydra database
    dbname = 'hydra'
    cur = con.cursor()
    cur.execute('CREATE DATABASE ' + dbname)
    cur.close()
    con.close()


def create_relations():
    """Create Relations in the DB according to Hydra Classes."""
    db_credentials = "dbname='hydra' user='postgres' host='localhost' password='hydra'"
    # Starting a connection to postgres DB and getting a cursor
    conn = psql.connect(db_credentials)
    cur = conn.cursor()
    # Creating required relations
    cur.execute("""CREATE TABLE SubSystem (
        ID SERIAL PRIMARY KEY,
        NAME TEXT NOT NULL,
        CATEGORY TEXT NOT NULL
    )
    """)

    cur.execute("""CREATE TABLE COM(
        ID INT UNIQUE REFERENCES SubSystem(ID),
        POWER INT,
        MASS INT,
        COST INT,
        VOLUME INT,
        minWorkingTemp INT,
        maxWorkingTemp INT
    )
    """)

    cur.execute("""CREATE TABLE PROP(
        ID INT UNIQUE REFERENCES SubSystem(ID),
        POWER INT,
        MASS INT,
        COST INT,
        VOLUME INT,
        minWorkingTemp INT,
        maxWorkingTemp INT
    )
    """)

    cur.execute("""CREATE TABLE DTR(
        ID INT UNIQUE REFERENCES SubSystem(ID),
        POWER INT,
        MASS INT,
        COST INT,
        VOLUME INT,
        TYPE TEXT,
        minWorkingTemp INT,
        maxWorkingTemp INT
    )
    """)

    cur.execute("""CREATE TABLE PPW(
        ID INT UNIQUE REFERENCES SubSystem(ID),
        POWER INT,
        MASS INT,
        COST INT,
        VOLUME INT,
        minWorkingTemp INT,
        maxWorkingTemp INT
    )
    """)

    cur.execute("""CREATE TABLE BCK(
        ID INT UNIQUE REFERENCES SubSystem(ID),
        POWER INT,
        MASS INT,
        COST INT,
        VOLUME INT,
        minWorkingTemp INT,
        maxWorkingTemp INT
    )
    """)

    cur.execute("""CREATE TABLE THR(
        ID INT UNIQUE REFERENCES SubSystem(ID),
        POWER INT,
        MASS INT,
        COST INT,
        VOLUME INT,
        TYPE TEXT,
        minTemperature INT,
        maxTemperature INT
    )
    """)

    cur.execute("""CREATE TABLE STR(
        ID INT UNIQUE REFERENCES SubSystem(ID),
        POWER INT,
        MASS INT,
        COST INT,
        VOLUME INT,
        minWorkingTemp INT,
        maxWorkingTemp INT
    )
    """)

    cur.execute("""CREATE TABLE CDH(
        ID INT UNIQUE REFERENCES SubSystem(ID),
        POWER INT,
        MASS INT,
        COST INT,
        VOLUME INT,
        minWorkingTemp INT,
        maxWorkingTemp INT
    )
    """)

    cur.execute("""CREATE TABLE AODCS(
        ID INT UNIQUE REFERENCES SubSystem(ID),
        POWER INT,
        MASS INT,
        COST INT,
        VOLUME INT,
        TYPE TEXT,
        MECHANISM TEXT,
        minWorkingTemp INT,
        maxWorkingTemp INT
    )
    """)
    # Close the cursor
    cur.close()
    # Commit changes to the DB
    conn.commit()
    # Close connection
    conn.close()


def delete_all():
    """Delete all relations created in the DB."""
    db_credentials = "dbname='hydra' user='hydrus' host='localhost' password='hydra'"
    # Starting a connection to postgres DB and getting a cursor
    conn = psql.connect(db_credentials)
    cur = conn.cursor()
    # Creating required relations
    cur.execute("DROP TABLE AODCS")
    cur.execute("DROP TABLE CDH")
    cur.execute("DROP TABLE STR")
    cur.execute("DROP TABLE PPW")
    cur.execute("DROP TABLE BCK")
    cur.execute("DROP TABLE PROP")
    cur.execute("DROP TABLE DTR")
    cur.execute("DROP TABLE COM")
    cur.execute("DROP TABLE THR")
    cur.execute("DROP TABLE SubSystem")
    cur.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    setup_initial_db()
    create_relations()
    # delete_all()
