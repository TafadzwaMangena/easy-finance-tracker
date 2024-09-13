import gspread
from google.oauth2.service_account import Credentials
from simple_term_menu import TerminalMenu
from tabulate import tabulate
from colorama import Fore, Style, init

#To initialize Colorama to be compatible with Windows
init(autoreset=True)

def connect_to_google_sheets(easy_finance_tracker):
    """
    Authenticate and connect to google spreadsheet using json file,
    then open google spread sheet, easy_finance_tracker
    """
    
    SCOPE = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
        ]

    CREDS = Credentials.from_service_account_file('creds.json', SCOPE)
    GSPREAD_CLIENT = gspread.authorize(CREDS)

    SHEET = GSPREAD_CLIENT.open('easy_finance_tracker').sheet1
    return SHEET

def get_data_from_sheet(SHEET):
    """
    Get all data from google spreadsheet, store income in row 1 and expenses from row 2.
    Check if expense data row exists.
    """
    income = float(SHEET.cell(1, 2).value or 0.0) 
    expenses = []
    expense_data = SHEET.get_all_values()[1:] 
    
    for row in expense_data:
        if row[0]:  
            description = row[0]
            amount = float(row[1])
            expenses.append((description, amount))

    return income, expenses


def add_income():
    """
    Get income from user which can be a floating number, 
    cannot be a string and should be positive.
    """
    added_income = float(input(f"{Fore.BLUE}Please enter your income: {Style.RESET_ALL}"))
    print(f"{Fore.YELLOW}Your income has been updated to: {added_income}{Style.RESET_ALL}")

def add_expense():
    """
    Get expenses from user, description of expenses which should
    be a string and amount which should be a positive floating number.
    Add the two and print the expense.
    """
    description = input(f"{Fore.BLUE}Please enter the name for this expense: {Style.RESET_ALL}")
    amount = float(input(f"{Fore.BLUE}Please enter the amount for this expense: {Style.RESET_ALL}"))
    print(f"{Fore.YELLOW}The expense added is '{description}' amounting €{amount}{Style.RESET_ALL}")


def display_budget():
    """
    Calculate total expenses and savings. Display all data received and calculated to user.
    """

options = ["Add Income", "Add Expense", "Display Current Budget", "Exit"]
while True:
    terminal_menu = TerminalMenu(options, title="Select an option:")
    choice = terminal_menu.show()

    if choice == 0:
        add_income()
    elif choice == 1:
        add_expense()
    elif choice == 2:
        display_budget()
    elif choice == 3:
        print(f"{Fore.GREEN}Exiting the program...\nGoodbye!{Style.RESET_ALL} ")
        break
    else:
        print(f"{Fore.RED}The choice you entered is invalid. Please select a valid option.{Style.RESET_ALL}")
        break

