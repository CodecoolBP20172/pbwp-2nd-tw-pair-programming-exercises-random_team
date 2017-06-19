def listoverlap(list1, list2):

    return list(set(list1) & set(list2))

A=[1,2,3,4,5,6,7,8,9,10]
B=[5,6,7,4,2,10,11,99]
def main():
    listoverlap(A,B)
    return


if __name__ == '__main__':
    main()
