from sys import exit

# Start - Text input validation: Makes use of call back function until real str alpha is entered
'''
don't give up and don't let bad data fool you!
Validate input
'''

def encode():
    try:
        newTxt = ""
        oldTxt = txt()
        for i in oldTxt:
            if ord(i) == 32:
                continue
            else:
                newTxt += i
        assert newTxt.isalpha()
        return newTxt
    except:
        print("Please enter a valid text: ")
        encode()

# End - Text input validation: Makes use of call back function until real str alpha is enter

def wishToBeMod():
    if __name__ == "numInputValidator":
        exit()
wishToBeMod()