import re
import sys

def main():
    # input is a str
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    # [0-9] single digits 0-9
    # [1-9][0-9]   10-99
    # 1[0-9][0-9] 100-199
    # 2[0-4][0-9] 200-249
    # 25[0-5] 250-255
    # parantheses are required because of the order of precedence


    #.#.#.#. # - a number between 0-255  inclusive
    matches = re.search(r"\b(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\.|$)){4}\b", ip)
    # returns True False if the inut is valid or not
    if matches:
        return(True)
    else:
        return(False)

if __name__ == "__main__":
    main()
