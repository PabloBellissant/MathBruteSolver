import main
from identiteRemarquable import identiteRemarquable
import math



formule = main.formule
resultNeeded = main.resultNeeded

arbre = {0:formule}

#1 = Identité remarquable



def tryCalcul():
    if(list(arbre.keys())[len(arbre)-1] != 1):
        newCalcul = identiteRemarquable(formule)
        if(newCalcul != 0):
            arbre[1] = newCalcul
            if(newCalcul == main.resultNeeded):
                return arbre
            else:
                tryCalcul()
    else:
        return False



print(tryCalcul())
