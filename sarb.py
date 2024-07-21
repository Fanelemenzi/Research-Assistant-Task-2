import pandas as pd


sarb_dataset = pd.read_csv('F:\Coding Projects\SARB Dataset\SARB_BankingData.csv')

selected_columns = ['KBP1120M', 'KBP1078M', 'KBP1514M', 'KBP1081M', 'KBP1080M']
selected_dataset = sarb_dataset[selected_columns]
