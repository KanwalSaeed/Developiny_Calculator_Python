print("PYTHON CALCULATOR")
first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))
print ("OPERATION TYPES")
print("+ for Addition")
print("- for Subtration")
print("* for Multipication")
print("/ for Divission")
operator = input("Please select any one of above option: ")
result = 0
if operator == "+" :
    result = first_number + second_number
if operator == "-" :
    result = first_number - second_number
if operator == "*" :
    result = first_number * second_number
if operator == "/" :
    result = first_number / second_number

print(f"Result: {result}")