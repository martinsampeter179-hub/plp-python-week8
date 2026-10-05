"""
Personal Mini-Toolkit Program
PLP Python - Week 8 Final Project

This program provides a menu-driven interface with three tools:
1. Simple Calculator (Conditionals & Arithmetic)
2. To-Do List Manager (Lists & Loops)
3. Number Guessing Game (Random numbers & Loops)
"""

import random


def run_calculator():
    """Tool 1: Performs basic arithmetic operations between two numbers."""
    print("\n--- Tool 1: Simple Calculator ---")
    print("Operations: + (Add), - (Subtract), * (Multiply), / (Divide)")
    
    op = input("Choose an operation (+, -, *, /): ").strip()
    
    if op not in ['+', '-', '*', '/']:
        print("Invalid operation selected.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
            return
        result = num1 / num2

    print(f"Result: {num1} {op} {num2} = {result}")


def run_todo_list(tasks):
    """Tool 2: Manages a dynamic to-do list using list operations."""
    print("\n--- Tool 2: To-Do List Manager ---")
    
    while True:
        print("\nTo-Do Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Back to Main Menu")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            if not tasks:
                print("Your to-do list is currently empty!")
            else:
                print("\nYour Current Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        elif choice == '2':
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Added: '{new_task}'")
            else:
                print("Task cannot be empty!")
        elif choice == '3':
            if not tasks:
                print("No tasks available to remove.")
            else:
                print("\nYour Current Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                try:
                    task_num = int(input("Enter task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"Removed: '{removed}'")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == '4':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid selection. Please choose options 1 to 4.")


def run_guessing_game():
    """Tool 3: A number-guessing game using loops and conditionals."""
    print("\n--- Tool 3: Number Guessing Game ---")
    secret_number = random.randint(1, 20)
    attempts = 0
    guessed = False
    
    print("I'm thinking of a number between 1 and 20.")
    
    while not guessed:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < 1 or guess > 20:
                print("Please guess a number between 1 and 20!")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You guessed {secret_number} correctly in {attempts} attempt(s)!")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    """Main menu loop driving the toolkit program."""
    # Persistent list data structure passed to the task manager
    todo_tasks = []
    
    print("=" * 40)
    print(" Welcome to Your Personal Mini-Toolkit! ")
    print("=" * 40)
    
    while True:
        print("\n=== Main Menu ===")
        print("1. Simple Calculator")
        print("2. To-Do List Manager")
        print("3. Number Guessing Game")
        print("4. Quit")
        
        user_choice = input("Choose a tool (1-4): ").strip()
        
        if user_choice == '1':
            run_calculator()
        elif user_choice == '2':
            run_todo_list(todo_tasks)
        elif user_choice == '3':
            run_guessing_game()
        elif user_choice == '4':
            print("\nThank you for using the Personal Mini-Toolkit! Goodbye!\n")
            break
        else:
            print(f"\n[!] '{user_choice}' is an invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

