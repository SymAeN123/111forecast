#Db imports
import sqlite3

con = sqlite3.connect("contests.db")

con.execute(
    """
    CREATE TABLE contests(
        contest INTEGER NOT NULL PRIMARY KEY,
        current INTEGER NOT NULL
    )
    """
)

con.commit()
con.close()