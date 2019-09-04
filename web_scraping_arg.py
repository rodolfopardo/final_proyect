#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:39:01 2019

@author: rodolfopardo
"""
#Importo librerias

print('Importando librerías...')

import pandas as pd 
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
#Se instala librerias que no vienen por defecto
#!pip install wordcloud, feedparser
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import feedparser
import time


#Funcion que convierte un diccionario a dataframe

def convierte(url,df):
    for i in url:
        #global df
        x = feedparser.parse(i)
        df = df.append(x.entries)
    return df

#Funcion que grafica un wordcloud 

def wordcloud(df):
    titulos = " ".join(review for review in df.title)
    stopwords = set(STOPWORDS)
    stopwords.update(["de", "la", "por", "el", "una", "con", "su", "que", "lo",
                  "un", "hay", "El", "ya", "en", "es", "los", "se", "del",
                  "las", "para", "ex", "ante", "va", "le"])
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(titulos)
    plt.figure(figsize = (8, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    


#RSS diarios 

rss_clarin = ['https://www.clarin.com/rss/lo-ultimo/', 
              'https://www.clarin.com/rss/politica/',
              'https://www.clarin.com/rss/mundo/', 
              'https://www.clarin.com/rss/sociedad/',
              'https://www.clarin.com/rss/policiales/', 
              'https://www.clarin.com/rss/economia/']


rss_lanacion = ['http://contenidos.lanacion.com.ar/herramientas/rss/origen=2',
                'http://contenidos.lanacion.com.ar/herramientas/rss/categoria_id=30',
                'http://contenidos.lanacion.com.ar/herramientas/rss/categoria_id=272',
                'http://contenidos.lanacion.com.ar/herramientas/rss/categoria_id=7773',
                'http://contenidos.lanacion.com.ar/herramientas/rss/categoria_id=7']

rss_pagina12 = ['https://www.pagina12.com.ar/rss/secciones/el-pais/notas',
                'https://www.pagina12.com.ar/rss/secciones/economia/notas',
                'https://www.pagina12.com.ar/rss/secciones/sociedad/notas',
                'https://www.pagina12.com.ar/rss/secciones/el-mundo/notas',
                'https://www.pagina12.com.ar/rss/portada']



#Genero dataframes vacíos que servirán como almacenamiento de datos
df = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()

print('Scraping on...')

#LLamo a funcion convierte

df = convierte(rss_clarin,df)
df2 = convierte(rss_lanacion,df2)
df3 = convierte(rss_pagina12,df3)
      
print('Dataframes generados')
#Tiempo para procesar información
time.sleep(2)
print("Generando wordclouds de los titulos")

#Llamo a funcion wordcloud

wordcloud(df)
wordcloud(df2)
wordcloud(df3)





