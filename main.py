# UTF-8 CRLF
# Done in REPL.IT & Python 3.8.4 32-bit interpreter
# Reproduction without citation is exclusively NOT permitted
# Licensed under GNU GPLv3.0

# Copyright (c) 2022 Tyler Peppy @ OCDSB

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import time
import os
import math
import numpy as np
from SleepScore import *
from datetime import datetime
from datetime import date

MAGENTA = "\u001b[35m"
BLACK = "\033[0;30m"
YELLOW = "\u001b[33m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
RESET = "\u001b[0m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"

name = ""

current = [0,0,0] # Current Date As Array Instead Of 3 Vars
birth = [0,0,0]   # Birth Date As Array Instead Of 3 Vars

daysOld = 0       # Variable Storing How Old The User Is
numLeapYears = 0  # Variable To Store How Many Leap Years The User Has Endured

d1 = 0            # Temporary Variables To Store User's dates
d2 = 0

weeklyHours = 0 # Hours Slept During Week
endlyHours = 0  # Hours Slept During Weekend

weekDays = 0    # Number Of Weekdays
endDays = 0     # Number Of Weekends

totalHours = 0  # Total Slept Hours

totalWeek = 0  # Total Hours On Week
totalEnd = 0   # Total Hours On Weekend 

ageBreakdown = [0,0,0,0,0,0] # Array to Store YY/MM/DD/HH/MM/SS BrokenDown Time (PrettyPrint)

today = date.today() # Define Current Date



def intro():
  '''
    Function That Prints A Text Array That Appears As An ASCII Banner
  '''
  print("  _____ _                    _____      _            _       _               ")
  print(" / ____| |                  / ____|    | |          | |     | |              ")
  print("| (___ | | ___  ___ _ __   | |     __ _| | ___ _   _| | __ _| |_ ___  _ __   ")
  print(" \___ \| |/ _ \/ _ | '_ \  | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|  ")
  print(" ____) | |  __|  __| |_) | | |___| (_| | | (__| |_| | | (_| | || (_) | |     ")
  print("|_____/|_|\___|\___| .__/   \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|     ")
  print("                  | |                                                        ")
  print("                  |_|                                                        ")
  print("                              By: Tyler Peppy                                ")
  time.sleep(2.5)
  os.system('clear')
def playAgain():     
  '''
    Function Prompting User To Play Again Or Not (Error-trapping)
  '''
  while True:        # Trap User In Loop To Enter Choice Until Proper Data Is Recieved
    try:             # Try To Gain Input   
      choice = input(BLUE+"\nWould You Like To Play Again? 'y' To Continue, And 'n' To Exit: "+RESET)
    except ValueError:  
      print(RED+"\nInvalid Choice!"+RESET)
    else:                         # If Input Doesn't Raise 'ValueError'
      if (choice in ""):          # If 'ENTER' key is used
        print(RED+"\nInvalid Choice!"+RESET)
      elif(choice not in "yYnN"): # If No Y Or N Is Recieved (Improper Charecter) 
        print(RED+"\nInvalid Choice!"+RESET)
      elif (choice in "yY"):      # If 'Y' Recieved, Return True
        return True
      elif (choice in "nN"):      # If 'N' Recieved, Return False And Thank User
        print(GREEN+"\nThanks For Playing!"+RESET)
        return False

def getBirthDate():  
  '''
    Function Attempting To Gain The User's Valid Birthdate
  '''
  
  global birth         # Declare Birthdate Array As Global, As It's Used Elsewhere As Well
  global age
  
  while True:
    try:
      age = int(input(BLUE+"\nWhat's your age?: "+RESET))
    except ValueError:
      print(RED+"\nInvalid Choice!"+RESET)
    else:
      if (age <= 0):
        print(RED+"\nCan't Be Less Than Or Equal To Zero Years!"+RESET)
      elif (age > 100):
        print(RED+"\nToo Old"+RESET)
      else:
        break
        
  
  while True:          # Error-trapped Gaining Of Birth Year (1-2099)
    try:
      birth[0] = int(input(BLUE+"\nWhat's Your Birth Year (YYYY): "+RESET))  # Check Birth Year And Store It In Index0 Of Array
    except ValueError:
      print(RED+"\nYou Didn't Enter A Valid Month!"+RESET) 
    if (birth[0] <= 0):                                                  # Can't Have Negative Years, Or 0 Years
      print(RED+"\nYear Can't Be Smaller Or Equal To 0"+RESET)
    elif (birth[0] > 2100):                                              # Put A Cap On The Max Year For Birth
      print(RED+"\nYear too Large"+RESET)
    elif (birth[0] > today.year):
      print(RED+"\nYou Can't Be Born In The Future!"+RESET)
    elif (birth[0] <= (today.year - age)-2):
      print(RED+"\nInvalid Year!"+RESET)
      print(RED+"You're Born CIRCA:",(today.year - age),"(±1 Year)"+RESET)
    elif (birth[0] >= (today.year - age)+2):
      print(RED+"\nInvalid Year!"+RESET)
      print(RED+"You're Born CIRCA:",(today.year - age),"(±1 Year)"+RESET)
    else: 
      break                                                              # Continue Logic On Valid Input, Not Caught In Error-Filter
  
  while True:    # Error-Trapped Gaining Of Birth Month
    try:
      birth[2] = int(input(BLUE+"What's Your Birth Month (MM): "+RESET))  # Check Birth Month And Store it In Index1 Of Array
    except ValueError:
      print(RED+"\nYou Didn't Enter A Valid Month!"+RED)     
    if (birth[2] > 12):                                                   # Can't Have More Than 12 Months
      print(RED+"\nThere Aren't More Than 12 Months In A Year!"+RESET)
    elif (birth[2] <= 0):                                                 # Can't Have Less Than 0 Months Or 0 Months
      print(RED+"\nValue Too Small!"+RESET)
    else:
      break

  while True:                                                             # Error-Trapped Gaining Of Birthdate
    try:
      birth[1] = int(input(BLUE+"What's Your Birthday (DD): "+RESET))
    except ValueError:
      print(RED+"\nYou Didn't Enter A Valid Day!"+RESET) 
    if (birth[1] > 31):                                                   # Raise Error When Day Is Greater Than 31 (>31); No Month With 32 Days
      print(RED+"\nThere Aren't More Than 31 Days In A Month!"+RESET)
    elif (birth[1] <= 0):                                                 # Can't Have Too Low Of A Value
      print(RED+"\nValue Too Small!"+RESET)
    else:
      
      if(birth[0]%4 != 0):                                    # If Not A Leap Year
        
        if(birth[2] in [1,3,5,7,8,10,12] and birth[1] > 31):  # If A 31 Day-Month, Don't Accecpt Larger Than 31 Days
          print(RED+"\nBad Day!"+RESET)
        elif (birth[2] in [4,6,9,11] and birth[1] > 30):      # If A 30 Day-Month, Don't Accecpt Larger Than 30 Days
          print(RED+"\nBad Day!"+RESET)
        elif (birth[2] == 2 and birth[1] > 28):               # If A 28 Day Month (Non-Leap), Don't Accecpt Larger Than 28 Days
          print(RED+"\nBad Day!"+RESET)
        else:
          break
      elif(birth[0]%4 == 0 and birth[0]%100 != 0) or (birth[0]%400 == 0):  # If A Leap Year
        if(birth[2] in [1,3,5,7,8,10,12] and birth[1] > 31):               # If A 31-Day Month, Don't Accecpt Larger Than 31 Days
          print(RED+"\nBad Day!"+RESET)
        elif (birth[2] in [4,6,9,11] and birth[1] > 30):                   # If A 30-Day Month, Don't Accecpt Larger Than 30 Days
          print(RED+"\nBad Day!"+RESET)
        elif (birth[2] == 2 and birth[1] > 29):                            # If A 29-Day Month, Don't Accecpt Larger Than 29 Days (Feb)
          print(RED+"\nBad Day!"+RESET)
        else:
          break
    
  print(MAGENTA+"\nEntered Date! (DD/MM/YYYY):",birth[1],"/",birth[2],"/",birth[0],""+RESET)  # Print The User's Entered Date
  date_time = date(birth[0],birth[2],birth[1])
  d = date_time.strftime(PURPLE+"\nPretty Print: %A, %d %B, %Y"+RESET)
  print(d)

def getCurrentDate(): 
  '''
    Function To Gain User's Input For Current Date, While Error Trapping Accecptable YYYY, MM, And DD Values
  '''
  global current
  
  while True: 
    
    try:                 # Try To Gain User's Selection Of Using Automatic Date Or Manually Enter It
      currentDate = input(YELLOW+"\nUse Current Date? 'y' To Continue, Or 'n' To Manually Enter Date: "+RESET)
    except ValueError:
      print(RED+"\nI Need A Definitive Answer!"+RESET)
    else:
      
      if (currentDate in ""):                              # Error-Trap Enter Key
        print(RED+"\nI Need A Definitive Answer!"+RESET)
      elif (currentDate not in "yYnY"):                    # Error-Trap Invalid Charecter
        print(RED+"\nInvalid Answer"+RESET)
      elif (currentDate in "yY"):                          # Accecpt 'y or Y', and CurrentDate Array Has YY/DD/MM Stored In Index 0,1,2
        current[0] = today.year
        current[1] = today.day
        current[2] = today.month
        break                                              # Don't Continue Prompting User For Date, It Has Been Calculated Already 
      else:
              
        while True:                                       # Trap User In Infinite Loop For Input For Year Value (YY)               
          try:
            current[0] = int(input(BLUE+"\nWhat's Today's Year (YYYY): "+RESET))
          except ValueError:
            print(RED+"\nYou Didn't Enter A Valid Year!"+RESET) 
          if (current[0] <= 0):                           # Self-Explanatory, No Year Smaller Than Or Equal To 0
            print(RED+"\nCan't Have Year 0 Or Less"+RESET)
          elif (current[0] < birth[0]):                   # Can't Have A Year Smaller Than Birth Year
            print(RED+"\nCan't have A Year Smaller Than Your Birth Year!"+RESET)
          elif (current[0] >= 2100):
            print(RED+"\nInvalid Year (Too Large)"+RESET)
          else:
            break  
      
        while True:                                       # Trap User In Infinite Loop For Input For Month Value (MM)
          try:
            current[2] = int(input(BLUE+"What's Today's Month (MM): "+RESET))
          except ValueError:
            print(RED+"\nYou Didn't Enter A Valid Month!"+RESET) 
          if (current[2] > 12):
            print(RED+"\nThere Aren't More Than 12 Months In A Year"+RESET)
          elif (current[2] <= 0):
            print(RED+"\nValue Too Small!"+RESET)
          else:
            break
    
        while True:                                        # Trap User In Infinite Loop For Input For Day Value (DD)
          try:
            current[1] = int(input(BLUE+"\nWhat's Today's Day (DD): "+RESET))
          except ValueError:
            print(RED+"\nYou Didn't Enter A Valid Day!"+RESET) 
          if (current[1] > 31):                            # No More Than 31 Days In A Month Maximum
            print(RED+"\nThere Aren't More Than 31 Days In A Month!"+RESET)
          elif (current[1] <= 0):                          # No Less Than 1 Day In A Month
            print(RED+"\nValue Too Small!"+RESET)
          else:

            if(current[0]%4 != 0):                                    # If Not A Leap Year
              
              if(current[2] in [1,3,5,7,8,10,12] and current[1] > 31):  # If A 31 Day-Month, Don't Accecpt Larger Than 31 Days
                print(RED+"\nBad Day!"+RESET)
              elif (current[2] in [4,6,9,11] and current[1] > 30):      # If A 30 Day-Month, Don't Accecpt Larger Than 30 Days
                print(RED+"\nBad Day!"+RESET)
              elif (current[2] == 2 and current[1] > 28):               # If A 28 Day Month (Non-Leap), Don't Accecpt Larger Than 28 Days
                print(RED+"\nBad Day!"+RESET)
              else:
                return
                
            elif(current[0]%4 == 0 and current[0]%100 != 0) or (current[0]%400 == 0):  # If A Leap Year
              if(current[2] in [1,3,5,7,8,10,12] and current[1] > 31):                 # If A 31-Day Month, Don't Accecpt Larger Than 31 Days
                print(RED+"\nBad Day!"+RESET)
              elif (current[2] in [4,6,9,11] and current[1] > 30):                     # If A 30-Day Month, Don't Accecpt Larger Than 30 Days
                print(RED+"\nBad Day!"+RESET)
              elif (current[2] == 2 and current[1] > 29):                              # If A 29-Day Month, Don't Accecpt Larger Than 29 Days (Feb)
                print(RED+"\nBad Day!"+RESET)
              else:
                return
            
            
  print(MAGENTA+"\nCurrent Date! (DD/MM/YYYY):",current[1],"/",current[2],"/",current[0])  # Print Current Used Date (Current Day)
  date_time = date(current[0],current[2],current[1])  # Create DateTime Object From Ints
  d = date_time.strftime(PURPLE+"\nPretty Print: %A, %d %B, %Y"+RESET)  # Create String From Date Object
  print(d)  # Print Text Date Object

def getDiff(date1, date2):  # Function To Return Time Delta In Days From 2 DateTime Objects (date1, date2)
  '''
    Function To Get Difference Between 2 'dateTime' Objects, Taking Arguments Of EndDate - StartDate
  '''
  
  delta = date1 - date2
  return delta.days

def getInformation():       # Properly Error-Trapped Function To Gain User Info
  '''
    Function To Get User's Personal Information, Taking No Input, Causing Console Window To Prompt For User Info
  '''
  global birth
  global current
  global name
  
  while True:               # Error-Trapped Way To Get User Name As Correct String
    try:
      name = input(BLUE+"What's Your Name?: "+RESET)
    except ValueError:
      print("You Didn't Enter A Valid Name!")
    else:
      print(YELLOW+"\nHello "+name+", Ready To Calculate Your Dormant Age?"+RESET)
      break

  print(GREEN+"\nTime To Get Your Birthdate!"+RESET)
  getBirthDate()
  print(GREEN+"\nTime To Get The Current Date!"+RESET)
  getCurrentDate()

def breakdown(totalHours):
  '''
    Function To Take Argument Of 'TotalHours' -> Total Hours To Break Down Into
    Different Forms (YYYY,MM,DD,HH,MM,SS) *Note, This Function Doesn't Take Hours
    And Break Them Individually, But Shows The Hours In A Pretty Print Format
  '''
  
  ageBreakdown[0] = totalHours/8760 # Convert TotalHours To Years
  
  result = math.modf(ageBreakdown[0])  # Split Decimal From Years Calculation (Remainder) And Get Months
  ageBreakdown[1] = result[0]*12
  
  result = math.modf(ageBreakdown[1]) # Split Months From Decimal And Convert Remainder To Days
  ageBreakdown[2] = result[0]*30.417

  result = math.modf(ageBreakdown[2]) # Split Days From Decimal And Convert Remainder To Hours
  ageBreakdown[3] = result[0]*24

  result = math.modf(ageBreakdown[3]) # Split Hours From Decimal And Convert Remainder To Minutes
  ageBreakdown[4] = result[0]*60

  result = math.modf(ageBreakdown[4]) # Split Minutes From Decimal and Convert Remainder To Seconds
  ageBreakdown[5] = result[0]*60
  
  print(GREEN+"\nYour Sleep Statistics:"+RESET)  # Print Breakdown Of Time (Consecutive)
  print(YELLOW+"Years:",int(ageBreakdown[0]))
  print("Months:",int(ageBreakdown[1]))
  print("Days:",int(ageBreakdown[2]))
  print("Hours:",int(ageBreakdown[3]))
  print("Minutes:",int(ageBreakdown[4]))
  print("Seconds:",ageBreakdown[5])
  print("Or,",round(((ageBreakdown[0]/age)*100), 3),"% Of Your Life!")
  
  
intro()  # Print Intro Banner

while True:
  
  getInformation()
  d1 = date(current[0], current[2], current[1])   # YY/MM/DD
  d0 = date(birth[0], birth[2], birth[1])         # YY/MM/DD
  daysOld = getDiff(d1, d0)
  
  for x in range (birth[0], current[0]):
    if(x%4 == 0 and x%100 != 0) or (x%400 == 0):  # Calculate How Many Leap Years Between The Range Of Birthdate -> Current Date
      numLeapYears += 1
  print(YELLOW+"\nYou Are:",daysOld,"Days Old! (Including)",numLeapYears,"Leap Years"+RESET)   # Don't Add Leap Years, Python Timedelta Object Counts This Already!

  while True:
    try:
      weeklyHours = int(input(BLUE+"\nHow Many Hours Do You Average Sleeping Per WEEK NIGHT: "+RESET))
    except ValueError:
      print(RED+"\nValues Aren't Optional!"+RESET)
    else:
      if(weeklyHours > 24): 
        print(RED+"\nYou Can't Have More Than 24H Of Sleep In A Day..."+RESET)
      elif(weeklyHours <= 0):
        print(RED+"\nYou Can't Have Less Than 0H Of Sleep In A Day..."+RESET)
      else:
        break
        
  while True:
    try:
      endlyHours = int(input(BLUE+"\nHow Many Hours Do You Average Sleeping Per WEEKEND: "+RESET))
    except ValueError:
      print(RED+"\nValues Aren't Optional!"+RESET)
    else:
      if(endlyHours > 24): 
        print(RED+"\nYou Can't Have More Than 24H Of Sleep In A Day..."+RESET)
      elif(endlyHours <= 0):
        print(RED+"\nYou Can't Have Less Than 1H Of Sleep In A Day..."+RESET)
      else:
        break  

  weekDays = np.busday_count(d0, d1)
  endDays = daysOld - weekDays

  totalWeek = weekDays*weeklyHours
  totalEnd = endDays*endlyHours

  print(MAGENTA+"\nYou Have Spent",totalWeek+totalEnd,"Hours Sleeping!"+RESET)
  breakdown(totalWeek+totalEnd)
  sleepScore(age, (weeklyHours + endlyHours)/2)

  if(playAgain() == False):
    break
  else:
    print("")
  