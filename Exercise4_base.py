import time
import sys
import itertools


def search_function(filename):
    values = ["", ""]
    values[0] = 0  # Smaller number is saved here
    values[1] = 0  # The greater number is saved here
    # Add code underneath!
    # ///////////Open and read file
    import csv
    records = []
    try:
        with open(filename, 'r') as recordListCsv:
            recordList = csv.reader(recordListCsv)
            for i in recordList:
                records.append(i[0])
        recordListCsv.close()
        mylist = list(dict.fromkeys(records))
        mylist.sort()
        firtElement = int(mylist.__getitem__(0))
        lastElement = int(mylist.__getitem__(len(mylist) - 1))
        val = int(firtElement) * 3
        if lastElement > val:
            values[0] = firtElement
            values[1] = lastElement
        return values
    except FileNotFoundError:
        print("Error while processing file '{}', stopping.".format(filename))
        raise SystemExit
    # ///////////////////// remove reapeated key

    # Code addition ends here.

def main():
    # file = 'T4D2.txt'
    file = input("Input filename: \n")
    timer1 = time.perf_counter()
    result = search_function(file)
    timer2 = time.perf_counter()
    duration = timer2 - timer1
    if ((result[0] == 0) and (result[1] == 0)):
        print("Search algorithm did not find a matching pair.")
    elif (duration > 2):
        print("Search algorithm was not fast enough.")
    else:
        print("Search algorithm was fast! Awesome!")
        print("It found a matching pair:", result[0], "and", result[1])


main()
