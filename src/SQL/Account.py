import Connect, Queries
import hashlib, uuid

def generateSalt():
    return uuid.uuid4().hex

def hash(password, salt):
    return hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

#Check if account already exists
def accountExists(name):
    if (name == None or name == ""):
        return True
    query = "SELECT COUNT(*) FROM {0}.login WHERE name = %s;".format(Connect.db)
    result = Queries.getSQuery(query, name)

    return bool(result) if query != None else True

#Check if email already exists
def emailExists(email):
    if (email == None or email == ""):
        return True

    query = "SELECT COUNT(*) FROM {0}.login WHERE email = %s;".format(Connect.db)
    result = Queries.getSQuery(query, email)

    return bool(result) if query != None else True

#Insert account into database after validation
def register(name, email, password):
    if (Connect.connectExists() and name != None and email != None and password != None and name != "" and email != "" and password != ""):
        if (accountExists(name) or emailExists(email)):
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
        
        querySalt = "SELECT salt FROM {0}.login WHERE name = %s;".format(Connect.db)
        salt = Queries.getSQuery(querySalt, name).decode('utf-8')
        queryPass = "SELECT hash FROM {0}.login WHERE name = %s;".format(Connect.db)
        hashedPass = Queries.getSQuery(queryPass, name).decode('utf-8')

        return True if hashedPass == hash(password, salt) else False
        
    return False