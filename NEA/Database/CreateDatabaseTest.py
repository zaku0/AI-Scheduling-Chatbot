import os
import sqlite3

def create_database(name):
    check_exists(name)
    con = sqlite3.connect(name)
    cur = con.cursor()
    create_tables(cur)


def create_tables(cur):
    cur.execute("CREATE TABLE UserAccount(Username VARCHAR(20) PRIMARY KEY, Password VARCHAR(64), SecurityQuestion VARCHAR(35), SecurityAnswer VARCHAR(20), FirstName VARCHAR(15), Age INTEGER, CommutePath VARCHAR(50))");
    cur.execute("CREATE TABLE ExtraCurriularActivities(ActivityNumber INTEGER PRIMARY KEY AUTOINCREMENT, AccountNumber INTEGER, Name VARCHAR(20), Day VARCHAR(10), Time VARCHAR(5), RepeatWeekly BOOLEAN, FOREIGN KEY(AccountNumber) REFERENCES UserAccount(AccountNumber))");
    cur.execute("CREATE TABLE Task(TaskNumber INTEGER PRIMARY KEY AUTOINCREMENT, AccountNumber INTEGER, TaskName VARCHAR(20), ResponseDescription VARCHAR(20), ResponseDate VARCHAR(8), ResponseTime VARCHAR(5), FOREIGN KEY(AccountNumber) REFERENCES UserAccount(AccountNumber))");
    cur.execute("CREATE TABLE TransportUpdates(LineName VARCHAR(20) PRIMARY KEY, Time VARCHAR(5), Details VARCHAR(20), Resolved BOOLEAN, WhereOccurred VARCHAR(15), Relevant BOOLEAN)");
    cur.execute("CREATE TABLE TransportTimes(LineName VARCHAR(20) PRIMARY KEY, Station VARCHAR(25), Direction VARCHAR(15), NextArrivalTime VARCHAR(5))");
    cur.execute("CREATE TABLE LunchTimetable(DayNumber INTEGER PRIMARY KEY, Week INTEGER, DayName VARCHAR(10), FoodOption VARCHAR(20), FoodType VARCHAR(15), WhereFound VARCHAR(30))");
    cur.execute("CREATE TABLE TaskIntents(Tag VARCHAR(20) PRIMARY KEY, PatternID INTEGER, ResponseID INTEGER, ContextID INTEGER)");
    cur.execute("CREATE TABLE Pattern(PatternID INTEGER, Value VARCHAR(60), FOREIGN KEY(PatternID) REFERENCES TaskIntents(PatternID))");
    cur.execute("CREATE TABLE Response(ResponseID INTEGER, Value VARCHAR(60), FOREIGN KEY(ResponseID) REFERENCES TaskIntents(ResponseID))");
    cur.execute("CREATE TABLE Context(ContextID INTEGER, Value VARCHAR(60), FOREIGN KEY(ContextID) REFERENCES TaskIntents(ContextID))");

def check_exists(name):
    if os.path.exists(name):
           os.remove(name)

create_database('chatbottest.db')
