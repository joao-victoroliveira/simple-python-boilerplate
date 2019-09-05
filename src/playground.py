
def fibbonacci(num):
    if num < 3:
        return 1
    return fibbonacci(num-1) + fibbonacci(num-2)

def findCommonNumber(listOne,listTwo):

    return [ elementoA for elementoA in listOne for elementoB in listTwo if elementoA == elementoB ]

