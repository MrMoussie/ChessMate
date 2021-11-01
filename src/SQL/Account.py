import Connect, Queries
import hashlib, uuid

def generateSalt():
    return uuid.uuid4().hex

def hash(password, salt):
    return hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

#Check if account already exists
def accountExists(name):
    query = "SELECT COUNT(*) FROM %s.login WHERE name = '%s';" % (Connect.db, name)
    result = Queries.getSQuery(query)

    return bool(result) if query != None else True

def register(name, email, password):
    if (Connect.connectExists() and name != None and password != None and name != "" and password != ""):
        if (accountExists(name)):
            print("Error: Account already exists!")
            return False

        salt = generateSalt()
        hashedPass = hash(password, salt)

        query = "INSERT INTO {0}.login VALUES (%s, %s, %s, %s);".format(Connect.db)
        tuple = (name, email, hashedPass, salt)
        result = Queries.doQuery(query, tuple)

        if (not result):
            print("Error: could not insert into table!")
            return False

        return True
    
    return False

#Returns True if credentials are correct, False for otherwise as well as errors
def login(name, password):
    if (Connect.connectExists() and name != None and password != None and name != "" and password != ""):
        if (not accountExists(name)):
            return False
        
        querySalt = "SELECT salt FROM %s.login WHERE name = '%s';" % (Connect.db, name)
        salt = Queries.getSQuery(querySalt)
        queryPass = "SELECT hash FROM %s.login WHERE name = '%s';" % (Connect.db, name)
        hashedPass = Queries.getSQuery(queryPass)

        return True if hashedPass == hash(password, salt) else False
        
    return False