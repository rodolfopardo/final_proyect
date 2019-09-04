# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 09:45:29 2019

@author: alex_
"""

import feedparser

url = "https://www.reforma.com/rss/negocios.xml"

data = feedparser.parse(url)
data