import gspread
import re
import pandas as pd
import datetime
from utils.scrape import Scrape

daily = Scrape()


class Google:

    def __init__(self):
        self.cred = 'credentials.json'

    def get_data(self):
        # set credentials
        gc = gspread.service_account(self.cred)

        # Open a sheet and create dataframe
        wks = gc.open("Promised_Neverland_Data").sheet1
        data = wks.get_all_values()
        headers = data.pop(0)
        df = pd.DataFrame(data, columns=headers)

        return df

    def add_row(self):
        # score, users = data
        new_data = ['MAL']
        new_data = new_data + daily.get_current_score()
        today = datetime.date.today().strftime("%m/%d/%Y")
        new_data.append(today)

        new_df = pd.Series(new_data, index=['Source', 'Score', 'Users', 'Date'])
        dataframe = self.get_data()
        dataframe = dataframe.append(new_df, ignore_index=True)
        
        gc = gspread.service_account(self.cred)
        wks = gc.open("Promised_Neverland_Data").sheet1
        wks.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())

        print('updated sheet')

def run(event, context):
    g = Google()
    g.add_row()