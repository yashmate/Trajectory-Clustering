# -*- coding: utf-8 -*-
"""Clustering with Distance Matrix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fDTo0V6osxq3gBmrrSmqZKrnlVoEJmWy
"""

import numpy as np 
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn_extra.cluster import KMedoids
from sklearn.cluster import OPTICS
import argparse 
import pandas as pd

def get_default_distances(N=20):
  matrix = np.random.random_integers(0,100,size=(N,N)) # 0-100 defines the range of values
  distance_matrix = (matrix + matrix.T)/2
  return distance_matrix

def get_clusters(distance_matrix,number_of_clusters,method="agg"):
  if method == "agg":
    model = AgglomerativeClustering(affinity='precomputed', n_clusters=number_of_clusters, linkage='complete').fit(distance_matrix)
    return model.labels_
  elif method == "dbscan":
    model =DBSCAN(metric="precomputed")
    return model.fit_predict(distance_matrix)
  elif method == "kmediods":
    model = KMedoids(n_clusters=number_of_clusters,metric="precomputed",init="k-medoids++",random_state=0).fit(distance_matrix)
    return model.labels_
  elif method == "optics":
    model = OPTICS(metric="precomputed")
    return model.fit_predict(distance_matrix)
    
  


def get_custom_distances(filename):
  dataframe = pd.read_csv(filename)
  return dataframe.to_numpy()

def main():
  parser = argparse.ArgumentParser(description='Agglomerative Clustering of a distance matrix')
  parser.add_argument("--distances",type=str,help="File Path for the distance matrix csv")
  parser.add_argument("--clusters",type=int,help="Number of clusters",default=1)
  parser.add_argument("--method",type=str,help="Clustering Algorithm",default="agg")
  parser.add_argument("--device_ids",type=str,help="File path for device ids",default="device_ids_100.csv")
  args = parser.parse_args()
  print(args.distances,args.clusters)
  if args.distances:
    distance_matrix = get_custom_distances(args.distances)
  else:
    distance_matrix = get_default_distances()
  print(distance_matrix)
  print(distance_matrix.shape)
  clusters = get_clusters(distance_matrix,args.clusters,args.method)
  print(clusters)
  device_df = pd.read_csv(args.device_ids)
  device_df['Cluster'] = clusters
  device_df.to_csv(args.device_ids)
  

main()

