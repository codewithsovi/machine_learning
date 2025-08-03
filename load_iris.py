import pandas as pd
from sklearn.datasets import load_iris

"""
kategori bunga :
0 → Setosa
1 → Versicolor
2 → Virginica
"""

iris = load_iris()

# menampilkan keys (dictionary)
for key in iris.keys():
    print(f"{key}: {type(iris[key])}")


# menampilkan DESC (deskripsi) 
print(iris['DESCR'])

# membuat frame data
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

print(df)