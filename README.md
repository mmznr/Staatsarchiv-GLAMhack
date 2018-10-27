\#glamhack2018

# Sex and Crime und Kneipenschlägereien in der Frühen Neuzeit

## Goal
Make the data ("Stillstandsprotokolle des 17. Jahrhunderts") better searchable and georeference it for visualization.

## Team
* Ernst Rosser, ernst.rosser@gmail.com
* Barbara Leimgruber, Barbara.Leimgruber@ji.zh.ch
* Rebekka Plüss, Rebekka.Pluess@ji.zh.ch
* Ismail Prada, ismail.prada@gmail.com
* Matthias Mazenauer, matthias.mazenauer@statistik.ji.zh.ch
* Tobias Hodel, tobias.hodel@ji.zh.ch

## Data sources:
* Primary Data

  * [ZENODO](https://zenodo.org/record/1471130)


* Secondary data 

  * [Siedlungsverzeichnis des Kantons Zürich](http://www.web.statistik.zh.ch/cms_siedlungsverzeichnis/daten.php)


## Steps taken

** Create lookup for normalized strings (https://github.com/mmznr/Staatsarchiv-GLAMhack/blob/master/woerterStillstand_Result.tsv)
** Annotate named entities (normalization)
*** places (also add BfS-data)
*** persons (normalization to be used for auto-complete in search)
** Cluster words
*** to be used to refer to topic/concept
** Cluster documents
*** to be used as keyword(s) in TEI header
** Produce script to add information as tags (in header or body) to write in XML


## Lemmatization/Normalisation

* Done: Wordlist and Frequencies

* ToDo: Do POS

## Named Entities

* Names of persons: done A-D

* Names of places: done

## Visualization


### Word-Cluster

#### Visualization
(using fasttext)
https://github.com/mmznr/Staatsarchiv-GLAMhack/tree/master/Visualisierungen/clusters.png
https://github.com/mmznr/Staatsarchiv-GLAMhack/tree/master/Visualisierungen/clusters2.png

#### Frequency list of Word-Cluster
https://docs.google.com/spreadsheets/d/1rFo7p9YsQRwJufMuWGw2677acOsWevcmm-lN5RVBJv4/edit?usp=sharing

### GIS Visualization

https://beta.observablehq.com/@mmznrstat/sex-and-crime-und-kneipenschlagereien-in-der-fruhen-neuzei

* Done: Borders from swisstopo via Linked Data, Matching of the settlements of the canton of Zurich

* ToDo: Get List of old names of this settlements, match them and show all relating documents of a settlement (or municipality) 


