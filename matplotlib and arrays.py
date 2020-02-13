import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# CSCI 127, Lab 12                                |
# November 19, 2019                               |
# Michael Gotta                                   |
# -------------------------------------------------


def read_file(file_name):
    file = open(file_name, "r")                # opening the file
    numbers = int(file.readline().strip())
    colleges = np.ndarray(numbers, dtype=object)
    people = np.ndarray(numbers, dtype=int)         # creating some arrays
    count = 0
    for information in file:
        technical = information.strip().split(",")       # looping through the information and stripping un-needed items such as commas
        colleges[count] = technical[0]
        people[count] = int(technical[1])
        count += 1     # increasing the count to find out how many people go to which college

    return colleges, people     # returning two things to make my graph


# -------------------------------------------------
def main(file_name):

    college_names, college_enrollments = read_file(file_name)

    x = np.arange(len(college_enrollments))
    bar = plt.bar(x, college_enrollments, facecolor='b')
    bar[1].set_color("gold")
    bar[3].set_color("gold")
    bar[5].set_color("gold")                                  # all pretty basic pandas/matplotlib stuff here
    plt.xticks(x, college_names)
    plt.yticks(np.arange(0, 4800, 400))
    plt.xlabel('College Name')
    plt.ylabel('College Enrollment')
    plt.grid(False)
    plt.gcf().canvas.set_window_title('Montana State University Fall 2019 Enrollments')
    plt.show()

# -------------------------------------------------


main("fall-2019.csv")    # the file I am using