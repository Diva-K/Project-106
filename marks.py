import csv
import plotly_express as px
import numpy as np

def getDataSource(data_path):

    marks=[]
    present=[]
    with open(data_path) as f:
       df=csv.DictReader(f)
       for row in df:
           marks.append(float(row["Marks In Percentage"]))
           present.append(float(row["Days Present"]))
    return {"x": marks, "y":present}

def findCorellation(data_source):
    corellation=np.corrcoef(data_source["x"],data_source["y"])
    print("correllation is ",corellation[0,1])

def setup ():
    data_path="marks.csv"
    data_source=getDataSource(data_path)
    findCorellation(data_source)

setup()
       
    