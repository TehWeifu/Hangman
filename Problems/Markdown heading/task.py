def heading(string, number=0):
    if number < 2:
        return "# " + string
    elif number < 3:
        return "## " + string
    elif number < 4:
        return "### " + string
    elif number < 5:
        return "#### " + string
    elif number < 6:
        return "##### " + string
    else:
        return "###### " + string
