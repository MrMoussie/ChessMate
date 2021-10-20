import Connect
import Queries
import Account

def main():
    Connect.connect()
    Connect.setupDB()
    Connect.setupMissions()
    #Connect.dropMissions()

    Account.register("yes123", "moussie@mail.com", "yes123")

    Connect.close()

if __name__ == "__main__":
    main()