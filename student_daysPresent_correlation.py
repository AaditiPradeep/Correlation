import numpy as np
import csv
import plotly.express as px

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df , x = "Marks In Percentage" , y = "Days Present")
        fig.show()

def getDataSource(data_path):
    marks = []
    daysPresent = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    return{"x":marks , "y":daysPresent}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"] , dataSource["y"])
    print(correlation[0,1])

def setup():
    data_path = "Student Marks vs Days Present.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure(data_path)

setup()
    


