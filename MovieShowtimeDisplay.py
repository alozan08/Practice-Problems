'''
    Write a program that reads movie data from a CSV file and output the data in a formatted table
    The first reads the name of the CSV file from the user. The program then reads the CSV file and outputs
    the contents according to the following requirements:
        Each row contains the title, rating, and all showtimes of a unique movie
        A space is placed before and after each vertical separator (|) in each roq
        Column 1 displays the movie titles and is left justified with a min of 44 chars
        If the movie title has more than 44 chars, output the first 44 chars only
        Column 2 displays the movie ratings and is right justified with a min of  5 chars
        Column 3 displayss all the showtimes of the same movie, separate by a space
    Each row of the CSV file contains the showtime, title, and rating of a movie
    Assume the data of the same movie are grouped in consecutive rows
'''
import csv

movies = {}

with open('movies.csv') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if row[1] in movies:
            movies[row[1]] += [row[0]]
        else:
            movies[row[1]] = [row[2], row[0]]
for title, details in movies.items():
    showtimes = details[1:]
    showtimes = ' '.join(showtimes)
    name = title[:44]
    rating = details[0]
    print(f'{name:<44} | {rating:>5} | {showtimes}')