import Connect

#Returns 1 single value in the table (i.e.: query[0] == "Value")
#Return None if no results
def selectSingleQuery(query):
    if (Connect.connectExists()):
        sql = Connect.getSQL()
        mycursor = sql.cursor()
        mycursor.execute(query)

        result = mycursor.fetchone()

        if (result != None):
            return result[0]

    return None


#Returns an array of tuples (i.e.: [{0, 1}, {1,2}])
#Returns None if no results
def selectQuery(query):
    if (Connect.connectExists(sql)):
        mycursor = sql.cursor()
        mycursor.execute(query)

        for x in mycursor:
            return None