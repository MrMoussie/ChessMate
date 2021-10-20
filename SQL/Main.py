import Connect
import Queries
import Account

def main():
    Connect.connect()
    Connect.setupDB()
    Connect.setupMissions()
    #Connect.dropMissions()
    #query = "SELECT description FROM ChessMate.easy_missions WHERE id = 1"
    #print(Queries.selectSingleQuery(query))

    Account.register("yes123", "moussie@mail.com", "yes123")
    Account.register("yes1234", None, "yes2134")

    Connect.close()

if __name__ == "__main__":
    main()