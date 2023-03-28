import pandas as pd


excel_file = '/home/arjun/practice/python/algo/data_science/pandas/movies.xls'
movies = pd.read_excel(excel_file)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(movies.head())


