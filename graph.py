#visualizes data parsed by the parse function
#Charles Ritter 2017

from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

import parse

def visualize_days():
    """Visualize data by day of the week"""

    #grab our parsed data
    data_file = parse.parse(parse.MY_FILE, ",")

    #make a new variable, 'counter', from iterating through each
    #line of data in the parsed data, and count how many incidents
    #happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    #separate the x-axis data (the days of the week) from the
    #'counter' variable form the y-axis data (the number of)
    #incidents for each day)
    data_list = [
    counter["Monday"],
    counter["Tuesday"],
    counter["Wednesday"],
    counter["Thursday"],
    counter["Friday"],
    counter["Saturday"],
    counter["Sunday"]
    ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    #with that y-axis data, assign it to a matplotlib instance

    #create the amount of ticks needed fo rour x-axis, and assign
    #the labels

    #save the plot!

    #close the plot

def main():
    visualize_days()

if __name__ == "__main__":
    main()
