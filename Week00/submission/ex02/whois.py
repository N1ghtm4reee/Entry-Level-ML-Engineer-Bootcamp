import sys

if len(sys.argv) == 2:
    if sys.argv[1].isnumeric():
        if int(sys.argv[1]) % 2:
            print("I'm Odd.")
        else:
            print("I'm Even.")
    else :
        print("AssertionError: argument is not an integer")
else :
    print("AssertionError: more than one argument is provided")