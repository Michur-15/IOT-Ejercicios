#Importación/Llamado de librerias
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

#Update file
#En la variable guardamos los datos del archivo cargado e indicamos que este se separa por punto y coma ';'
df = pd.read_csv("D:\\TRABAJOS\\10mo Semestre\\Eectiva 1- Internet de las Cosas\\Corte 1\\1.peso&altura.csv", sep=';')
#Solicitamos los primeros datos del archivo.
df.head()

#Estadisticas Generales
df.describe()

#Histograma
sn.histplot(df.Height, kde=True)
plt.show()

#Cleaning
mean = df.Height.mean()
std = df.Height.std()
lowerBound = mean - 3*std
upperBound = mean + 3*std


df.Height[df.Height < lowerBound]  # outlier
df.Height[df.Height > upperBound]  # outlier
df.Height[(df.Height < lowerBound) | (df.Height > upperBound)]# outlier

df_no_outlier = (df.Height > lowerBound) & (df.Height < upperBound)
df_no_outlier.head()
df_no_outlier.count

# z score
df["z-score"] = (df.Height-mean)/std
df.head()
sn.histplot(df["z-score"], kde=True)
plt.show()