#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 12:46:58 2025

@author: cherry
"""
import csv
import os

FILENAME = "expenses.csv"

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses file found. Please make sure 'expenses.csv' exists in the same directory.\n")
        return
    
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        expenses = [row for row in reader if row and len(row) == 3]  # Ignore empty/malformed rows
        
        if len(expenses) <= 1:
            print("No expenses recorded yet.\n")
            return
        
        print("\nDate       | Category   | Amount")
        print("----------------------------------")
        for row in expenses[1:]:
            print(f"{row[0]} | {row[1]} | Rs.{row[2]}")
        print("\n")

def total_spent():
    if not os.path.exists(FILENAME):
        print("No expenses file found. Please make sure 'expenses.csv' exists in the same directory.\n")
        return
    
    total = 0
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                continue  # Skip header row
            if len(row) == 3 and row[2].replace('.', '', 1).isdigit():  # Ensure valid row format and numeric value
                total += float(row[2])
    
    print(f"Total amount spent: Rs.{total}\n")

def main():
    while True:
        print("Expense Tracker")
        print("1. View Expenses")
        print("2. Total Spent")
        print("3. Exit")
        try:
            choice = input("Choose an option: ")
            if choice == "1":
                view_expenses()
            elif choice == "2":
                total_spent()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1-3.\n")
        except EOFError:
            print("Input error detected. Exiting program.")
            break

if __name__ == "__main__":
    main()





