def bissextile(n:int)->bool:
    if (n%4 == 0 and n%100!= 0) or (n%400 == 0):
        return True
    return False


def bis(n:int)-> bool:
    if n%4 == 0:
        if n%100 == 0:
            if n%400 == 0:
                return True
            return False
        return True
    return False

            
        