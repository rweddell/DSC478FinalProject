
import pandas as pd
import os

# TODO: this class should check for user profiles or create new ones


class UserHandler:
    def __init__(self):
        self.current_name = None
        self.current_prefs = None
        self.data_path = os.path.join(os.getcwd(), 'DataStorage')

    def get_profile(self, name, preferences=None):
        # checks if a csv file(?) exists as user.name.txt
        try:
            df = pd.read_csv(name+'.csv')
        except FileNotFoundError:
            # TODO: no file found, so create a new csv for that user
            # updated for new login?
            self.current_name = name
            self.current_prefs = preferences
            df = pd.DataFrame(preferences)
            df.to_csv(os.path.join(self.data_path, name))
            print('Profile does not exist. Created new file')
        return df

    def update_profile(self, new_prefs):
        # new_prefs should be a DataFrame
        if new_prefs is None:
            # should this return a string instead of an exception?
            raise Exception('Found no new preferences to update user profile')
        else:
            # TODO: can update new user preferences here
            try:
                new_prefs.to_csv(str(self.current_name) + '.csv')
            except:
                print('Could not create a new file')

    def make_preferences(self):
        # TODO: figure out what we want to store in user preferences
        # This method will collect information to be stored in the user profile
        pass