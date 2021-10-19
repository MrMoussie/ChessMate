import Connect

def main():
    sql = Connect.connect()
    Connect.setupDB(sql)
    Connect.close(sql)

if __name__ == "__main__":
    main()