def check(data):
    if len(data) < 10:
        return False

    if data.isdigit() == True:
        return False



    one = False
    two = False
    three = False
    for x in list(data):

        if x.isdigit == True:
            one = True

        if x.islower == True:
            two = True

        if x.isupper == True:
            three = True

    if one == False or two == False or three == False:
        return False
    return True