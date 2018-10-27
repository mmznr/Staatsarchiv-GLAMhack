#! /usr/bin/python3

from glob import glob
import fastText
import Clustering_functions as cf
import numpy as np
import re


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

docs = glob("../eStPZH_XML_Neu/*.xml")

vector_table = {}
    
model = fastText.load_model('stillstand5.bin')
    
doc_names = []
doc_vectors = []

for doc in docs:
    with open(doc) as inf:
        complete = []
        content = inf.read()
        texts = re.findall("<p>((.|\n)*?)<\/p>", content)
        cont = None
        for p in texts:
            p = p[0]
            if cont is not None:
                p = cont + p
                cont = None
            p = re.sub("<choice>", "", p)
            p = re.sub("<\/choice>", "", p)
            p = re.sub("<abbr>.*?<\/abbr>", "", p)
            p = re.sub("<expan>", "", p)
            p = re.sub("<\/expan>", "", p)
            p = re.sub("<unclear.*?>.*?<\/unclear>", "", p)
            p = re.sub("<.*?>", "", p)
            p = re.sub("\s\s", " ", p)
            p = re.sub("\.", "", p)
            p = re.sub(":", "", p)
            p = re.sub("\,", "", p)
            p = re.sub("\*", "", p)
            p = re.sub("\✳", "", p)
            p = re.sub("\(", "", p)
            p = re.sub("\)", "", p)
            p = re.sub("\[", "", p)
            p = re.sub("\]", "", p)
            m = re.search("\S+¬", p)
            if m:
                cont = m.group(0)[:-1]
                p = re.sub("\S+¬", "", p)
            complete.extend(p.split())
            
        word_vectors = []
        
        for token in complete:
            if is_number(token) or token[0].isupper():
                continue
            word_vectors.append(model.get_word_vector(token))
                
        #~ print(doc)
        
        if len(word_vectors) > 0:
            doc_vector = np.mean(np.array(word_vectors), axis=0)
            
            doc_names.append(doc)
            doc_vectors.append(doc_vector)
        
#cf.pca_plot(doc_vectors, doc_names, output_filename=None)
#cf.hierarchical_clusters_draw(doc_vectors,doc_names,max_d=0.15,
                               #~ output_filename=None, 
                               #~ figheight =100, figwidth=20)
cf.hierarchical_clusters_print(doc_vectors,doc_names,max_d=0.15)
        

        
        
