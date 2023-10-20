import pandas as pd
#import numpy as np
import matplotlib.pylab as plt
#import seaborn as sns

pd.set_option("display.max_columns",30)
plt.style.use('ggplot')
import requests

def prc_get_data_from_url(href):
    # href = "https://data.binance.com/api/v3/ticker/24hr"
    # Above url did nt work I get status code 200. But data.json() fails
    data = requests.get(href)
    #data = requests.post(href)
    if data.status_code != 200:
        print("Data not received, error")
        return None
    print(data)
    data_json = data.json()
    print(type(data_json))
    return data_json

def disp_df_props(df):
    print("Display data frame")
    print(df.shape)
    print(df.info())
    print(df.head(5))
    print(df.dtypes)


def process_binance_tk():
    print("Get data from url")
    href = "https://api.binance.com/api/v3/ticker/24hr"
    #href = "https://data.binance.com/api/v3/ticker/24hr"
    data_json = prc_get_data_from_url(href)
    if data_json is None:
        return

    df = pd.DataFrame(data_json)
    disp_df_props(df)
    print("saving data in csv")
    df.to_csv("cb_binance_ticket_24hr.csv", index=False)


if __name__ == "__main__":
    print("Start main program")
    process_binance_tk()
    print("Ending program")

