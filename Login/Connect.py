import mysql.connector
import configparser

configFile = "SQL.cfg"
db = ""

def connectExists(sql):
    return sql != None and sql.cursor() != None

#Connects to SQL database with credentials of the configuration file.
def connect():
    global db

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
        return sql
    except Exception as e:
        print(e)
        return None

#Close connection with SQL database
def close(sql):
    if (connectExists(sql)):
        sql.cursor().close()
        print("SQL: Connection closed!")

#Create database and table in case it does not already exist
def setupDB(sql):
    if connectExists(sql):
        mycursor = sql.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS %s" % db)
        mycursor.execute("USE %s" % db)
        
        mycursor.execute('CREATE TABLE IF NOT EXISTS login (%s, %s, %s, %s)' % 
            ("name VARCHAR(25) PRIMARY KEY", "email VARCHAR(255)", "hash VARCHAR(255) NOT NULL", "salt VARCHAR(255) NOT NULL"))
        mycursor.execute("SHOW DATABASES")

        for x in mycursor:
            print(x)
