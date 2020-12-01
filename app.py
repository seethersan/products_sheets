import gspread
import pandas as pd

gc = gspread.service_account(filename='productssheets.json')

sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1vM0B6BY7ZfyGX-C0Xmn7Y1Pesg5X5LFVEDDZsUaqAVM/edit#gid=1396266021')

worksheet_list = sheet.worksheets()


for worksheet in worksheet_list:
    dataframe = pd.DataFrame(worksheet.get_all_records())
    dataframe['PRICE (PEN)'] = dataframe['PRICE (USD)'] * 3.73
    dataframe['IGV'] = (dataframe['PRICE (PEN)'] * 0.18).round(2)
    dataframe['VALUE'] = ((dataframe['PRICE (PEN)'] + dataframe['IGV']) * dataframe['STOCK']).round(2)
    dataframe.to_csv(worksheet.title.replace(" ","_").lower() + '.csv')
