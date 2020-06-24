def get_percentage(number, round_digits=-1):
    if round_digits < 0:
        percent = int(number * 100)
    else:
        percent = round(number * 100, round_digits)
    return ("{}%".format(percent))
