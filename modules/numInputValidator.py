from sys import exit
from inputCollector import key

def wishToBeMod():
    if __name__ == "numInputValidator":
        exit()

wishToBeMod()

'''
This function validates numeric characters
'''

def numVal():
    try:
        plKey = key()
        assert plKey.numeric
        return plKey
    except TypeError:
        print("Please enter a valid number.\n Number between 1 - 25!")
        numVal()
    except:
        print("Please enter a valid number")
