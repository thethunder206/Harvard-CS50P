'Bank accounts created by Aarav Sharma in 2023'

import csv
import re

__password = 'CS50P'

def clear(filename='accounts.csv'):
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+")
    f.close()


def add_account(name=None, balance=None, pin=None):
    if not (isinstance(name, str)):
        raise ValueError('Please enter name with no numbers')
    if not (isinstance(balance, int)):
        raise ValueError('Please enter balance with only numbers')
    if not (isinstance(pin, int)):
        raise ValueError('Please enter pin with only numbers')

    with open('accounts.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, balance, pin])


def remove_account(name):
    with open('accounts.csv', 'r') as f:
        lines = f.readlines()
    with open('accounts.csv', 'w') as f:
        for line in lines:
            if line.split(',')[0] != name:
                f.write(line)


def deposit(name, amount):
    if not (isinstance(name, str)):
        raise ValueError('Please enter name with no numbers')
    if not (isinstance(amount, int)):
        raise ValueError('Please enter amount with only numbers')

    r = csv.reader(open('accounts.csv'))
    lines = list(r)
    for i in range(0, len(lines)):
        if lines[i][0] == name:
            lines[i][1] = int(lines[i][1]) + int(amount)
            writer = csv.writer(open('accounts.csv', 'w', newline=''))
            writer.writerows(lines)
            return

    raise ValueError('Account not found')

def withdraw(name, amount, passing):
    if not (isinstance(name, str)):
        raise ValueError('Please enter name with no numbers')
    if not (isinstance(amount, int)):
        raise ValueError('Please enter amount with only numbers')
    if not (isinstance(amount, int)):
        raise ValueError('Please enter pin with only numbers')

    r = csv.reader(open('accounts.csv'))
    lines = list(r)
    for i in range(0, len(lines)):
        if lines[i][0] == name and __password == passing:
            if int(lines[i][1]) >= int(amount):
                lines[i][1] = int(lines[i][1]) - int(amount)
                writer = csv.writer(open('accounts.csv', 'w', newline=''))
                writer.writerows(lines)
                return
            else:
                raise ValueError('Insufficient balance')

    raise ValueError('Account not found or pin is incorrect')


def balance(name):
    if bool(re.search(r'\d', name)):
        raise ValueError('Please enter name with no numbers')

    r = csv.reader(open('accounts.csv'))
    lines = list(r)
    for i in range(0, len(lines)):
        if lines[i][0] == name:
            return int(lines[i][1])

    # raise ValueError('Account not found')


def all_info():
    r = csv.reader(open('accounts.csv'))
    lines = list(r)
    return lines

# Adding Accounts
# add_account('shweta', 200, 15)

# Removing Accounts
remove_account('aarav')

# Depositing Money
# deposit('aarav', 400)

# Withdrawing Money
# withdraw('aarav', 200, 'CS50P')

# Check Balance
# print(balance('aarav'))

# All Information(List)
# print(all_info())