vertical = ["a","b","c","d","e","f","g","h"]
horizontal = ['1','2','3','4','5','6','7','8']
all = []
def isValid(move):
    toReturn = False
    if len(move) == 4:
        print(type(move[0]),move[1],move[2],move[3])
        if (vertical.__contains__(move[0]) and horizontal.__contains__(move[1]) and
                vertical.__contains__(move[2]) and horizontal.__contains__(move[3])):
            print('sssss')
            toReturn = True
    return toReturn
