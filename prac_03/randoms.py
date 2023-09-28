"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
"""
import random

# 14, 16, 14, 6, 17, 5
# Smallest = 5, largest = 20
"""
What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
"""
# 9, 3, 3, 3, 7, 3
# Smallest = 3, largest = 9
# Could not have produced a 4 as it had a step size of 2 starting from 3
"""
What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
"""
# 3.445381078566844, 4.334660176496087, 3.7974046986478647
# Smallest = 2.5, largest = 5.5
"""
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
print(random.randint(1, 100))
