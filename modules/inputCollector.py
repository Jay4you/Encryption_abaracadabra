from sys import exit

def wishToBeMod():
    if __name__ == "numInputValidator":
        exit()
wishToBeMod()

# Start of Input function for text to be encoded
'''
This function asks the user for one line of text to encrypt
Then returns the string of text
'''
def txt():
    text = input("Please input one line of text to encrypt: ")
    str(text)
    return text
# End of Input function for text to be encoded

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

