import pandas as pd

df = pd.read_csv("mohammad.csv")

pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", 100)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.html.table_schema",True)

df.info()
print(df)