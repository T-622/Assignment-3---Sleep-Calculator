from colors import *

def sleepScore(ages, sleepHours):
  '''
    Function To Take Args Of Age, And Sleep Hours, To Return "Sleep Score", Or How Much Sleep They Are Getting Compared To How Much They Should Be Having
  '''
  print(MAGENTA+"\nYou Are",ages,"!"+RESET)
  
  if (ages > 0 and ages < 3):
    print(YELLOW+"\nSo, You should Be Having 11-14 Hrs Of Sleep"+RESET)
    if(sleepHours >= 11):
      print(GREEN+"And You're Getting:",sleepHours,"/ 14 Hours"+RESET)
    else:
      print(RED+"You Aren't Quite Getting Enough Sleep: ",sleepHours,"/ 14 Hrs Of Sleep"+RESET)

  if (ages > 2 and ages < 6):
    print(YELLOW+"\nSo, You should Be Having 10-13 Hrs Of Sleep"+RESET)
    if(sleepHours >= 10):
      print(GREEN+"And You're Getting:",sleepHours,"/ 13 Hours"+RESET)
    else:
      print(RED+"You Aren't Quite Getting Enough Sleep: ",sleepHours,"/ 13 Hrs Of Sleep"+RESET)

  if (ages > 5 and ages < 14):
    print(YELLOW+"\nSo, You should Be Having 9-11 Hrs Of Sleep"+RESET)
    if(sleepHours >= 9):
      print(GREEN+"And You're Getting:",sleepHours,"/ 11 Hours"+RESET)
    else:
      print(RED+"You Aren't Quite Getting Enough Sleep: ",sleepHours,"/ 11 Hrs Of Sleep"+RESET)

  if (ages > 13 and ages < 18):
    print(YELLOW+"\nSo, You should Be Having 8-10 Hrs Of Sleep"+RESET)
    if(sleepHours >= 8):
      print(GREEN+"And You're Getting:",sleepHours,"/ 10 Hours"+RESET)
    else:
      print(RED+"You Aren't Quite Getting Enough Sleep: ",sleepHours,"/ 10 Hrs Of Sleep"+RESET)

  if (ages > 17 and ages < 26):
    print(YELLOW+"\nSo, You should Be Having 7-9 Hrs Of Sleep"+RESET)
    if(sleepHours >= 7):
      print(GREEN+"And You're Getting:",sleepHours,"/ 9 Hours"+RESET)
    else:
      print(RED+"You Aren't Quite Getting Enough Sleep: ",sleepHours,"/ 9 Hrs Of Sleep"+RESET)

  if (ages > 25 and ages < 65):
    print(YELLOW+"\nSo, You should Be Having 7-9 Hrs Of Sleep"+RESET)
    if(sleepHours >= 7):
      print(GREEN+"And You're Getting:",sleepHours,"/ 9 Hours"+RESET)
    else:
      print(RED+"You Aren't Quite Getting Enough Sleep: ",sleepHours,"/ 9 Hrs Of Sleep"+RESET)

  if (ages > 64):
    print(YELLOW+"\nSo, You should Be Having 7-8 Hrs Of Sleep"+RESET)
    if(sleepHours >= 7):
      print(GREEN+"And You're Getting:",sleepHours,"/ 8 Hours"+RESET)
    else:
      print(RED+"You Aren't Quite Getting Enough Sleep: ",sleepHours,"/ 8 Hrs Of Sleep"+RESET)