print("Resources opened successfully")

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter dinominator: "))
    result = a / b
    print("Result is : ", result)

except ZeroDivisionError as ze:
    print("An error occurred: invalid literal", ze)

except ValueError as ve:
    print("An error occurred: invalid literal", ve)

# universal exception
except Exception as e:
    print("An error occurred: Division by zero is not allowed", e)

# If app crash without handling errors properly, finally block will call
finally:
    print("Resources closed successfully")

print("End of programme")
