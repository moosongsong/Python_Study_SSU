import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fig = plt.figure()

df = pd.read_csv('pima-indians-diabetes.csv',
                 names=['pregnant', 'plasma', 'pressure', 'thickness', 'insulin', 'BMI', 'pedigree', 'age', 'class'])
print(df)

a = df.groupby('pregnant').mean()
print(a)

sns.heatmap(df.corr(), annot=True, linecolor='white')
fig.show()

facet = sns.FacetGrid(df,col='class')
facet.map(plt.hist, 'plasma', bins=10)
plt.show()


from tensorflow.keras.models import Sequential
#인공 신경방을 그리기위한 도화지
from tensorflow.keras.layers import Dense
#동그라미