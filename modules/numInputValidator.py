from inputCollector import key
from sys import exit


if __name__ != "__main__":
    exit()

'''
This function validates numeric characters
'''


def numeral():
    try:
        pokey = key()
        assert pokey.numeric
        return pokey
    except TypeError:
        print("Please enter a valid number.\n Number between 1 - 25!")
        numeral()
    except ValueError:
        print("Please enter a valid number")
