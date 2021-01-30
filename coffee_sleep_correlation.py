import numpy as np
import csv
import plotly.express as px

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = sorted(csv.DictReader(csv_file))
        fig = px.scatter(df , x = "Coffee in ml" , y = "sleep in hours")
        fig.show()

def getDataSource(data_path):
    coffee = []
    hoursOfSleep = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            hoursOfSleep .append(float(row["sleep in hours"]))
    return{"x":coffee , "y":hoursOfSleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"] , dataSource["y"])
    print(correlation[0,1])

def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure(data_path)

setup()
