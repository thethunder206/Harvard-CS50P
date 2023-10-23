# Online Banking System

This is an Online Banking Concept created by Aarav Sharma for my CS50P Final Project.
You can find my youtube explanation videa at this URL: https://www.youtube.com/watch?v=r3JE8ibX1Zw

## Features

* Create Bank Account.
* Add users to Bank Account
* Remove users from Bank Account
* Deposit Money
* Withdraw Money
* Find balance for given users
* Return all users and information if correct password was given

## Prerequisites

Be sure you have the following installed on your development machine:

+ Python >= 3.9
+ Regular Expressions Library
+ pip

## Requirements

+ csv==0.0.13
+ tabulate==0.9.0

Please make sure you have the .csv file in the same repository of the main code
## Documentation

- [Python Documentation](https://docs.python.org/3/)
- [System Documentation](https://docs.python.org/3/library/sys.html)
- [CSV Documentation](https://docs.python.org/3/library/csv.html)
- [Regular Expressions Documentation](https://docs.python.org/3/library/re.html)
## Installation


Installing Regular Expressions Library

```bash
  pip install regex
```

## Code Explanation

To start the code of, you will need to import all the dependencies and to set the master password. I made sure that the password had two underscores, telling ensuring that no one changes the variable.
```python
import csv
import re

__password = 'CS50P'

```
The code here shows a function that just opens and clears the csv file
```python
def clear(filename='accounts.csv'):
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+")
    f.close()

```
### Add Account Function
This part of my code shows will add the information that the user has provided to the program. The code will add this information to the csv file that stores all the data.
```python
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

```

### Remove account Function
Here you can see the remove account function for when the user calls the function to remove an account. The user will give the values of the information needed when the remove account funtion was executed.

```python
def remove_account(name):
    with open('accounts.csv', 'r') as f:
        lines = f.readlines()
    with open('accounts.csv', 'w') as f:
        for line in lines:
            if line.split(',')[0] != name:
                f.write(line)
```

### Deposit to account Function
Here you can deposit money to a spefic account. The code take the information provided when the deposit function was executed. If there is no such account, it will raise a ValueError requesting the user to give vaild information.

```python
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
```

### Withdraw from account Function
Here you can withdraw money from a spefic account. The code will use the information provided from the arguments from the Withdraw Function. If the information was invalid it will return a prompted error, and if the balance was Insufficient the program will let the user know. If the pin was incorrect the program will also let the user know.

```python
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

```

### Find Balance of account Function
Here you can find the balance from a spefic account. The code will take the information from the balance function. The code will return the account name, the total money they have, and their age.

```python
def balance(name):
    if bool(re.search(r'\d', name)):
        raise ValueError('Please enter name with no numbers')

    r = csv.reader(open('accounts.csv'))
    lines = list(r)
    for i in range(0, len(lines)):
        if lines[i][0] == name:
            return int(lines[i][1])
```

### Find all information of bank
Here you can find all of the information stored in the banks file. The information will eaisly be given to the user when prompted to when using the all information function.
```python
def all_info():
    r = csv.reader(open('accounts.csv'))
    lines = list(r)
    return lines
```
## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## License

The MIT License (MIT)

Copyright (c) 2023 Aarav Sharma

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
