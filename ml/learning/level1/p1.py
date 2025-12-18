import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
# from sklearn

dataset = pd.read_csv('Data.csv')
# print(dataset.isnull().sum())
x= dataset.iloc[:,:-1].values
y= dataset.iloc[:,-1:].values


#to take average values of a partcular column
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

#make first column as 10101 based on country , so it will form array based on
#no of categegorical
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
x = np.array(ct.fit_transform(x))

#to change to boolean value
le = LabelEncoder()
y = le.fit_transform(y)
# print(y)


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)
# print(y_train)

sc = StandardScaler()
x_train[:,3:] = sc.fit_transform(x_train[:,3:])
x_test[:,3:] = sc.fit_transform(x_test[:,3:])
print(x_train)

