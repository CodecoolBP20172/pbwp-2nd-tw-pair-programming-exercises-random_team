def palindrome(string):
    string.lower()
    if string.replace(" ","")[::-1].lower()==string.replace(" ","").lower():
        return True
    else:
        return False


def main():
    palindrome("Bob")
    return


if __name__ == '__main__':
    main()
