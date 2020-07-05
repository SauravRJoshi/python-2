import csv

def read_csv(filename):
    my_list = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            my_list.append(row)
    print(my_list)

filename = 'csv-file.csv'
read_csv(filename)