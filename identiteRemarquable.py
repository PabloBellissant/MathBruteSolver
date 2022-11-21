


def identiteRemarquable(input):
    if(isSimpleIdentiteRemarquable(input)):
        dict = buildIdentiteRemarquable(input)

        listValue = list(dict.keys())
        finalResult = "("+listValue[1]+")^2" + listValue[2]+"2*("+listValue[1]+"*"+listValue[3]+")+("+listValue[3]+")^2"
        return finalResult
    elif(isDoubleIdentiteRemarquable(input)[0]):
        a = isDoubleIdentiteRemarquable(input)[1]
        b = isDoubleIdentiteRemarquable(input)[2]
        finalResult = a +"(^2)-"+ b + "(^2)"
        return finalResult
    else:
        print("non")
        return False


def isSimpleIdentiteRemarquable(input):
    value = str(input)
    if(value.__contains__("(") and value.__contains__(")") and value.__contains__("^2") and (value.__contains__("+") or value.__contains__("-"))):
        return True
    else:
        return False

def isDoubleIdentiteRemarquable(input):
    value = str(input)
    listFake = [False]
    if(value.__contains__(")(") and value.__contains__("-") and value.__contains__("+")):
        startFirstPlacement = getPlacementInString(input, "(")
        endFirstPlacement = getPlacementInString(input, ")")
        operator = ["+", "-"]
        if (getPlacementInString(input, "+") != 0):
            firstOperatorPlacement = getPlacementInString(input, "+")
        if(getPlacementInString(input,"-") != 0 and getPlacementInString(input,"-") < firstOperatorPlacement):
            firstOperatorPlacement = getPlacementInString(input, "-")

        a = ""
        for i in range(firstOperatorPlacement - startFirstPlacement - 1):
            actual = i + 1 + startFirstPlacement
            a = a + input[actual]

        b = ""
        for i in range(endFirstPlacement - firstOperatorPlacement - 1):
            actual = i + 1 + firstOperatorPlacement
            b = b + input[actual]


        list = [True, a, b]
        if(input[firstOperatorPlacement] == "+"):
            wantedMath = "("+a+"-"+b+")"
            if(value.__contains__(wantedMath)):
                return list
        elif(input[firstOperatorPlacement] == "-"):
            wantedMath = "(" + a + "+" + b + ")"
            if (value.__contains__(wantedMath)):
                return list
        else:
            return listFake

    else:
        return listFake


def buildIdentiteRemarquable(input):
    dict = {}
    operator = ["+","-"]
    startPlacement = getPlacementInString(input,"(")
    endPlacement = getPlacementInString(input,")")
    operatorPlacement = 0
    for i in range(operator.__len__()):
        if(getPlacementInString(input,operator[i]) != 0):
            operatorPlacement = getPlacementInString(input, operator[i])
            operator = operator[i]
            break

    a = ""
    for i in range(operatorPlacement-startPlacement-1):
        actual = i+1+startPlacement
        a = a+input[actual]

    b = ""
    for i in range(endPlacement-operatorPlacement-1):
        actual = i+1+operatorPlacement
        b = b+input[actual]


    dict["("] = startPlacement
    dict[a] = "a"
    dict[operator] = operatorPlacement
    dict[b] = "b"
    dict[")"] = endPlacement

    return dict



def getPlacementInString(string,char):
    if(string.__contains__(char)):
        string = str(string)
        for i in range(string.__len__()):
            if(string[i] == char):
                return i
                break
    else:
        return 0

