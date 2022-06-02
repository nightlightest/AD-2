import main
import pandas as pd
from spyre import server

server.include_df_index = True


class Vhithings(server.App):
    title = "VCI TCI VHI"
    ddd = main.Dataframes('e:\\projects\\datalab1')
    ddd.readdata()
    ddd.changeindexes()
    inputs = [{
        "type": 'dropdown',
        "label": 'NOAA data dropdown',
        "options": [
            {"label": "VCI", "value": "VCI"},
            {"label": "TCI", "value": "TCI"},
            {"label": "VHI", "value": "VHI"}],
        "value": 'GOOG',
        "key": 'ticker',
        "action_id": "update_data"
    }, {
        "type": 'text',
        "label": 'interval',
        "value": '9-10',
        "key": 'ticker3',
        "action_id": "update_data"
    }, {
        "type": 'dropdown',
        "label": 'area',
        "options": [
            {"label": "1", "value": "1"},
            {"label": "2", "value": "2"},
            {"label": "3", "value": "3"},
            {"label": "4", "value": "4"},
            {"label": "5", "value": "5"},
            {"label": "6", "value": "6"},
            {"label": "7", "value": "7"},
            {"label": "8", "value": "8"},
            {"label": "9", "value": "9"},
            {"label": "10", "value": "10"},
            {"label": "11", "value": "11"},
            {"label": "12", "value": "12"},
            {"label": "13", "value": "13"},
            {"label": "14", "value": "14"},
            {"label": "15", "value": "15"},
            {"label": "16", "value": "16"},
            {"label": "17", "value": "17"},
            {"label": "18", "value": "18"},
            {"label": "19", "value": "19"},
            {"label": "20", "value": "20"},
            {"label": "21", "value": "21"},
            {"label": "22", "value": "22"},
            {"label": "23", "value": "23"},
            {"label": "24", "value": "24"},
        ],
        "value": 'GOOD',
        "key": 'ticker2',
        "action_id": "update_data"
    }
    ]

    tabs = ["Plot", "Table"]

    controls = [{
        "type": "button",
        "id": "update_data",
        "label": "update"
    }]

    outputs = [
        {
            "type": "plot",
            "id": "plot",
            "control_id": "update_data",
            "tab": "Plot"},
        {
            "type": "table",
            "id": "table_id",
            "control_id": "update_data",
            "tab": "Table",
            "on_page_load": True
        }
    ]

    def getData(self, params):
        ticker = params['ticker']
        ticker2 = params['ticker2']
        ticker3 = params['ticker3']
        if ticker == 'empty':
            ticker = params['custom_ticker'].upper()
        if ticker2 == 'empty':
            ticker2 = params['custom_ticker'].upper()
        if ticker3 == 'empty':
            ticker3 = params['custom_ticker'].upper()
        # ddd.yearandprovince(11, 2007)
        # ddd.allyearsanddroughts2(7)
        # print(ticker)
        # print(ticker2)
        # print(ticker3)
        arr = ticker3.split('-')

        df = pd.DataFrame(
            Vhithings.ddd.merged[(Vhithings.ddd.merged["area"] == int(ticker2)) & (Vhithings.ddd.merged["Week"] >=
                                                                                   int(arr[0])) & (
                                         Vhithings.ddd.merged["Week"] <= int(arr[1]))][['Year', 'Week', ticker]])
        return df

    def getPlot(self, params):
        df = self.getData(params)

        plt_obj = df.plot(x='Year', y=params['ticker'])
        plt_obj.set_ylabel(params['ticker'])
        plt_obj.set_xlabel("Year")
        plt_obj.set_title(params['ticker'])
        return plt_obj.get_figure()


app = Vhithings()
app.launch(port=9094)
