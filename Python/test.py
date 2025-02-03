import random

string = "the number is"
bool = True
bool2 = False
bool3 = False
bool4 = False
bool5 = False

random_number1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
random_number2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def result1(a, b):
    global bool2
    if(bool == True):
        print(string, a + b)
        bool2 = True

def result2(a, b):
    global bool2
    global bool3
    print(string, a - b)
    bool3 = True

def result3(a, b):
    global bool3
    global bool4
    print(string, a * b)
    bool4 = True

def result4(a, b):
    global bool4
    global bool5
    print(string, a / b)
    bool5 = True

def result5(a, b):
    print(string, a ** b)
    global bool
    global bool5
    bool5 = False

if(bool2 == True):
    result2

if(bool3 == True):
    result3

if(bool4 == True):
    result4

if(bool5 == True):
    result5

result1(random_number1, random_number2)
result2(random_number1, random_number2)
result3(random_number1, random_number2)
result4(random_number1, random_number2)
result5(random_number1, random_number2)