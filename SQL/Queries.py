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

def doQuery(query):
    try:
        if (Connect.connectExists()):
            sql = Connect.getSQL()
            mycursor = sql.cursor()
            mycursor.execute(query)

            sql.commit()

            return True
    except Exception as e:
        print(e)

    return False