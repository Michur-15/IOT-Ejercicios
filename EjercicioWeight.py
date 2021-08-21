#Importación/Llamado de librerias
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

#Update file
#En la variable guardamos los datos del archivo cargado e indicamos que este se separa por punto y coma ';'
df = pd.read_csv("D:\\TRABAJOS\\10mo Semestre\\Eectiva 1- Internet de las Cosas\\Corte 1\\1.peso&altura.csv",sep=';')
#Solicitamos los primeros datos del archivo.
df.head()

#General statics
df.describe()

#Plot histogram, Se indica de que columna se tomaran los datos.
sn.histplot(df.Weight, kde=True)
plt.show()

#Cleaning
mean = df.Weight.mean()
std = df.Weight.std()
#Creamos los limites inferior y superior
lowerBound = mean - 3*std
upperBound = mean + 3*std


df.Weight[df.Weight < lowerBound]  # outlier
df.Weight[df.Weight > upperBound]  # outlier
df.Weight[(df.Weight < lowerBound) | (df.Weight > upperBound)]# outlier

df_no_outlier = (df.Weight > lowerBound) & (df.Weight < upperBound)
df_no_outlier.head()
df_no_outlier.count

#z score
df["z-score"] = (df.Weight-mean)/std
df.head()
sn.histplot(df["z-score"], kde=True)
plt.show()