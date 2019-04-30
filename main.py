"""
The Oyster Card Problem

- This is a fare card system which is a limited version of London’s Oyster card system.
- The user has a card with £30 balace initially.
- Balance is deducted after every trip.

To run it from a Mac:
- Open a Terminal window.
- Navigate to oyster_card folder.
- type
python3 main.py
Note: you have to have python 3 installed

main.py is just the main file that will call functions from the classes

- Then the software will guid you through the menu

Written by Hussain Alhassan on April 6, 2019
"""
from classes.menu import Menu

menu_obj = Menu()
menu_obj.main_menu()