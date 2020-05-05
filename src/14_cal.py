"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

args = sys.argv

# no month or year provided in args
if (len(args) == 1):
  yy = datetime.now().year
  mm = datetime.now().month
  output = calendar.month(yy, mm)
  print(output)
  print('To display a specific month and year in the past, please pass integers for the month and year as arguments when running the program like so: "14_cal.py [month] [year]"')

else:
  # only one arg passed in, which is assumed to be the month of this year
  if (len(args) == 2) and (0 < int(args[1]) < 13):
    yy = datetime.now().year
    mm = int(args[1])

  elif (len(args) == 2) and (int(args[1]) > 13):
    print('You only provided one argument, which is presumed to be a specific month of this year. Please pass an integer value from 1 to 12 as this argument.')

  # both month and year provided in args
  elif (len(args) == 3):
    yy = int(args[2])
    mm = int(args[1])

  output = calendar.month(yy, mm)
  print(output)


# # My old code using prompted inputs

# yy = input("Input Year: ")
# mm = input("Input Month: ")

# if(yy == "") and (mm == ""):
#     yy = datetime.now().year
#     mm = datetime.now().month
#     output = calendar.month(yy, mm)
#     print(output)

# elif (yy == "") and (mm.isdigit()):
#     yy = datetime.now().year
#     mm = int(mm)
#     output = calendar.month(yy, mm)
#     print(output)

# elif (yy.isdigit()) and (mm == ""):
#     yy = int(yy)
#     mm = datetime.now().month
#     output = calendar.month(yy, mm)
#     print(output)

# elif (yy.isdigit()) and (mm.isdigit()):
#     yy = int(yy)
#     mm = int(mm)
#     output = calendar.month(yy, mm)
#     print(output)