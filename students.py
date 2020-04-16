def assortedStudentsRecord(allrecords):
    # This function accept aggregate scores of all students in a list, and return assorted list in ascending order

    return sorted(allrecords)


def getPosition(studentrecord, allrecords):
    all_records = assortedStudentsRecord(allrecords)
    print('this is all_records : ', all_records)
    print(all_records.index(studentrecord) +1)




allrecords = [234,987, 45.9, 453, 4422,482]

getPosition(482, allrecords)