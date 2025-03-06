# Expense Tracker

## Project Description
The **Expense Tracker** is a simple Python-based CLI (Command Line Interface) application that allows users to track their expenses. It reads expense data from a predefined CSV file and provides functionalities to view expenses and calculate the total amount spent.

## Features
- **View Expenses**: Displays all recorded expenses from the CSV file.
- **Total Spent**: Calculates the total amount spent based on the data in the CSV.
- **Preloaded CSV Data**: Comes with a sample `expenses.csv` file containing predefined expense records.

## Prerequisites
- Python 3.x installed on your system.
- Spyder IDE (Optional) or any Python-compatible editor.

## Setup Instructions
1. Clone or download the project.
2. Ensure `expenses.csv` is in the same directory as `expensestracker.py`.
3. Run the script in Spyder or any Python environment using:
   ```bash
   python expensestracker.py
   ```

## Usage
1. Run the script and choose an option:
   - Press `1` to view recorded expenses.
   - Press `2` to view the total amount spent.
   - Press `3` to exit the program.
2. The script reads expenses from the CSV file and displays relevant information.

## File Structure
```
/expense-tracker
|-- expensestracker.py   # Main script
|-- expenses.csv         # Preloaded expense data
|-- README.md            # Project documentation
```

## Future Enhancements
- Allow users to **add expenses dynamically** via input.
- Implement a **graphical user interface (GUI)** using Tkinter or Flask.
- Provide **expense filtering options** based on date or category.

## Author
Charishma Bonkuri

