import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    b = list(map(int, input().rstrip().split()))
     
    for i in range(1, n+1):
        print(b[n-i], end=" ")