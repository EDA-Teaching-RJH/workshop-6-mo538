#Your code goes here. 

import math

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
     return("cannot divide by zero")
     return("result")


def process_list(input_list):
   total =0
   for  item in list:
    try:
        number= int(item)
        total+= number**2
    except (TypeError, ValueError):
        #if  item is not a number skip it
        continue
    return total


def nested_operations(a, b):
    try:
        a= int(a)
        b= int(b)
        try:
           result = a / b
           return(math.sqrt(result))
        except ZeroDivisionError:
           return "cannot divide by zero"
    except ValueError:
        return "invalid input please enter number" 



def process_input():
   try:
      Userinput = input("enter a number: ")
      number = float(Userinput)
      result = number**2
   except ValueError:
      print("invalid input, please enter a value ")
      return None
   finally:
      print("processing complete.")




def main():
   #test part one
   print("part one:", safe_divide(10,0))
   print("part one:" safe_divide(10,2))

   #test part two
   print("part two:"process_list([1,2, 'a',3]))

   ~