def bissextile(a : int) -> bool:

    return (a%4 == 0 and a%100 != 0) or (a%4 == 0 and a%100 == 0 and a%400 == 0)

def bissextile2(a : int) -> bool:
    if a%4 == 0:
        if a%100 == 0:
            if a%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False