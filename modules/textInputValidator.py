from inputCollector import txt
from sys import exit


if __name__ == "__main__":
    exit()
# Start - Text input validation: Makes use of call back function until real str alpha is entered


'''
don't give up and don't let bad data fool you!
Validate input
'''


def encode():
    try:
        new_txt = ""
        old_txt = txt()
        for i in old_txt:
            if ord(i) == 32:
                continue
            else:
                new_txt += i
        assert new_txt.isalpha()
        return new_txt
    except TypeError:
        print("Please enter a valid text: ")
        encode()
    except ValueError:
        print("Please enter a valid text: ")
        encode()

# End - Text input validation: Makes use of call back function until real str alpha is entered
