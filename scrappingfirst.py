#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:39:25 2019

@author: rodolfopardo
"""

#Se importan las librerias

import sys
#!{sys.executable} -m pip install bs4 requests pandas lxml html5lib
import pandas as pd
import requests
from bs4 import BeautifulSoup

#URL_TO_DATA pide un requests a la url e identifica el scraping

def url_to_data(*args):
    diario = requests.get(url_peticion).content
    soup = BeautifulSoup(diario, 'html')
    titulos = soup.select('h1')
    return titulos

#Limpia los titulos y luego comienza a buscar según la busqueda ingresada por el usuario 

#df_news = pd.DataFrame()

def titulos_to_results(*args):
    noticias = [element.text for element in tit]
    df_news = pd.DataFrame(noticias)
    columnas = ["titulos"]
    df_news.columns = columnas
    #news = df_news[(df_news['titulos'].str.contains(buscador))]
    
    return df_news

#Pido al usuario la url
url_peticion = int(input("Ingrese 1 para scrapping El Sol, 2 si quiere scrapping Clarin y 3 si quiere scrapping MDZ: "))

#Condicion para elegir el diario
if url_peticion == 1:
    url_peticion = "https://elsol.com.ar"
elif url_peticion == 2:
    url_peticion = 'https://clarin.com'
else:
    url_peticion = "https://mdzol.com"
    
#Guardo el return para utilizarlo en la proxima funcion
tit = url_to_data(url_peticion)
#Que ingrese la busqueda
#buscador = input("Ingrese la palabra que desea buscar en los titulos: ")    
url_to_data(url_peticion)
titulos_to_results(tit)