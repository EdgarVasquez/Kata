
def RangeInteger1(number):

    if number >= 2 and number < 6:
        return  True
    else:
        return  False

def ContainsRange(number):
    if number >= 2 and number < 5:
        return True
    else:
        return False

def ContainsRange2(number):
    if number >= 3 and number < 5:
        return True
    else:
        return False

def ContainsRange3(number):
    if number >= 2 and number < 10:
        return True
    else:
        return False
def GetAllPoints(RANGE1,RANGE2):
    i = 0
    resultado = ""
    while i < RANGE2:
         if i >= RANGE1 and i < RANGE2:
             resultado = resultado +","+ str(i)
             i = i +1
         else:
             i = i + 1
    return  resultado


if __name__ == '__main__':
    RangeInteger(1)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
