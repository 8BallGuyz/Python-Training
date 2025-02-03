digit1 = input("type in the first digit")
resultChecker = False

if digit1:
    digit2 = input("type in the 2nd digit")
    digit1Result = int(digit1)

if digit2:
    formula = input("type in the symbol")
    digit2Result = int(digit2)

if formula == "+":
    result1 = print(digit1Result + digit2Result)
    resultChecker = True
    result1

if formula == "-":
    result1 = print(digit1Result - digit2Result)
    resultChecker = True
    result1

if formula == "*":
    result1 = print(digit1Result * digit2Result)
    resultChecker = True
    result1

if formula == "/":
    result1 = print(digit1Result / digit2Result)
    resultChecker = True
    result1

if formula == "**":
    result1 = print(digit1Result ** digit2Result)
    resultChecker = True
    result1

if resultChecker == True:
    formula2 = input("type in the symbol")

if formula2 == "+":
    result1 = print(digit1Result + digit2Result)
    resultChecker = True
    result1

if formula2 == "-":
    result1 = print(digit1Result - digit2Result)
    resultChecker = True
    result1

if formula2 == "*":
    result1 = print(digit1Result * digit2Result)
    resultChecker = True
    result1

if formula2 == "/":
    result1 = print(digit1Result / digit2Result)
    resultChecker = True
    result1

if formula2 == "**":
    result1 = print(digit1Result ** digit2Result)
    resultChecker = True
    result1