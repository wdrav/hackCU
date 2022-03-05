import csv


with open("cases.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=',')
    header = next(reader)
    print(header[0])
    for row in header:
        case_Lat = [5]
        print(case_Lat)