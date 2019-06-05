import csv

# Here we load the CSV
#      Open the file
#      Read line by line
#      Separate in commas

# with open('user_details.csv', newline='') as csv_file:
#     csvreader = csv.reader(csv_file, delimiter=',')
#     print(csvreader)
#     for row in csvreader:
#         print(row[-1])


with open('user_details.csv', newline='') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    iterable = iter(csvreader)
    #print(iterable)
    next(iterable)

    for row in iterable:
        print(row)

# list

# with open('user_details.csv', newline='') as csv_file:
#     csvreader = csv.reader(csv_file, delimiter=',')
#     list_list = list(csvreader)
#     print(type(list_list))
#     print(len(list_list))
#     # for row in list(csvreader):
#     #     print(row)
#     #     print('helloeoe')