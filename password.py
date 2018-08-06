def check(data):
    if len(data) < 10:
        return False

    if data.isdigit() == True:
        return False