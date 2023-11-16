
# Start of Input function for shift value
'''
This function asks the user for a shift value, an integer number from the range 1..25
note: you should force the user to enter a valid shift value
Then returns the value
'''


def key():
    num = input("Please shift value: ")
    return num


# End of Input function for shift value


def numVal():
    try:
        plKey = key()
        assert plKey.numeric
        return cond
    except:
        print("Please enter a valid number between 1 - 25!")
        numVal()


encode()
numVal()
print(newTxt)