"""Write a function called 'square'
Takes one number, returns its square
square(5) → 25"""
def main1():
    num = int(input("Enter a number: "))
    print(f"The square of {num} is {square(num)}")
    
def square(n):
    return n**2

if __name__ == "__main__":
    main1()
    
''' Write a function called 'is_even'
Takes one number, returns True if even, False if odd
is_even(4) → True
is_even(7) → False'''

def main2():
    num = int(input("Enter a number: "))
    print(f"Is {num} even? {is_even(num)}")
    
def is_even(n):
    return n % 2 == 0

if __name__ == "__main__":
    main2()
    
''' Write a function called 'greet_user'
Takes name and age, prints a greeting sentence
greet_user("Ahinsree", 32) →
"Hello Ahinsree! You are 32 years old."'''
def main3():
    name, age = input("Enter your name and age (separated by space): ").split()
    greet_user(name, int(age))
    
def greet_user(name, age):
    print(f"Hello {name}! You are {age} years old.")
    
if __name__ == "__main__":
    main3()