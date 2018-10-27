#! /usr/bin/python3

import csv
import Clustering_functions as cf
import numpy as np



vector_array = []
pot_target_words = []

with open("freq.tsv") as freq:
    reader = csv.reader(freq, delimiter="\t")
    for row in reader:
        if len(row) > 1 and row[3] != "":
            pot_target_words.append(row[2])


limit = 5000
i = 0

vec_dict = {}

for line in open("stillstand5.vec"):
    #~ if i == limit:
        #~ break
    line = line.split()
    if len(line) < 3:
        continue
    vec_dict[line[0]] = line[1:]
    i += 1
    
target_words = []
    
for t in pot_target_words:
    if t in vec_dict.keys():
        target_words.append(t)
        vector_array.append(vec_dict[t])
    
    
vector_array = np.array(vector_array)
    
cf.hierarchical_clusters_print(vector_array,target_words,max_d=0.25)
#cf.pca_plot(vector_array, target_words, output_filename=None)
cf.hierarchical_clusters_draw(vector_array,target_words,max_d=0.25,
                               output_filename=None, 
                               figheight =100, figwidth=20)
#cf.kmeans_clusters_print(vector_array, target_words,  
                          #~ num_clusters = 50)
