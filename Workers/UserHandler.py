
import pandas as pd

# TODO: this class should check for user profiles or create new ones

class UserHandler:
    def __init__(self, name, preferences):
        self.cur_name = name
        self.cur_prefs = preferences

    def get_profile(self, name, preferences=None):
        # checks if a csv file(?) exists as user.name.txt
        try:
            df = pd.read_csv(name+'.csv')
        except FileNotFoundError:
            # TODO: no file found, so create a new csv for that user
            # updated for new login?
            self.cur_name = name
            self.cur_prefs = preferences
            df = pd.DataFrame(preferences)
            df.to_csv('/DataStorage/' + name)
            print('Profile does not exist. Created new file')
        return df

    def update_profile(self, new_prefs):
        # new_prefs should be a DataFrame
        if new_prefs == None:
            print('Yo, that doesn\'t work')
            return
        else:
            # TODO: can update new user preferences here
            new_prefs.to_csv(str(self.cur_name) + '.csv')
