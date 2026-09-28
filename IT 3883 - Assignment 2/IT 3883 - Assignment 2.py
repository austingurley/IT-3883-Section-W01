# IT 3883 - Assignment 2.py
# IT3883/Section W01
# Austin Gurley
# Assignment #2
# Due Date: 10/02/2026
# Purpose: This program reads an input file where each line holds a
#          student's name followed by 6 scores. It calculates each
#          student's final average and prints each student's name and
#          average, sorted in descending order by grade.
# Resources used:
#   - Python documentation: file I/O (open), str.split(), list.sort()
#     with key/reverse, and f-string formatting
#     (https://docs.python.org/3/)

INPUT_FILE = "Assignment2input.txt"


def read_students(filename):
    # Return a list of (name, average) tuples from the input file.
    students = []
    with open(filename, "r") as file:
        for line in file:
            fields = line.split()
            if not fields:          # skip blank lines
                continue
            name = fields[0]
            scores = [float(score) for score in fields[1:]]
            average = sum(scores) / len(scores)
            students.append((name, average))
    return students


def main():
    students = read_students(INPUT_FILE)

    # Sort by average, highest first
    students.sort(key=lambda student: student[1], reverse=True)

    for name, average in students:
        print(f"{name} {average:.2f}")


if __name__ == "__main__":
    main()
