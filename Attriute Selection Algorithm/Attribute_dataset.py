import pandas as pd

data={
    "Weather":["Sunny","Sunny","Windy","Rainy","Rainy","Rainy","Windy","Windy","Windy","Sunny"],
    "Parents":["Yes","No","Yes","Yes","No","Yes","No","No","Yes","No"],
    "Financial condition":["Rich","Rich","Rich","Poor","Rich","Poor","Poor","Rich","Rich","Rich",],
    "Decision":["Cinema","Play Tennis","Cinema","Cinema","Stay in","Cinema","Cinema","Shopping","Cinema","Play Tennis"]
}
df=pd.DataFrame(data) #creates a dataframe, table like structure
df.to_csv("Dataset.csv",index=False) #if index is false, pandas won't create the row numbers for the data set
print("CSV file has been created!")