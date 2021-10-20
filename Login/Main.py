import Connect
import Queries

def main():
    sql = Connect.connect()
    Connect.setupDB(sql)
    Connect.setupMissions(sql)
    #Connect.dropMissions(sql)
    query = "SELECT description FROM ChessMate.easy_missions"
    Queries.selectQuery(sql, query)
    Connect.close(sql)

if __name__ == "__main__":
    main()