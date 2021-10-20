import Connect, Queries
import hashlib, uuid

def generateSalt():
    return uuid.uuid4().hex

def hash(password, salt):
    return hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

#Check if account already exists
def accountExists(name):
    query = "SELECT COUNT(*) FROM %s.login WHERE name = '%s';" % (Connect.db, name)
    result = Queries.selectSingleQuery(query)

    return bool(result) if query != None else True

def register(name, email, password):
    if (Connect.connectExists() and name != None and password != None):
        if (accountExists(name)):
            print("Error: Account already exists!")
            return False

        salt = generateSalt()
        hashedPass = hash(password, salt)

        query = "INSERT INTO %s.login VALUES ('%s', '%s', '%s', '%s');" % (Connect.db, name, email, hashedPass, salt)
        result = Queries.doQuery(query)

        if (not result):
            print("Error: could not insert into table!")
            return False

        return True
    
    return False

def login(name, password):
    if (Connect.connectExists() and name != None and password != None):
        if (not accountExists(name)):
            print("Error: Account does not exist!")
        
        #TO-DO
    
    return