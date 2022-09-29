# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.size'] = 18
sns.set_context('talk', font_scale=1.2);
# %matplotlib inline

df = pd.read_csv('day_wise.csv')



df.shape



display(df.dtypes)



df.head()

df.tail()



df = df.rename(columns={"Date" : "Data","Confirmed":"Confirmados","Deaths":"Mortes","Recovered":"Recuperados","Active":"Ativos",
                        "New cases":"Novos casos","New deaths":"Novas mortes","New recovered":"Novos recuperados","No. of countries":"Qtd países",
                        "Deaths / 100 Cases":"Mortes a cada 100 casos","Recovered / 100 Cases":"Recuperados a cada 100 casos","Deaths / 100 Recovered":"Mortes a cada 100 recuperados"})
df.head()



df.head()

df.tail()



(df.isnull().sum() / df.shape[0]).sort_values(ascending=False)



df[['Confirmados', 'Mortes', 'Recuperados', 'Ativos',
    'Novos casos', 'Novas mortes' , 'Novos recuperados','Mortes a cada 100 casos','Recuperados a cada 100 casos','Mortes a cada 100 recuperados','Qtd países']].describe()


df.hist(bins=20, figsize=(30,30));


df.tail(1)



df = df.rename(columns={"Mortes a cada 100 recuperados":"100 Mortes a cada recuperado"})
df.head(5)


plt.figure(figsize=(10,5))
corr = df[['Data', 'Confirmados', 'Mortes', 'Recuperados', 'Ativos', 'Novos casos','Novas mortes','Novos recuperados','Mortes a cada 100 casos','Recuperados a cada 100 casos','100 Mortes a cada recuperado','Qtd países']].corr()

display(corr)

"

plt.figure(figsize=(15,10))
sns.heatmap(corr, cmap='RdBu', fmt='.3f', square=True, linecolor='white', annot=True);



df.head(188)



df[['Confirmados', 'Mortes', 'Recuperados', 'Ativos',
    'Novos casos', 'Novas mortes' , 'Novos recuperados','Mortes a cada 100 casos','Recuperados a cada 100 casos','100 Mortes a cada recuperado','Qtd países']].describe()

