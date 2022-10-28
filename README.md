# Assignment-3---Sleep-Calculator
Sleep Age Calculator

For this program, users were tasked with the idea of creating a calculator, calculating days between birth and current (or manually enterable) date, and calculate how many hours the user had been sleeping for, to then break this down into more understandable time.

Project Criteria:

Write a Python program that
a) asks the user to enter their birthdate
b) asks for the current date
c) calculates how many hours they have slept (assuming that they sleep 8 hrs per day)

Spoiler: this assignment amounts to determining the number of days between the two dates and multiplying that value by 8...
the trick is determining the number of days

Your program should 
make good use of appropriate structures and concepts (specifically: loops, if / elif / else constructs,  error trapping loops, play again loops, etc.)
NB - I do not want you to use classes for this assignment
include well formatted and decriptive input and output messages to the user (with good use of blank lines / spacing, etc.)
appropriate documentation (including: program header, descriptive variable names, comments throughout the code)
Simple version (level 3):
assuming 365 days/year and 30 days/month
assumes that a persons sleeps 8 hrs per night,
asks the user to also enter the current date
More complex (some or all of the following): 
calculate the actual number of days (including leap days, etc.) 
gives the user the option of the current date (automatically determined) or a different (user-specified) date
asks the user for the average number of hours slept per nigh
(what about more/less sleep on weekends)
`pretty prints` the date (with the day of the week!)
This will be most easily accomplished using a `list` variable... see link below
makes appropriate use of functions
other features as determined by you
Hints: 
ask the user for the date elements separately rather than all at once: e.g., ask for the year, then the month and finally the date... 
ask the for the month by number rather than by name --> January =  1, February =  2...
error trap each entry separately... what restrictions there are on each value
the datetime library might aldso be helpful...
Expected duration: ~1 week to design, develop, test and refine
