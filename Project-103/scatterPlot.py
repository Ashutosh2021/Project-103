import pandas as pd
import plotly.express as px

df = pd.read_csv("Copy+of+data+-+data.csv")

fig = px.scatter(data_frame= df, x= "date", y ="cases", color= "country",title= "Covid Cases in different countries on different days")
fig.show()