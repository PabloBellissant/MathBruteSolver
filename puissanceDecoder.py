



def whereContain(string, what, start = 0):
    string = str(string)
    if(string.__contains__(what)):
        for i in range(len(string)):
            if(string[i] == what):
                return i
                break
    else:
        return False


def puissanceDecoder(formule):
    if(formule.__contains__("^")):
        placement = whereContain(formule, "^")
        puissance = ""
        value = ""
        startPuissance = placement+1
        startValue = placement-1
        if(formule[startPuissance] == "("):
            logicBrackets = 1
            for i in range(len(formule)-placement-2):
                if(formule[placement + 2 + i] == ")"):
                    logicBrackets -= 1
                if (formule[placement + 2 + i] == "("):
                    logicBrackets += 1
                if (logicBrackets == 0):
                    endPuissance = placement + 2 + i
                    for i in range(endPuissance-startPuissance-1):
                        val = i+startPuissance+1
                        puissance = puissance + formule[val]
                    break
        else:
            puissance = formule[startPuissance]

        if(formule[startValue] == ")"):
            logicBrackets = -1
            for i in range(placement - 1):
                if (formule[placement - 2 - i] == ")"):
                    logicBrackets -= 1
                if (formule[placement - 2 - i] == "("):
                    logicBrackets += 1
                if (logicBrackets == 0):
                    endValue = placement - 2 - i
                    for i in range(startValue-endValue-1):
                        val = endValue + i + 1
                        value = value + formule[val]
                    break

        else:
            value = formule[startValue]

    #Faire code pour les puissance. On a déjà : Toutes les valeurs de départ et d’arrivé pour quoi est puissancé et la puissance, il nous manque uniquement le calcul. puis la mise en place de la réponse





    else:
        return False

puissanceDecoder("(2x)^4")




