# import math
# import os
# import random
# import re
# import sys

# if __name__ == '__main__':
#     N = int(input())

#     if N%2 != 0 or ((N > 5 and N < 21) and N%2 == 0):
#         print("Weird")
#     else:
#         print("Not Weird")


# OR

N = int(input())

if N % 2 != 0:
    print("Weird")
else:
    if N <= 5:
        print("Not Weird")
    elif N <= 20:
        print("Weird")
    else:
        print("Not Weird")