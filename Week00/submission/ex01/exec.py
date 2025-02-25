import sys

if len(sys.argv) > 1:
    i = len(sys.argv)
    while i > 1 :
        str = sys.argv[i - 1].swapcase()
        print(f"{str[::-1]}",end="")
        i = i - 1
print("")