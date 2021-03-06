#visualizes data parsed by the parse function
#Charles Ritter 2017

from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

import parse

def visualize_days():

    """Visualize data by day of the week in a line graph"""

    #grab our parsed data
    data_file = parse.parse(parse.MY_FILE, ",")

    #make a new variable, 'counter', from iterating through each
    #line of data in the parsed data, and count how many incidents
    #happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    #separate the x-axis data (the days of the week) from the
    #'counter' variable form the y-axis data (the number of)
    #incidents for each day)

    #data
    data_list = [
    counter["Monday"],
    counter["Tuesday"],
    counter["Wednesday"],
    counter["Thursday"],
    counter["Friday"],
    counter["Saturday"],
    counter["Sunday"]
    ]
    #labels
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    #with that y-axis data, assign it to a matplotlib instance
    plt.plot(data_list)

    #create the amount of ticks needed for our x-axis, and assign
    #the labels
    plt.xticks(range(len(day_tuple)), day_tuple)

    #title the plot
    plt.title("The number of incidents occurring on each day of the week")

    #save the plot
    plt.savefig("Days.png")

    #close the plot
    plt.clf()

def visualize_type():
    """Visualize data by category in a bar graph"""

    # grab our parsed data
    data_file = parse.parse(parse.MY_FILE, ",")

    # make a new variable, 'counter', from iterating through each line
    # of data in the parsed data, and count how many incidents happen
    # by category
    counter = Counter(item["Category"] for item in data_file)

    # Set the labels which are based on the keys of our counter.
    # Since order doesn't matter, we can just used counter.keys()
    labels = tuple(counter.keys())

    # Set exactly where the labels hit the x-axis
    xlocations = np.array(range(len(labels))) + 0.5

    # Width of each bar that will be plotted
    width = 0.5

    # Assign data to a bar plot (similar to plt.plot()!)
    plt.bar(xlocations, counter.values(), width=width)

    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # Give some more room so the x-axis labels aren't cut off in the
    # graph
    plt.subplots_adjust(bottom=0.5)

    # Make the overall graph/figure is larger
    plt.rcParams['figure.figsize'] = 12, 8

    #titles the plot
    plt.title("The frequency of each category of incident")

    # Save the graph!
    plt.savefig("Type.png")

    # Close plot figure
    plt.clf()

def main():
    visualize_days()
    visualize_type()

if __name__ == "__main__":
    main()
