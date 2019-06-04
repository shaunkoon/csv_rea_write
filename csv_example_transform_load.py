import csv

with open('user_details.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Get the data and remove gender and title
#   return  transformed data

def transform_user_details(csv_full_name):
    newuser_data = []

    with open(csv_full_name, newline='') as csv_file:
        user_details_csv = csv.reader(csv_file, delimiter=',')

        for rowlist in user_details_csv:
            transformed_row = []
            transformed_row.append(rowlist[1].capitalize())
            transformed_row.append(rowlist[2].capitalize())
            transformed_row.append(rowlist[4])
            newuser_data.append(transformed_row)
        return newuser_data

new_trans_data = transform_user_details('user_details.csv')


# Let create a function to write our transformed data
#   write to csv

def create_new_csv_user_data(transformed_data, new_user_file_name):
    # have transformed data
    # open new file
    new_file = open(new_user_file_name, 'w', newline='')

    #write to that file
    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(transformed_data)

print(new_trans_data)
create_new_csv_user_data(new_trans_data, 'transformed_csv.csv')