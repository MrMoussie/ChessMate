import os, mysql.connector
import configparser

configFile = os.path.dirname(os.path.abspath(__file__)) + "/SQL.cfg"
missionFiles = ["easy_missions.txt", "medium_missions.txt", "hard_missions.txt", "expert_missions.txt"]

db = ""
sql = None


def getSQL():
    return sql


def connectExists():
    return sql != None and sql.cursor() != None


# Connects to SQL database with credentials of the configuration file.
def connect():
    global db
    global sql

    print("SQL: Connecting...")

    config = configparser.ConfigParser()
    config.read(configFile)

    host=config['SQL']['host']
    user=config['SQL']['user']
    db=config['SQL']['database']

    try:
        sql = mysql.connector.connect (
            host=host,
            user=user,
            password=config['SQL']['password']
        )
        print("SQL: Connected to [{0}@{1}]!".format(user, host))
    except Exception as e:
        print(e)


# Close connection with SQL database
def close():
    global sql

    if (connectExists()):
        sql.cursor().close()
        sql.close()
        sql = None
        print("SQL: Connection closed!")

# Create database and table in case it does not already exist
def setupDB():
    global sql

    if connectExists():
        mycursor = sql.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS %s" % db)
        mycursor.execute("USE %s" % db)
        
        mycursor.execute('CREATE TABLE IF NOT EXISTS login (%s, %s, %s, %s)' % 
            ("name VARCHAR(25) PRIMARY KEY", "email VARCHAR(255) UNIQUE", "hash VARCHAR(255) NOT NULL", "salt VARCHAR(255) NOT NULL"))

        for i in range(len(missionFiles)):
            mycursor.execute('CREATE TABLE IF NOT EXISTS %s (%s, %s)' %
                (missionFiles[i].split(".")[0], "id INT PRIMARY KEY AUTO_INCREMENT", "description VARCHAR(255)"))
        
        setupMissions()


        mycursor.execute('CREATE TABLE IF NOT EXISTS leaderboard (%s, %s, %s, %s, %s, %s, %s);' % 
            ("name VARCHAR(25) PRIMARY KEY", "elo INT", "missionPoints INT", "wins INT", "loss INT", "winrate INT", "FOREIGN KEY(name) REFERENCES login(name)"))

        sql.commit()

# Delete database
def dropDB():
    global sql

    if connectExists():
        mycursor = sql.cursor()
        mycursor.execute("DROP DATABASE {0};".format(db))
        sql.commit()


# Setup mission tables in database
def setupMissions():
    global sql

    mycursor = sql.cursor()

    for i in range(len(missionFiles)):
        with open(os.path.dirname(os.path.abspath(__file__)) + "/missions/" + missionFiles[i]) as file:
            fileName = missionFiles[i].split(".")[0]
            mycursor.execute("SELECT COUNT(*) FROM %s;" % fileName)
            count = mycursor.fetchone()

            if (not count[0]):
                for line in file:
                    query = "INSERT INTO %s (description) VALUES ('%s');" % (fileName, line.rstrip())
                    mycursor.execute(query)
    
        sql.commit()


# Drops the missions tables
def dropMissions():
    global sql
    mycursor = sql.cursor()

    for i in range(len(missionFiles)):
        query = "DROP TABLE IF EXISTS %s.%s" % (db, missionFiles[i].split(".")[0])
        mycursor.execute(query)
    
    sql.commit()
