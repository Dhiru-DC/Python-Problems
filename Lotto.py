# P24 Lotto - Draw random number from (1....M)

import random as r

limit = int(input(
    "Enter the maximum number uptil which random number needs to be generated:"))  # end limit of random number generation
try:
    print(r.sample(range(1, limit + 1), 6))
except:
    print("Invalid Limit Entered")

