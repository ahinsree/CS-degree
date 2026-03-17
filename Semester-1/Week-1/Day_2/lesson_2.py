# Logical operators in Python
# Logical operators are used to combine conditional statements. The three main logical operators in Python are:
# 1. and: Returns True if both statements are true.
# 2. or: Returns True if one of the statements is true.
# 3. not: Reverse the result, returns False if the result is true.
age = 20 
score = 85
# AND operator Both conditions must be true for the result to be true
print( age >= 18 and score >= 80) # True, because both conditions are true
print( age >= 18 and score >= 90) # False, because the second condition is false

# OR operator At least one condition must be true for the result to be true
print( age >= 18 or score >= 90) # True, because the first condition is true
print( age <= 18 or score >= 90) # True, because the second condition is true

# NOT operator Flips the result of the condition
print( not (age >= 18)) # False, because age is greater than or equal to 18
print( not (score >= 90)) # True, because score is less than 90

# Truth Tables
#
# AND Operator
# A     | B     | A and B
#-------|-------|---------
# True  | True  | True
# True  | False | False
# False | True  | False
# False | False | False
#
# OR Operator
# A     | B     | A or B
#-------|-------|--------
# True  | True  | True
# True  | False | True
# False | True  | True
# False | False | False
#
# NOT Operator
# A     | not A
#-------|-------
# True  | False
# False | True
