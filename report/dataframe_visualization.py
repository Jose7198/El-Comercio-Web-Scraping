# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:33:28 2020

@author: jose7
"""

import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

path = 'D:\\Documents\\GitHub\\py-murillo-lopez-jose-luis\\proyecto-2b\\scrapy\\arania_noticias\\tmp\\comercio-news.csv'

df = pd.read_csv(path)

df.dtypes

df.Category.fillna('Sin categoría', inplace=True)

df.Date.fillna('Sin fecha', inplace=True)

df.Editor.fillna('Sin editor', inplace=True)

df.Hour.fillna('00:00', inplace=True)

df.Tag.fillna('Sin tag', inplace=True)

df.Title.fillna('Sin título', inplace=True)

df.loc[7545, 'Hour'] = '00:45'

df.to_pickle('D:\\Documents\\GitHub\\py-murillo-lopez-jose-luis\\proyecto-2b\\report\\news.pkl')

#Primer gráfico

df_per_year = df.groupby(df.Date.str[-4:])['Title'].count()

df_per_year = df_per_year.reset_index()

df_per_year = df_per_year[df_per_year['Date'].str.isdigit()]

#Segundo gráfico

df_per_month_2019 = df.Date.str.split(' ').apply(lambda x: ' '.join(x[-3:]))

df_per_month_2019 = df_per_month_2019.reset_index()

df_per_month_2019 = df_per_month_2019[df_per_month_2019['Date'].str[-4:] == '2019']

df_per_month_2019 = df_per_month_2019.Date.str.split(' ').apply(lambda x: x[0])

df_per_month_2019 = df_per_month_2019.reset_index()

df_per_month_2019 = df_per_month_2019.groupby(df_per_month_2019.Date)['index'].count()

df_per_month_2019 = df_per_month_2019.reset_index()

df_per_month_2019 = df_per_month_2019[df_per_month_2019.Date != 'de']

df_per_month_2019 = df_per_month_2019.set_index('Date')

#Tercer gráfico

df_per_hour = df.groupby(df.Hour)['Title'].count()

df_per_hour = df_per_hour.reset_index().sort_values('Title', ascending=False).head(10)

#Cuarto gráfico

df_per_editors = df.groupby(df.Editor)['Title'].count()

df_per_editors = df_per_editors.reset_index().sort_values('Title', ascending=False).head(11)

#Quinto gráfico

df_per_categories = df.groupby(df.Category)['Title'].count()

#Sexto gráfico

df_per_tag = df.groupby(df.Tag)['Title'].count()

df_per_tag = df_per_tag.reset_index()

#Séptimo gráfico

df_tag_per_category = df.groupby(['Category','Tag'])['Title'].count()

df_tag_per_category = df_tag_per_category.reset_index().sort_values('Title', ascending=False)

#Décimo gráfico

df_views_per_year = df.groupby(df.Date.str[-4:])['Views'].sum()

df_views_per_year = df_views_per_year.reset_index()

df_views_per_year = df_views_per_year[df_views_per_year['Date'].str.isdigit()]

df_per_year['Views'] = df_views_per_year['Views'] / 1000

##Undécimo gráfico

df_views_per_category = df.groupby(df.Category)['Views'].sum()

df_views_per_category = df_views_per_category.reset_index()

#Duodécimo gráfico

df_views_per_category['Articles'] = df_per_categories.reset_index()['Title']

df_views_per_category['Views'] = df_views_per_category['Views'].apply(lambda x: x/1000)

#Decimotercer gráfico

df_top_views = df.sort_values('Views').tail(20)

#Decimocuarto gráfico

df_reactions_per_year = df.groupby(df.Date.str[-4:])['Total_Reactions'].sum()

df_reactions_per_year = df_reactions_per_year.reset_index()

df_reactions_per_year = df_reactions_per_year[df_reactions_per_year['Date'].str.isdigit()]

df_per_year['Reactions'] = df_reactions_per_year['Total_Reactions']

#Decimosexto gráfico

df_ratio = df.groupby(df.Date.str[-4:])['Views_Reacts_Ratio'].mean()

df_ratio = df_ratio.reset_index()

df_ratio = df_ratio[df_ratio['Date'].str.isdigit()]

#Decimosexto gráfico

df_all_reactions = df.sum(numeric_only=True)

df_all_reactions = df_all_reactions[['Contento', 'Indiferente', 'Indignado','Sorprendido','Triste']]

#Decimoséptimo gráfico

df_top_reactions = df.sort_values('Total_Reactions').tail(21)

df_top_reactions = df_top_reactions[df_top_reactions['Title'] != "Tatiana Ordeñana: 'El fallo de Satya reconoce que hay más tipos de familia'"]

df_top_reactions = df_top_reactions[['Title','Contento', 'Indiferente', 'Indignado','Sorprendido','Triste']]

#Decimooctavo gráfico

df_top_contento = df.sort_values('Contento').tail(20)

df_top_contento = df_top_contento[['Title','Contento']]
