import Connect

#Returns 1 single value in the table (i.e.: query[0] == "Value")
#Return None if no results
#Uses prepare statements, if not needed pass None in tuple.
def getSQuery(query, value):
    try:
        if (Connect.connectExists()):
            sql = Connect.getSQL()
            mycursor = sql.cursor(prepared=True)

            if (value != None):
                mycursor.execute(query, (value, ))
            else:
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