def check_email(string):
    if string.find(" ") > -1:
        return False
    if string.find("@") == -1:
        return False
    if string.rfind(".") < string.find("@"):
        return False
    if string.rfind("@") + 1 == string.rfind("."):
        return False

    return True
