"""
balance.py
Balance class handles the balance related matter
"""
import constants as const


class Balance:

    journey_history = list()

    def __init__(self, balance):
        """Constructor will be called from Menu class in menu.py to initiate the balance."""

        self.balance = balance
    
    def is_sufficient_balance(self, status, trans_type):
        """Check whether the balance is enough or not."""

        if status == 'IN' and trans_type == 'train' and self.get_current_balance() < const.TRAIN_MAX_FARE:
            return False
        elif status == 'IN' and self.get_current_balance() < const.BUS_CONSTANT_FARE:
            return False
        return True
    
    def calculate_new_balance(self, status, station, trans_type):
        """Calculate the new balance."""

        if status == 'IN' and trans_type == 'train':
            new_balance = self.get_current_balance() - const.TRAIN_MAX_FARE
        elif status == 'IN' and trans_type == 'bus':
            new_balance = self.get_current_balance() - const.BUS_CONSTANT_FARE
        elif status == 'OUT':
            last_IN_trans_type = self.journey_history[-1][2]
            if last_IN_trans_type == 'bus':
                self.journey_history.append([status, station, '-', self.get_current_balance()])
                new_balance = self.get_current_balance()
            else:  # if checking out using 'train'
                start_station = self.journey_history[-1][1]
                start_zones = list(const.STATIONS[start_station])
                destination_zones = list(const.STATIONS[station])

                if 1 not in start_zones or 1 not in destination_zones: # Any one zone outside zone 1
                    new_balance = self.get_current_balance() - 2.00
                elif 1 not in start_zones and 1 not in destination_zones: # Any two zones excluding zone 1
                    new_balance = self.get_current_balance() - 2.25
                elif 1 in start_zones and 1 in destination_zones: # Anywhere in Zone 1
                    new_balance = self.get_current_balance() - 2.50
                elif 1 in start_zones or 1 in destination_zones: # Any two zones including zone 1
                    new_balance = self.get_current_balance() - 3.00 
                elif 1 in (start_zones + destination_zones) and 1 in (start_zones + destination_zones): # Any three zones
                    new_balance = self.get_current_balance() - 3.20

                # put the max fare back (we take max fare in case checked in,
                # but not checked out. Then put it back if checked out)
                new_balance += const.TRAIN_MAX_FARE
                self.balance = new_balance
                
            self.journey_history[-1][3] = new_balance
            self.journey_history.append([status, station, '-', new_balance])
        return new_balance
        
    def is_edge_cases_clear(self, status):
        """Check some of edge cases and return True if all clear."""

        # if the last status was the same as the current one(e.g. check in and then check in again)
        if self.journey_history and status == self.journey_history[-1][0]:
            print('Sorry, last record was checking ' + status)
            return False
        elif not self.journey_history and status == 'OUT':  # if the very first start was with check out
            print('Sorry, your very first time can not be check out')
            return False
        else:
            return True  # edge cases are clear
        
    def set_balance(self, status, station, trans_type):
        """Check whether we have sufficient balance and update it after the trip."""

        is_sufficient_balance = self.is_sufficient_balance(status, trans_type)
        if not is_sufficient_balance:
            print('Insufficient balance')
            return False
        elif self.is_edge_cases_clear(status):
            new_balance = self.calculate_new_balance(status, station, trans_type)
            self.balance = new_balance
            self.journey_history.append([status, station, trans_type, new_balance])
            return True

    def trip_history(self):
        """Print a list of the trip history."""

        print(self.journey_history)
        return True

    def get_current_balance(self):
        """Get the current balance availabel."""

        return self.balance
