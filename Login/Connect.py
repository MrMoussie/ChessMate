import mysql.connector
import configparser

configFile = "SQL.cfg"
sql = None

def connectExists():
    return sql != None and sql.cursor() != None

#Connects to SQL database with credentials of the configuration file.
def connect():
    if not connectExists():
        global sql

        print("SQL: Connecting...")

        config = configparser.ConfigParser()
        config.read(configFile)

        host=config['SQL']['host']
        user=config['SQL']['user']

        try:
            sql = mysql.connector.connect (
                host=host,
                user=user,
                password=config['SQL']['password']
            )
            print("SQL: Connected! [{0}@{1}]".format(user, host))
            return sql
        except Exception as e:
            print(e)
            return None

#Close connection with SQL database
def close():
    if (connectExists()):
        sql.cursor().close()
        print("SQL: Connection closed!")

#Create database in case it does not already exist
def setupDB():
    return None