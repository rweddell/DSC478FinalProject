
import pandas as pd

# TODO: this class should check for user profiles or create new ones


class UserData:
    class UserProfile:
        def __init__(self, name, preferences=None):
            self.name = name
            self.preferences = preferences

    def __init__(self, name, preferences=None):
        self.user = UserData.UserProfile(name, preferences)

    def get_profile(self):
        # TODO: check if a text file(?) exists as user.name.txt
        try:
            df = pd.read_csv(str(self.user.name)+'.csv')
        except (FileNotFoundError):
            # TODO: no file found, so create a new csv for that user
            df = pd.DataFrame(self.user.preferences)
            df.to_csv('/DataStorage/' + self.user.name)
            print('Profile does not exist. Created new file')
        return df

    def update_profile(self):
        # TODO: can update new user preferences here
        # add to preferences
        # overwrite csv file?
        pass
