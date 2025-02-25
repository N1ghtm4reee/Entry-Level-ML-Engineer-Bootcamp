import string
import sys

def text_analyzer(str):
    printable = 0
    upper = 0
    lower = 0
    space = 0
    punctuation = 0
    if (str == "__doc__"):
        print("\n    This function counts the number of upper characters, lower characters,\n    punctuation and spaces in a given text.")
    else :
        for c in str :
            if (c.isprintable()):
                printable += 1
            if (c in string.ascii_uppercase):
                upper += 1
            if (c in string.ascii_lowercase):
                lower += 1
            if (c in string.whitespace):
                space += 1
            if (c in string.punctuation):
                punctuation += 1
        print(f"The text contains {printable} printable character(s):")
        print(f"- {upper} upper letter(s)")
        print(f"- {lower} lower letter(s)")
        print(f"- {punctuation} punctuation mark(s)")
        print(f"- {space} space(s)")

if len(sys.argv) == 1:
    text_analyzer(input("What is the text to analyze?\n"))
elif (len(sys.argv) == 2):
    text_analyzer(sys.argv[1])
else :
    print("invalid args number")