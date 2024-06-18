
import csv

file_path = "C:\\Users\\dell\\OneDrive\\Documents\\flights.csv"

with open(file_path, "r") as file:
    read = csv.reader(file)
    for row in read:
        print(row)







