import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    
    '''Function to calculate the total cost'''
    tax = meal_cost* tip_percent/100 + meal_cost* tax_percent/100
    total = meal_cost + tax
    print(round(total))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)