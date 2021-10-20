vertical = ["a", "b", "c", "d", "e", "f", "g", "h"]
horizontal = ['1', '2', '3', '4', '5', '6', '7', '8']
numbs = {'uno':'1','dos':'2','tres':'3','cuatro':'4','cinco':'5','seis':'6','siete':'7','ocho':'8'}
numbs = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8',
         'for':'4','tree':'3','to':'2','too':'2','do':'2','free':'3','night':'8'}


def isValid(move):
    toReturn = False
    if move != None and len(move) == 4:
        print(type(move[0]), move[1], move[2], move[3])
        if (vertical.__contains__(move[0]) and horizontal.__contains__(move[1]) and
                vertical.__contains__(move[2]) and horizontal.__contains__(move[3])):
            print('sssss')
            toReturn = True
    return toReturn



def traslateMove(move):
    words = str(move).split(' ')
    if len(words) > 3:
        if numbs.__contains__(words[1].lower()):
            words[1] = numbs.get(words[1].lower())
        if numbs.__contains__(words[3].lower()):
            words[3] = numbs.get(words[3].lower())
        first = words[0][0] + words[1]
        second = words[2][0] + words[3]
        print((first + second).lower())
        return (first + second).lower()
