# coding=utf-8
"""
menu.py
Menu class handles all the menus to lead the user
"""
from classes.balance import Balance
import constants as const


class Menu:
    
    def __init__(self):
        self.balance_obj = Balance(30.0)

    def is_option_valid(self, option, menu_length):
        """Check whther user entered a valid number from the menu or something else."""

        if option.isdigit() and int(option) in range(1,menu_length + 1):
            return True
        return False

    def station_menu(self, status):
        """Print menu of stations."""

        station_menu = ''
        i = 1
        for station in const.STATIONS:
            station_menu += str(i) + ') ' + station + "\n"
            i += 1
        station_option = input(
'''
Enter the number of the station:
''' 
+ station_menu)
        
        if self.is_option_valid(station_option, len(const.STATIONS)):
            station_name = list(const.STATIONS)[int(station_option)-1]
            if status == 'OUT':
                self.balance_obj.calculate_new_balance(status, station_name, '-')
                self.main_menu()
            else:
                self.transportation_type(status, station_name)
        else:
            print(station_option + ' is not an option. Please enter a number from the menu.')
            self.station_menu(status)

    def transportation_type(self, status, station_name):
        """Print menu of transportation types."""

        trans_option = input(
'''
Enter the number of the option needed:
1) Train trip.
2) Bus trip.
''')
        if self.is_option_valid(trans_option, 2):
            if int(trans_option) == 1:  # i]f train selected
                self.balance_obj.set_balance(status, station_name, 'train')
            else:  # if bus selected
                self.balance_obj.set_balance(status, station_name, 'bus')
            self.main_menu()
        else:
            print(trans_option + ' is not an option. Please enter a number from the menu (transportation_type).')
            self.transportation_type(status, station_name)
            
    def main_menu(self):
        """Print the main menu."""

        option = input(
'''
Enter the number of the option needed:
1) Checking IN.
2) Checking OUT.
3) Print current balance.
4) Print trip history.
5) Exit
''')

        if self.is_option_valid(option, 5):
            int_option = int(option)
            if int_option == 1:
                is_edge_case_clear = self.balance_obj.is_edge_cases_clear('IN')
                if is_edge_case_clear:
                    self.station_menu('IN')
                else:
                    self.main_menu()
            elif int_option == 2:
                is_edge_case_clear = self.balance_obj.is_edge_cases_clear('OUT')
                if is_edge_case_clear:
                    self.station_menu('OUT')
                else:
                    self.main_menu()
            elif int_option == 3:
                print('Your current balance: €' + str(self.balance_obj.get_current_balance()))
                self.main_menu()
            elif int_option == 4:
                self.balance_obj.trip_history()
                self.main_menu()
            else:
                print('Thank you for using our software (^_^)\n')
                raise SystemExit
        else:
            print(option + ' is not an option. Please enter a number from the menu.')
            self.main_menu()
