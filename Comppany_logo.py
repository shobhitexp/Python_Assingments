import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s=input()
letters=list(s)
count={}
for l in letters:
    if l not in count.keys():
        count[l]=1
    else:
        count[l]+=1    
sorted_count=list(sorted(count.items(),key=lambda x:(-x[1],x[0])))
for i in range(3):
    count_tuple=sorted_count[i]
    print(count_tuple[0],count_tuple[1])
    """A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,
"""
