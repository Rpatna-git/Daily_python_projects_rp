import random

import string

def generator(length,captail_chr,numbers_chrs,special_chrs):
    chars=string.ascii_letters

    if captail_chr == "y":
        chars=chars + chars.capitalize()

    if special_chrs == "y":
        chars=chars + string.punctuation

    if numbers_chrs == "y":
        chars=chars + string.digits

    reslt=''.join(random.choice(chars) for _ in range(length))

    return reslt


def main():
    length=int(input("Enter the length of pwd"))
    captail_chr=input("do you want to have Capital letters y/n ")
    small_chars=input("do you want to have small letters y/n ")
    special_chrs=input("do you want to have special letters y/n ")
    res=generator(length,captail_chr,small_chars,special_chrs)
    print(res)

if __name__ == "__main__":
    main()



