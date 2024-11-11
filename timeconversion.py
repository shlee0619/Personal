#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    period = s[-2:]  
    hour, minute, second = map(int, s[:-2].split(':'))

    
    if period == "PM":
        if hour != 12:      
            hour += 12
    else:  # AM
        if hour == 12:      
            hour = 0

    
    return f"{hour:02}:{minute:02}:{second:02}"
    
if __name__ == '__main__':
    

    s = input()

    result = timeConversion(s)

    print(result)