


def identiteRemarquable(input):
    if(isIdentiteRemarquable(input)):
        dict = buildIdentiteRemarquable()
    else:
        return False


def isIdentiteRemarquable(input):
    value = str(input)
    if(value.__contains__("(") and value.__contains__(")") and value.__contains__("^2")):
        return True
    else:
        return False

def buildIdentiteRemarquable(input):
    dict = {}
    