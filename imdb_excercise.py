# IMDB Data Transformation
# Only films from 2010 onward                       DONE
# Movies - Only Title Type (no shorts)              DONE
# Only Primary Title (not original title)           DONE
# Remove the end date and is adult fields entirely  DONE
import csv

with open('imdb_title.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Get the data and remove originaltitle, isAdult, endYear


def transform_user_details(csv_full_name):
    newuser_data = []
    try:
        with open(csv_full_name, newline='') as csv_file:
            user_details_csv = csv.reader(csv_file, delimiter=',')

            for rowlist in user_details_csv:
                transformed_row = []
                if rowlist[0] == "movie" and int(rowlist[4]) >= 2015:
                    transformed_row.append(rowlist[0].capitalize())  # titleType
                    transformed_row.append(rowlist[1].capitalize())  # primaryTitle
                    transformed_row.append(rowlist[4])               # startYear
                    transformed_row.append(rowlist[6])               # runtimeMinutes
                    transformed_row.append(rowlist[7].capitalize())  # genres
                    newuser_data.append(transformed_row)
            return newuser_data
    except FileNotFoundError as ermsg:
        print("Excuuuse me! Please make sure a file exists")
        print(ermsg)
    finally:
        print("execution doneee")


new_trans_data = transform_user_details('imdb_title.csv')
print(new_trans_data)

# Let create a function to write our transformed data
#   write to csv


def create_new_csv_user_data(transformed_data, new_user_file_name):
    # have transformed data
    # open new file
    new_file = open(new_user_file_name, 'w', newline='')

    # write to that file
    try:
        with new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerows(transformed_data)

    except NameError as ermsg:
        print("Excuuuse me! Please make sure data list exists ands is spelt right!")
        print(ermsg)
    finally:
        print("execution doneee")


create_new_csv_user_data(new_trans_data, 'imdb_transformed_csv.csv')

