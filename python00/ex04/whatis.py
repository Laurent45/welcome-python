from sys import argv

args = len(argv)

if args > 2:
    print("AssertionError: more than one argument is provided")
elif args == 2:
    try:
        whatis = "Even" if int(argv[1]) % 2 == 0 else "Odd"
        print(f"I am {whatis}")
    except ValueError:
        print("AssertionError: argument is not an integer")
