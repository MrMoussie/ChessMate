import Connect
import Queries

def main():
    sql = Connect.connect()
    Connect.setupDB(sql)
    Connect.setupMissions(sql)
    #Connect.dropMissions(sql)
    query = "SELECT description FROM ChessMate.easy_missions WHERE id = 1"
    Queries.selectSingleQuery(sql, query)
    Connect.close(sql)

if __name__ == "__main__":
    main()