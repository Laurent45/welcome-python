"""

    The purpose of this exercise is to write a function that prints the object type
    of all types of "Null". Return 0 if it goes well and 1 in case of error.

"""


def NULL_not_found(object: any) -> int:
    # your code here

    object_type = type(object)

    if object is None:
        print(f"Nothing: {object} {object_type}")
        return 0

    if object_type == float and object != object:
        print(f"Cheese: {object} {object_type}")
        return 0

    if object_type == int and object == 0:
        print(f"Zero: {object} {object_type}")
        return 0

    if object_type == str and object == "":
        print(f"Empty: {object_type}")
        return 0

    if object_type == bool and object is False:
        print(f"Fake: {object} {object_type}")
        return 0

    print("Type not found")
    return 1
