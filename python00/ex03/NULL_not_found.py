
def NULL_not_found(object: any) -> int:
    # your code here

    objectType = type(object)
    ret = 0

    if objectType is None:
        print(f"Nothing: {object} {objectType}")
    elif objectType == float:
        print(f"Cheese: {object} {objectType}")
    elif objectType == int:
        print(f"Zero: {object} {objectType}")
    elif objectType == str and object == "":
        print(f"Empty: {objectType}")
    elif objectType == bool:
        print(f"Fake: {object} {objectType}")
    else:
        print("Type not found")
        ret = 1

    return ret
