import Connect

def main():
    Connect.connect()
    Connect.setupDB()
    Connect.close()

if __name__ == "__main__":
    main()