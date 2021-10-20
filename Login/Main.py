import Connect
import Queries

def main():
    Connect.connect()
    Connect.setupDB()
    Connect.setupMissions()
    #Connect.dropMissions()
    #query = "SELECT description FROM ChessMate.easy_missions WHERE id = 1"
    #print(Queries.selectSingleQuery(query))
    Connect.close()

if __name__ == "__main__":
    main()