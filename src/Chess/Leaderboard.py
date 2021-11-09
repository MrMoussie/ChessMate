import sys
sys.path.append("../SQL")
import Queries

def getLeaderboard():
    query = "SELECT * FROM leaderboard;"
    result = Queries.getAllQuery(query, None)

    return result

def updateElo(name, elo):
    query = "UPDATE leaderboard SET elo = %s WHERE name = %s;"
    Queries.doQuery(query, (elo, name))

def getElo(name):
    query = "SELECT elo FROM leaderboard WHERE name = %s;"
    return Queries.getSQuery(query, name)

def addElo(name, elo):
    query = "UPDATE leaderboard SET elo = elo + %s WHERE name = %s;"
    Queries.doQuery(query, (elo, name))

def addPoints(name, points):
    query = "UPDATE leaderboard SET missionPoints = missionPoints + %s WHERE name = %s;"
    Queries.doQuery(query, (points, name))

def incrementWins(name):
    query = "UPDATE leaderboard SET wins = wins + 1 WHERE name = %s;"
    Queries.doQuery(query, (name, ))

    updateWinrate()

def incrementLoss(name):
    query = "UPDATE leaderboard SET loss = loss + 1 WHERE name = %s;"
    Queries.doQuery(query, (name, ))

    updateWinrate()

#########################################################################
## ! AUTOMATICALLY UPDATES WINRATE ACCORDING TO CURRENT TABLE VALUES ! ##
#########################################################################
def updateWinrate():
    query = "UPDATE leaderboard SET winrate = (CASE WHEN wins = 0 THEN 0 WHEN loss = 0 THEN 100 WHEN loss > 0 THEN wins/(wins+loss)*100 END);"
    Queries.doQuery(query, None)