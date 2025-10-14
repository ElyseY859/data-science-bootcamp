import numpy as np
import pandas as pd

#Numpy Questions
#1
A = np.array([1,2,3,4,5])
B = np.array([4,5,6,7,8])

vertical_stack = np.vstack((A,B))
print("Vertical Stack:\n", vertical_stack)

horizontal_stack = np.hstack((A, B))
print("Horizontal Stack:\n", horizontal_stack)
#2
common_elements = np.intersect1d(A, B)
print("Common elements:", common_elements)
#3
numbers_in_range = A[(A >= 5) & (A <= 10)]
print("Numbers in range 5-10:", numbers_in_range)
#4
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

filtered_rows = iris_2d[(iris_2d[:,2] > 1.5) & (iris_2d[:,0] < 5.0)]
print("Filtered rows:\n", filtered_rows)

#Pandas Questions
#1
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
filtered_rows = df.loc[::20, ['Manufacturer', 'Model', 'Type']]
print(filtered_rows) 
#2
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)

print(df[['Min.Price', 'Max.Price']].isnull().sum())
#3
df2 = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
rows_sum_gt_100 = df2[df2.sum(axis=1) > 100]
print(rows_sum_gt_100)