def what_to_do(instructions):
    if instructions.startswith("Simon says") or instructions.endswith("Simon says"):
        result = instructions.replace(" Simon says ", "")
        result = result.replace("Simon says ", "")
        result = result.replace("Simon says", "")

        result.strip()
        result.lstrip()
        result.rstrip()
        result = "I " + result
    else:
        result = "I won't do it!"

    return result
