"""
    The purpose of this exercise is to implement a function
    which print the type of parameter

"""

def all_thing_is_obj(object: any) -> int:
    # your code here

    objType = type(object)

    if objType == list:
        print("List :", objType)
    elif objType == tuple:
        print("Tuple :", objType)
    elif objType == dict:
        print("Dict :", objType)
    elif objType == set:
        print("Set :", objType)
    elif objType == str:
        print(f"{object} is in the kitchen : {objType}")
    else:
        print("Type not found")

    return 42
