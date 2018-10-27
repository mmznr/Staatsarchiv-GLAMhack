from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

"""
Originally done by Tatiana Ruzsics.
Slightly modified by Ismail Prada

Just some basic clustering functions.
"""


def hierarchical_clusters_draw(feature_matrix,target_words,max_d=0.5,
                               output_filename=None, 
                               figheight =50, figwidth=20):
    
    Z_spat = linkage(feature_matrix, 'average','cosine')
    # You can try out with different linkage function here:
    # 'single','complete','average'

    fig, ax = plt.subplots(nrows=1, ncols=1)
    fig.set_figheight(100)
    fig.set_figwidth(40)
    plt.title('Hierarchical Clustering Dendrogram', fontsize=10)
    plt.ylabel('Target words', fontsize=9)
    plt.xlabel('Distance', fontsize=9)
    dendrogram(
        Z_spat,
        leaf_font_size=8.,
        labels=target_words,
        orientation='right'
    )

    plt.axvline(x = max_d, color='k', linestyle='--') 
    # This drows a vertical number, 
    # choose the value where you think clusters should be cut
    
    if output_filename:
        plt.savefig(output_filename, bbox_inches='tight') 
        #bbox_inches='tight' - to make margins minimal
    else:
        plt.show()


def hierarchical_clusters_print(feature_matrix,target_words,max_d=0.5):

    Z_spat = linkage(feature_matrix, 'average','cosine')
    # You can play around with different linkage function here: 
    # 'single','complete','average'
    
    clusters = fcluster(Z_spat, max_d, criterion='distance')
    num_clusters = len(set(clusters))
    
    # Printing clusters
    for ind in range(1, num_clusters+1):
        for i,w in enumerate(target_words):
            if clusters[i] == ind:
                print('{}\t{}'.format(ind, w))
        print()#add whitespace


def kmeans_clusters_print(feature_matrix, target_words,  
                          num_clusters = 5):
                              
    #Fitting clusters
    km = KMeans(init='k-means++', n_clusters=num_clusters, n_init=10)
    
    kmeans =  km.fit(feature_matrix)

    cluster_labels = kmeans.labels_ 
    # the array of cluster labels 
    # to which each input vector in n_samples belongs

    cluster_to_words = defaultdict(list) 
    # which word belongs to which cluster
    for c, i in enumerate(cluster_labels):
            cluster_to_words[i].append( target_words[c] )
    
    # Printing clusters
    for i in range(num_clusters):
        for i,w in enumerate(target_words):
            if clusters[i] == ind:
                print('{}\t{}'.format(ind, w))
        print()#add whitespace

def pca_plot(feature_matrix, target_words, output_filename=None, title = "PCA decomposition"):

    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(feature_matrix)
    x = []
    y = []
    for value in pca_result:
        x.append(value[0])
        y.append(value[1])

    plt.figure(figsize=(16, 16))
    for i in range(len(x)):
        plt.scatter(x[i],y[i])
        plt.annotate(target_words[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.title('PCA decomposition', fontsize=20)

    if output_filename:
        plt.savefig(output_filename)
    else:
        plt.show()
                 
    print('PCA done!')
    
