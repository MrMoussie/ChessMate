import Connect

# Returns 1 single value in the table (i.e.: query[0] == "Value")
# Return None if no results
# Uses prepare statements, if not needed pass None in value.
def getSQuery(query, value):
    try:
        if (Connect.connectExists() and query != None and query != ""):
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

#Returns arrays of rows (array of tuples)
#Prepare statements
def getAllQuery(query, value):
    try:
        if (Connect.connectExists() and query != None and query != ""):
            sql = Connect.getSQL()
            mycursor = sql.cursor(prepared=True)

            if (value != None):
                mycursor.execute(query, (value, ))
            else:
                mycursor.execute(query)

            result = mycursor.fetchall()
            
            sql.commit()

            if (result != None):
                array = []
                for row in result:
                    array.append(row)

                return array
    except Exception as e:
        print(e)
    
    return None


# Prepared statement
# Always give a tuple as second argument!
def doQuery(query, tuple):
    try:
        if (Connect.connectExists() and query != None and query != ""):
            sql = Connect.getSQL()
            mycursor = sql.cursor(prepared=True)

            if (tuple != None):
                mycursor.execute(query, tuple)
            else:
                mycursor.execute(query)
            
            sql.commit()

            return True
    except Exception as e:
        print(e)

    return False