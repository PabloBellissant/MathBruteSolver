import main
from puissanceDecoder import puissanceDecoder



formule = main.formule
resultNeeded = main.resultNeeded

arbre = {0:formule}

#1 = Écrire les puissances



def tryCalcul():
    if(list(arbre.keys())[len(arbre)-1] != 1):
        newCalcul = puissanceDecoder(formule)
        if(newCalcul != 0):
            arbre[1] = newCalcul
            if(newCalcul == main.resultNeeded):
                return arbre
            else:
                tryCalcul()
    else:
        return False






def forceCalcul(method):
    if(method == 1):
        return identiteRemarquable(main.formule)

print(forceCalcul(1))