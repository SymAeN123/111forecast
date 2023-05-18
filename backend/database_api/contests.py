import shutil
from pathlib import Path
import sqlite3
import pickle
from datetime import datetime

class Contest:
    def __init__(self, contest: int):
        self.contest = contest
        self.dir = Path('contests')/self.contest

    def initialize_dir(self):
        if not any(self.dir.iterdir()):
            print("Can't initialize non-empty directory")
            return

        fcst_dates = []
        with open(str(self.dir) + "/fcst_dates.pkl", "wb") as file:
            pickle.dump(fcst_dates, file)

        con = sqlite3.connect(str(self.dir) + "/contest.db")
        cur = con.cursor()
        cur.execute(
            """
            CREATE TABLE verifications(
                date_utc TEXT NOT NULL PRIMARY KEY,
                davis_max_temp INTEGER NOT NULL,
                davis_min_temp INTEGER NOT NULL,
                davis_wind_bool INTEGER NOT NULL,
                davis_rain_category INTEGER NOT NULL,
                abroad_station TEXT NOT NULL,
                abroad_max_temp INTEGER NOT NULL,
                abroad_min_temp INTEGER NOT NULL,
                abroad_wind_bool INTEGER NOT NULL,
                abroad_rain_category INTEGER NOT NULL,
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE forecasters(
                key INTEGER NOT NULL PRIMARY KEY,
                email TEXT NOT NULL,
                name TEXT NOT NULL,
                discord INTEGER
            )
            """
        )
        con.commit()
        con.close()

    def add_fcst_date(self, date, abroad_station, home_station="KEDU"):
        with open(str(self.dir) + "/fcst_dates.pkl", "rb") as file:
            fcst_dates = pickle.load(file)

        fcst_dates.append((date, home_station, abroad_station))
        fcst_dates = sorted(fcst_dates, key=lambda x: x[0])

        with open(str(self.dir) + "/fcst_dates.pkl", "wb") as file:
            pickle.dump(fcst_dates, file)

    def store_verification(self, ver_dict):
        con = sqlite3.connect(str(self.dir) + "/contest.db")
        cur = con.cursor()

        cur.execute(
            """
                INSERT INTO verifications 
                (
                    date_utc, davis_max_temp, davis_min_temp, davis_wind_bool, davis_rain_category,
                    abroad_station, abroad_max_temp, abroad_min_temp, abroad_wind_bool, abroad_rain_category
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, 
            (
                ver_dict["date_utc"], ver_dict["davis_max_temp"], ver_dict["davis_min_temp"],
                ver_dict["davis_wind_bool"], ver_dict["davis_rain_category"],
                ver_dict["abroad_station"], ver_dict["abroad_max_temp"], ver_dict["abroad_min_temp"],
                ver_dict["abroad_wind_bool"], ver_dict["abroad_rain_category"]
            )
        )

        con.commit()
        con.close()

    def create_forecaster_table(self, key: int, email:str, name: str):
        con = sqlite3.connect(str(self.dir) + "/contest.db")
        cur = con.cursor()

        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ("f"+str(key),))
        result = cur.fetchone()
        if not (result is None):
            print("Forecaster already exists!")
            con.close()
            return

        cur = con.cursor()
        cur.execute(
            """
                INSERT INTO forecasters 
                (key, email, name) VALUES (?, ?, ?)
            """, 
            (key, email, name)
        )
        cur.execute(
            f"""
                CREATE TABLE {"f"+str(key)}(
                date_utc TEXT NOT NULL PRIMARY KEY,
                davis_max_temp INTEGER NOT NULL,
                davis_min_temp INTEGER NOT NULL,
                davis_wind_bool INTEGER NOT NULL,
                davis_rain_category INTEGER NOT NULL,
                abroad_station TEXT NOT NULL,
                abroad_max_temp INTEGER NOT NULL,
                abroad_min_temp INTEGER NOT NULL,
                abroad_wind_bool INTEGER NOT NULL,
                abroad_rain_category INTEGER NOT NULL,
                )
            """
        )

        con.commit()
        con.close()

    def insert_forecast():


class Contests:
    def __init__(self, filename: str):
        self.filename = filename
        self.contests_dir = Path('contests')

    def insert_contest_at_end(self, status_value):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()

        # Get the highest contest number in the table
        cur.execute("SELECT MAX(contest) FROM contests")
        max_contest = cur.fetchone()[0]

        # Insert a new row at the end of the table with the next contest number
        new_contest = max_contest + 1 if max_contest is not None else 1
        cur.execute("INSERT INTO contests (contest, status) VALUES (?, ?)", (new_contest, status_value))
        con.commit()
        con.close()

        # Create a new folder for the contest
        (self.contests_dir / str(new_contest)).mkdir()
        contest = Contest(new_contest)
        contest.initialize_dir()

    def delete_contest_by_id(self, contest):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()

        cur.execute("SELECT MAX(contest) FROM contests")
        max_contest = cur.fetchone()[0]
        if contest <= 0 or contest > max_contest or max_contest is None:
            print("Either requested context out of range or empty table")
            con.close()
            return

        # Delete the row from the table
        cur.execute("DELETE FROM contests WHERE contest = ?", (contest,))
        con.commit()

        # Remove the folder for the contest
        shutil.rmtree(self.contests_dir / str(contest))

        # Rename all rows with a higher contest number
        cur.execute("SELECT contest FROM contests WHERE contest > ?", (contest,))
        rows = cur.fetchall()
        for row in rows:
            cur.execute("UPDATE contests SET contest = ? WHERE contest = ?", (row[0]-1, row[0]))
            (self.contests_dir / str(row[0])).rename(self.contests_dir / str(row[0]-1))
        con.commit()
        con.close

    def select_new_current_contest(self, contest):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()

        # Set the status value of the given contest to 1
        cur.execute("UPDATE contests SET status = 1 WHERE contest = ?", (contest,))
        con.commit()

        # Set the status value of all other contests to 0
        cur.execute("UPDATE contests SET status = 0 WHERE contest != ?", (contest,))
        con.commit()
        con.close()

    def get_current_contest(self):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()

        # Select the contest number where status = 1
        cur.execute("SELECT contest FROM contests WHERE status = 1")
        result = cur.fetchone()

        con.close()

        if result:
            return result[0]
        else:
            return None

    def get_latest_contest(self):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()

        cur.execute("SELECT MAX(contest) FROM contests")
        max_contest = cur.fetchone()[0]

        if max_contest is None:
            print("Empty table")
            return
        
        con.close()
        
        return max_contest

    def print_contests(self):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()

        cur.execute("SELECT * FROM contests")
        print(cur.fetchall())

        con.close()