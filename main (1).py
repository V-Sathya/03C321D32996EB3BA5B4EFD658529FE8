# 1.1 Implement a recursive function to calculate the factorial of a given number 

"""
year % 4==0
year % 100￼!==0/
year % 400==0

"""
def isLeapyear(year):
  if(year %4==0 and year % 100!=0) or year % 400 ==0:
    return True 
  else:
    return False

year = 2012

if isLeapyear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format (year))
  