import gspread
from google.oauth2.service_account import Credentials
from simple_term_menu import TerminalMenu
from tabulate import tabulate
from colorama import Fore, Style, init

#To initialize Colorama to be compatible with Windows
init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('easy_finance_tracker')

def add_income():
    """
    Get income from user which can be a floating number, cannot be a string and should be positive.
    """


def add_expense():
    """
    Get expenses from user, discription of expenses which should be a string and amount which should be a positive floating number. Add the two and print the expense.
    """


def display_budget():
    """
    Calculate total expenses and savings. Display all data received and calculated to user.
    """