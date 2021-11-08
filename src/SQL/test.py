import Queries, Connect

Connect.connect()
Connect.setupDB()

# query = "INSERT INTO leaderboard VALUES (%s, %s, %s, %s, %s, %s);"
# Queries.doQuery(query, ("bob", 1000, 10, 0, 1, 0))

query = "UPDATE leaderboard SET wins = 6 WHERE name = 'bob';"
Queries.doQuery(query, None)

query = "UPDATE leaderboard SET loss = 1 WHERE name = 'bob';"
Queries.doQuery(query, None)

Connect.close()