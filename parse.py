#Python lifejacket #1 Data Visualization Project
#Charles Ritter 2017

import csv
import sys

if len(sys.argv) != 2:
    print("Error: wrong number of arguments")
    print("Usage: python *.py YOURFILE.csv")
    sys.exit()

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""

    #Open CSV file
    opened_file = open(raw_file)

    #Read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    #Setup an empty list
    parsed_data = []

    #Skip over the first line of the file for the headers
    fields = csv_data.next()

    #Iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    #Close CSV file
    opened_file.close()

    return parsed_data

def main():
    """Usage: python parse.py YOURFILE.csv"""

    #opens the file from the cmd line argument
    MY_FILE = sys.argv[1]

    #Call our parse function and give it the needed parameters
    new_data = parse(MY_FILE, ",")

    #prints the Data
    print (new_data)

if __name__ == "__main__":
    main()
