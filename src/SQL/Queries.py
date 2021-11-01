import Connect

#Returns 1 single value in the table (i.e.: query[0] == "Value")
#Return None if no results
def getSQuery(query):
    try:
        if (Connect.connectExists()):
            sql = Connect.getSQL()
            mycursor = sql.cursor()
            mycursor.execute(query)

            result = mycursor.fetchone()

            if (result != None):
                return result[0]
    except Exception as e:
        print(e)
    
    return None

#Prepared statement
def doQuery(query, tuple):
    try:
        if (Connect.connectExists()):
            sql = Connect.getSQL()
            mycursor = sql.cursor(prepared=True)

            mycursor.execute(query, tuple)
            sql.commit()

            return True
    except Exception as e:
        print(e)

    return False