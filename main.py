from art import logo

print(logo)
import os
def calculator():
  while True:
      # Initialize variables
      result = 0
      operation_dict = {'+': 'addition', '-': 'subtraction', '*': 'multiplication', '/': 'division'}

      # Ask for the first number
      first_number = float(input("What's the first number? "))

      while True:
          # Display available operations
          print("\nOperations:")
          for operator in operation_dict:
              print(operator)

          # Ask for the desired operation
          chosen_operation = input("Pick an operation: ")

          # Check if the operation is valid
          if chosen_operation not in operation_dict:
              print("Invalid operation. Please choose a valid operator.")
              continue

          # Ask for the next number
          next_number = float(input(f"What's the next number? ({operation_dict[chosen_operation]}) "))

          # Perform the operation
          if chosen_operation == '+':
              result = first_number + next_number
          elif chosen_operation == '-':
              result = first_number - next_number
          elif chosen_operation == '*':
              result = first_number * next_number
          elif chosen_operation == '/':
              if next_number != 0:
                  result = first_number / next_number
              else:
                  print("Error: Division by zero.")
                  continue

          print(f"\nResult after {operation_dict[chosen_operation]}: {result}")

          # Ask if the user wants to continue
          continue_calculation = input("Type 'y' to continue calculating with the new figure, or type 'n' to start a new calculation: ")
          if continue_calculation.lower() == 'y':
              first_number = result
          elif continue_calculation.lower() == 'n':
              break  # Exit the inner loop to start a new calculation
          else:
              print("Invalid input. Exiting the calculator.")
              return

# Run the calculator
calculator()
