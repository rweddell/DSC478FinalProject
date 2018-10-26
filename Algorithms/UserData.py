
import pandas as pd
#TODO: this file should make a new user profile to
#

class UserData:
    class UserProfile:
        def __init__(self, name, preferences=None):
            self.name = name
            self.preferences = preferences

    def __init__(self, name, preferences=None):
        self.user = UserData.UserProfile(name, preferences)

    def get_profile(self, user):
        # TODO: check if a textfile(?) exists as user.name.txt
        try:
            df = pd.read_csv(str(user.name)+'.csv')
        except:
            #TODO: no file found, so create a new csv for that user
            df = pd.DataFrame(user.preferences)
            df.to_csv('/DataStorage/' + user.name)
            print('Profile does not exist. Created new file')
        return df

    def update_profile(self):
        #TODO: can update new user preferences here
        # add to preferences
        # overwrite csv file?
        pass
