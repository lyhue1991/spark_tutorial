import networkx as nx
import pandas as pd 
import sys
import matplotlib.pyplot as plt

def plot(directed = True):
    dfedges = pd.read_csv('data/dfedges.csv',sep = '\t')
    if directed:
        graph = nx.DiGraph(dfedges[['srcId','dstId']].values.tolist())
    else:
        graph = nx.Graph(dfedges[['srcId','dstId']].values.tolist())
    nx.draw_networkx(graph)
    plt.show()

if __name__ == "__main__":
    if sys.argv[1]=="true": 
        plot(directed = True)
    else:
        plot(directed = False)