import sqlite3

def EnterCustDB(self):
    connection=sqlite3.connect("PYDB.DB")
    connection.execute("CREATE TABLE IF NOT EXISTS EnterCustDeat(GAUGE_NAME TEXT NOT NULL,REPORT_DATE TEXT NOT NULL,REMAINDER_DATE TEXT NOT NULL")
    connection.commit()
    connection.close()

def PDIRDB(self):
    connection=sqlite3.connect("PYDB.DB")
    connection.execute("CREATE TABLE IF NOT EXISTS PDIR_table()")
    connection.commit()
    connection.close()

def CustNonConfDB(self):
    connection=sqlite3.connect("PYDB.DB")
    connection.execute("INSERT INTO ")
    connection.commit()
    connection.close()

def InhouseNonConfDB(self):
    connection=sqlite3.connect("PYDB.DB")

def CalDB(self):
    connection=sqlite3.connect("PYDB.DB")
    connection.execute("CREATE TABLE IF NOT EXISTS Calibration(GAUGE_NAME TEXT NOT NULL,REPORT_DATE TEXT NOT NULL,REMINDER_DATE TEXT NOT NULL")
    connection.commit()
    connection.close()

def MCDB(self):
    connection=sqlite3.connect("PYDB.DB")
    connection.execute("CREATE TABLE IF NOT EXISTS Machine_capability(MACHINE_CAPABILITY_ID TEXT NOT NULL,MACHINE_CAPABILITY_DATE TEXT NOT NULL,MACHINE_CAPABILITY_REMINDER_DATE TEXT NOT NULL)")
    connection.commit()
    connection.close()

def SPCDB(self):
    connection=sqlite3.connect("PYDB.DB")

def MSADB(self):
    connection=sqlite3.connect("PYDB.DB")

def VendAudDB(self):
    connection=sqlite3.connect("PYDB.DB")