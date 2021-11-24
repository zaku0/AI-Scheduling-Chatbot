import sqlite3
import json
import os
import hashlib

class Database():
    tableColumns = {'Pattern':1,'Response':1,'Context':1,'UserAccount':8,'ExtraCurricularActivities':6,'Task':6,'TransportUpdates':6,'LunchTimetable':5,'TaskIntents':4}
    tableNames = ['UserAccount','ExtraCurriularActivities','Task','TransportUpdates','TransportTimes','LunchTimetable','TaskIntents','Pattern','Response','Context']
    tables = tableNames
    def __init__(self):
        self.name = 'chatbottest.db'
        self.connect()
    def connect(self):
        self.con = sqlite3.connect('../Database/'+self.name)
        self.cur = self.con.cursor()
    def get_noFields(self,table):
        return Database.tableColumns[table]
    def get_noRows(self,table):
        self.execute('SELECT COUNT(*) from %s'%table)
        cur_result = self.fetchone()
        return cur_result[0]
    def add_field(self,table):
        name = table + self.get_noFields(table)
        self.cur.execute("ALTER TABLE %s ADD COLUMN %s VARCHAR(300)"%(table,name))
        Database.tableColumns[table] += 1
    def insert(self,table,values):
        self.cur.execute('INSERT INTO %s VALUES %s'%(table,values))
    def create_user(self,values):
        self.cur.execute('INSERT INTO UserAccount(Username,Password,SecurityQuestion,SecurityAnswer,FirstName,Age,CommutePath) VALUES (?,?,?,?,?,?,?)',values)
    def execute(self, command):
        self.cur.execute(command)
    def executemany(self,command,values):
        self.cur.executemany(command,values)
    def fetchone(self):
        return self.cur.fetchone()
    def fetchmany(self,size):
        return self.cur.fetchmany(size)
    def fetchall(self):
        return self.cur.fetchall()
    def getValueArray(self,table,ID):
        myID = str(ID)
        self.execute('SELECT Value FROM %s WHERE %s=%s'%(table,table+'ID',myID))
        return self.fetchall()
    def formatQueryArray(self,array):
        formatted = []
        for value in array:
            formatted.append(value[0])
        return formatted
    def create_intentsJSON(self):
        self.con.row_factory = sqlite3.Row
        records = self.cur.execute('SELECT * from TaskIntents').fetchall()
        jsonrecords = []
        for tag in range(len(records)):
            pattern = self.formatQueryArray(self.getValueArray('Pattern',records[tag][1]))
            response = self.formatQueryArray(self.getValueArray('Response',records[tag][2]))
            context = self.formatQueryArray(self.getValueArray('Context',records[tag][3]))
            jsonrecords.append((('tag',records[tag][0]),('patterns',pattern),('responses',response),('context',context)))
        data = json.dumps([dict(i) for i in jsonrecords], indent = 4)
        jsonData = '{"intents": %s}'%(data)
        file = "../Chatbot/intents.json"
        self.check_file_exists(file)
        with open(file, "w") as outfile:
            outfile.write(jsonData)
        return
    def hash(self,string):
        return hashlib.sha256(string.encode('utf-8')).hexdigest()
    def check_file_exists(self,filename):
        if os.path.exists(filename):
            os.remove(filename)
    def clear_table(self,table):
        self.cur.execute('DELETE FROM %s'%(table))
    def make(self):
        self.cur.execute("CREATE TABLE UserAccount(AccountNumber INTEGER PRIMARY KEY AUTOINCREMENT, Username VARCHAR(20), Password VARCHAR(64), SecurityQuestion VARCHAR(35), SecurityAnswer VARCHAR(20), FirstName VARCHAR(15), Age INTEGER, TnCs BOOLEAN, CommutePath VARCHAR(50))");
    def commit(self):
        self.con.commit()
    def exit(self):
        self.con.commit()
        self.con.close()

db = Database()
