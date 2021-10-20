import Connect

def selectQuery(sql, query):
    if (Connect.connectExists(sql)):
        mycursor = sql.cursor()
        mycursor.execute(query)

        for x in mycursor:
            print(x)