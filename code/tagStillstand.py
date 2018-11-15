#!/usr/bin/python
# -*- coding: utf-8 -*-
#Rebekka Plüss 04-277-331

from glob import glob
import xml.etree.ElementTree as ET

class TagTEIXML(object):

    """
    Diese Klasse taggt in den Stillstandsprotokollen des 17. Jahrhunderts (Staatsarchiv des Kantonszürich):
    Normalisierte Wörter zur Suche gemäss einer mitgegebenen Liste 'normlist.tsv'
    Normalisierte Ortsnamen gemäss einer mitgegebenen Liste 'geolist.tsv'
    Normalisierte Personennamen gemäss einer mitgegebenen Liste 'perslist.tsv'
    mehr Infos im README
    """
    
    #diese Methode taggt ein XML-file 
    def tagXML(self,root,xmlfile,filename,geoList,persList,normList,worddesBeforeList,worddesAfterList):
    	#erstelle neues XML-File mit dem selben Namen im Ordner result
    	newfile = open("result/" + filename,"w")
    	
    	#schreibe alles bis <body> ins XML-File (Bereich, welcher nicht getaggt werden soll)
    	xmlfilesplittedhead = xmlfile.split('<body>')
    	newfile.write(xmlfilesplittedhead[0])
    	newfile.write('<body>') 
    	
    	#für jeden Paragraph in body/text gehe mitgegebenen Listen durch und tagge
    	for para in root.iter('p'):
    		if para.text == None:
    			xmlText = ""
    		else:
    			xmlText = para.text
    		
    		#Sonderzeichen in XML als Text
    		xmlText2 = xmlText
    		xmlText = xmlText2.replace('<','&lt;')
    		xmlText2 = xmlText
    		xmlText = xmlText2.replace('>','&gt;')
    		xmlText2 = xmlText
    		#tagge Personen
    		for persEntry in persList:
    			if persEntry[1] != "" and persEntry[2] != "":
    				for worddesB in worddesBeforeList:
    					for worddesA in worddesAfterList:
    						xmlText = xmlText2.replace(worddesB + persEntry[0] + worddesA,worddesB + "<persName key=\""+ persEntry[2]+ "\" ref=\""+ persEntry[1]+ "\">" + persEntry[0] + "</persName>"+ worddesA)
    						xmlText2 = xmlText
    			elif persEntry[1] != "":
    				for worddesB in worddesBeforeList:
    					for worddesA in worddesAfterList:
    						xmlText = xmlText2.replace(worddesB + persEntry[0]+worddesA,worddesB+"<persName ref=\""+ persEntry[1]+ "\">" + persEntry[0] + "</persName>"+ worddesA)
    						xmlText2 = xmlText
    			else:
    				for worddesB in worddesBeforeList:
    					for worddesA in worddesAfterList:
    						xmlText = xmlText2.replace(worddesB + persEntry[0]+worddesA,worddesB+"<persName key=\""+ persEntry[2]+ "\">" + persEntry[0] + "</persName>"+worddesA)
    						xmlText2 = xmlText
    						
    		#tagge Ortsnamen
    		for geoEntry in geoList:
    			if geoEntry[1] != "" and geoEntry[2] != "":
    				for worddesB in worddesBeforeList:
    					for worddesA in worddesAfterList:
    						xmlText = xmlText2.replace(worddesB + geoEntry[0] + worddesA,worddesB + "<placeName key=\""+ geoEntry[2]+ "\" ref=\""+ geoEntry[1]+ "\">" + geoEntry[0] + "</placeName>"+ worddesA)
    						xmlText2 = xmlText
    			elif geoEntry[1] != "":
    				for worddesB in worddesBeforeList:
    					for worddesA in worddesAfterList:
    						xmlText = xmlText2.replace(worddesB + geoEntry[0]+worddesA,worddesB+"<placeName ref=\""+ geoEntry[1]+ "\">" + geoEntry[0] + "</placeName>"+ worddesA)
    						xmlText2 = xmlText
    			else:
    				for worddesB in worddesBeforeList:
    					for worddesA in worddesAfterList:
    						xmlText = xmlText2.replace(worddesB + geoEntry[0]+worddesA,worddesB+"<placeName key=\""+ geoEntry[2]+ "\">" + geoEntry[0] + "</placeName>"+worddesA)
    						xmlText2 = xmlText
    		
    		#tagge Wörter mit Normalisierungen
    		for normEntry in normList:
    			for worddesB in worddesBeforeList:
    				for worddesA in worddesAfterList:
    					xmlText = xmlText2.replace(worddesB + normEntry[0]+worddesA,worddesB+"<w lemma=\""+ normEntry[1]+ "\">" + normEntry[0] + "</w>"+worddesA)
    					xmlText2 = xmlText
    		newfile.write('<p>' + xmlText + '</p>')
    	
    	#Schluss
    	newfile.write('</body></text></TEI>')
    	newfile.close()

#START 	
if __name__ == '__main__':

    #Lese Dateien fürs Tagging ein
    n = TagTEIXML()
    geo = open('tagLists/geolist.tsv','r')
    norm = open('tagLists/normlist.tsv','r')
    pers = open('tagLists/perslist.tsv','r')
    geolist = geo.readlines()
    normlist = norm.readlines()
    perslist = pers.readlines()
    
    #Definiere Liste
    geoL = [] #orig, nummer, normalisiert, 'placeName'
    persL = [] #orig, nummer, normalisiert, 'persName'
    normL = [] #orig, norm
    
    worddesAList = [" ", ".", ";","?","!","\t","\n"] #mögliche Wortgrenzen nach einem Wort
    worddesBList = [" ","\n","\t"] #mögliche Wortgrenzen vor einem Wort
    
    #Erstelle Listen
    for nline in normlist:
    	nline = nline.replace('\n','')
    	nlinelist = nline.split('\t')
    	if len(nlinelist) == 2:
    		normL.append(nlinelist)
    for gline in geolist:
    	glinelist = gline.split('\t')
    	if len(glinelist) >= 4:
    		geoL.append(glinelist)
    for pline in perslist:
    	plinelist = pline.split('\t')
    	if len(plinelist) >= 4:
    		persL.append(plinelist)
    		
    #Loop durch Stillstandsprotokolle in xml:
    infiles = glob("origXml/*.xml")
    for inf in infiles:
    	xmlf = open(inf,'r')
    	xmlfile = xmlf.read() 
    	file = ET.parse(inf)
    	root = file.getroot()
    	xmlname = inf.replace('origXml/','')
    	#tag, tag, tag... 	
    	n.tagXML(root,xmlfile,xmlname,geoL,persL,normL,worddesBList,worddesAList)
    	
    norm.close()
    geo.close()
    pers.close()



