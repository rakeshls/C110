import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
df = pd.read_csv('data.csv')
df.head()
data = df['temp'].tolist()
dataset = []
for i in range(0,1000):
    index = random.randint(0,len(data))
    value = data[index]
    dataset.append(value)
#print(dataset)
#print('standrad deviation is',stDev)
def randomSetOfMean(cnt):
    dataset = []
    print(len(data))
    for i in range(0,cnt):
        index1 = random.randint(0,len(data))
        value = data[index1]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
def showFigure(mList):
    mean = statistics.mean(mList)
    print('mean is',mean)
    fig =ff.create_distplot([mList],['temp'],show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode='lines'))
    fig.show()
def stdev1():
    list = []
    for i in range(0,1000):
        index = randomSetOfMean(100)
        list.append(index)
    stDev = statistics.stdev(list)
    print(stDev)
def setup():
    dataset = []
    for i in range(0,1000):
        index = randomSetOfMean(100)
        dataset.append(index)
    showFigure(dataset)
setup()
stdev1()


