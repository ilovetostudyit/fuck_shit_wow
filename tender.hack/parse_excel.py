import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from datetime import timedelta
import json
import numpy as np

class year_parse():
    def __init__(self):
        return
    def name_parse(self, name_of_xlsx, name_of_var):
        print("meow")
        return
        
    def just_parse(self, name_of_xlsx):
        df = pd.read_excel(name_of_xlsx, sheet_name='1')
        dict_for_json = {}
        df.dropna(how='all')
        print("Column headings:")
        for each in df.columns:
            if (each not in [4, 8, 12, 13]):
                df.drop(each, axis = 1, inplace = True)
        i = 0
        print(df[12])
        for each in df[12]:
            temp_t = each
            while (((df[13][i] - temp_t).days) > 0):
                temp_t = (pd.to_datetime(temp_t) + timedelta(days=1))
                curr_date = temp_t
                curr_date = int(curr_date.timestamp())
                if curr_date in dict_for_json:
                    dict_for_json[curr_date] += 1
                else:
                    dict_for_json[curr_date] = 1
            i+=1
            print(i)
        dict_for_json = json.dumps(dict_for_json)
        json_for_visual = json.loads(dict_for_json)
        with open('templates/year.json', 'w') as outfile:
            json.dump(json_for_visual, outfile)
    def execute(self):
        return