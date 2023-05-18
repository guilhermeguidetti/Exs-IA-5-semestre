import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics

df = pd.read_csv('ex4/dnd/dnd_ability_score_data.csv')

# Selecionar as colunas numéricas relevantes para clusterização
data = df[['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']]

k_values = range(2, 10)
sse = []
for k in k_values:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    sse.append(kmeans.inertia_)

plt.plot(k_values, sse, 'bx-')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Soma dos erros quadrados dentro do cluster (SSE)')
plt.title('Método Elbow')
plt.show()