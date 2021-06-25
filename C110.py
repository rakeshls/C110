import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
df = pd.read_csv('data.csv')
df.head()
data = df['temp'].tolist()
#print(data)
poplution_mean = statistics.mean(data)
print(poplution_mean)
poplution_stDev = statistics.stdev(data)
print(poplution_stDev)
fig = ff.create_distplot([data],['temp'])
fig.show()