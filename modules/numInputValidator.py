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
    except:
        print("Please enter a valid number between 1 - 25!")
        numVal()


