import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Assign colum names to the dataset
names = ['Mean', 'Standard_Deviation', 'Entropy', 'RMS', 'Variance', 'Smoothness','Kurtosis','Skewness','IDM','ACTIVITY']

# Read dataset to pandas dataframe
dataset = pd.read_csv('FALL_DATA.csv', names=names)

dataset.head()

X = dataset.iloc[1:, :-1].values
y = dataset.iloc[1:, 9].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=4)
classifier.fit(X_train, y_train)

KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
                     metric_params=None, n_jobs=None, n_neighbors=4, p=2,
                     weights='uniform')

y_pred = classifier.predict(X_test)


from sklearn.metrics import accuracy_score
print("Accuracy-Test data:", accuracy_score(y_pred, y_test))
