
from pandas.io.parsers import read_csv
from sklearn.metrics import silhouette_samples,silhouette_score 
from sklearn.cluster import KMeans 
import pandas as pd 
import numpy as np 
def get_custom_distances(filename):
  dataframe = pd.read_csv(filename)
  return dataframe.to_numpy()
filename = "device_ids_100_clusters_agglomerative.csv"
df = pd.read_csv(filename)
distance_matrix = get_custom_distances(filename)
for column_name in df.columns[2:]:
    silhouette_avg = silhouette_score(distance_matrix,df[column_name])
    number_of_clusters = column_name.split("_")[1]
    print("Silhoutte score with n clusters =  {} is {}".format(number_of_clusters,silhouette_avg))
print(df.columns[2:])