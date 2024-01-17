"""
    The purpose of this exercise is to implement a function
    which print the type of parameter

"""


def all_thing_is_obj(object: any) -> int:
    # your code here

    obj_type = type(object)

    if obj_type == list:
        print("List :", obj_type)
    elif obj_type == tuple:
        print("Tuple :", obj_type)
    elif obj_type == dict:
        print("Dict :", obj_type)
    elif obj_type == set:
        print("Set :", obj_type)
    elif obj_type == str:
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print("Type not found")

    return 42
