 
def csv_write(filename, my_list):
    import csv
    with open(filename, 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Name', 'Address', 'Age'])
        for element in my_list:
            csv_writer.writerow(element)

csv_write('csv-file.txt', [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)])