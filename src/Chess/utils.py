vertical = ["a", "b", "c", "d", "e", "f", "g", "h"]
horizontal = ['1', '2', '3', '4', '5', '6', '7', '8']
numbs = {'uno': '1', 'dos': '2', 'tres': '3', 'cuatro': '4', 'cinco': '5', 'seis': '6', 'siete': '7', 'ocho': '8'}
numbs = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
         'for': '4', 'tree': '3', 'to': '2', 'too': '2', 'do': '2', 'free': '3', 'night': '8'}


def isValid(move):
    toReturn = False
    if move != None and len(move) == 4:
        print(type(move[0]), move[1], move[2], move[3])
        if (vertical.__contains__(move[0]) and horizontal.__contains__(move[1]) and
                vertical.__contains__(move[2]) and horizontal.__contains__(move[3])):
            toReturn = True
    return toReturn


def traslateMove(move):
    length = len(move)
    if length == 4 or length == 5:
        move = getNormalCommand(move)
    if move != '':
        words = str(move).lower().split(' ')
        if len(words) > 3:
            if numbs.__contains__(words[1]):
                words[1] = numbs.get(words[1])
            if numbs.__contains__(words[3]):
                words[3] = numbs.get(words[3])
            first = words[0][0] + words[1]
            second = words[2][0] + words[3]
            print((first + second))
            return first + second


def getNormalCommand(move):
    move = str(move).lower()
    if len(move) == 4:
        if not move.__contains__(' '):
            if move[0] not in vertical:
                return ''
            if move[1] not in horizontal:
                return ''
            if move[2] not in vertical:
                return ''
            if move[3] not in horizontal:
                return ''
            return move[0] + 'ddd ' + move[1] + ' ' + move[2] + 'dd ' + move[3]
    elif len(move) == 5:
        move = move.replace(' ','')
        toReturn = ''
        if move[1].isalnum() and move[3].isalnum():
            print('fefefghfhgvjhgfhn')
            if move[1] in horizontal and move[3] in horizontal:
                if move[0] in vertical and move[2] in vertical:
                    return move[0] + 'ddd ' + move[1] + ' ' + move[2] + 'dd ' + move[3]
        return toReturn
