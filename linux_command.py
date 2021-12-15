import os 
for i in range(2,26):
    os.system("python3 clustering_with_distance_matrix.py --distances distance_df_100.csv --clusters {} --method agg".format(i))