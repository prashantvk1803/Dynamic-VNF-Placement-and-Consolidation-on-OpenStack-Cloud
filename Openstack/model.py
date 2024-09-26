
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("data1.csv")


data= data.drop('bandwidth', axis=1)

cpu_threshold = 30.0
memory_threshold = 2.0

data['cpu'] = data['cpu'].astype(float)
data['memory'] = data['memory'].astype(float)

def compute_utilization(row):
    if row['cpu'] < cpu_threshold or row['memory'] < memory_threshold:
        return 0
    else:
        return 1

# Apply the function to create a new column 'status'
data['status(1-over,0-under)'] = data.apply(compute_utilization, axis=1)



def sigmoid(z):
    return 1 / (1 + np.exp(-z))

data= pd.get_dummies(data)


X = data.drop(columns=["status(1-over,0-under)","time","cpu"])

y=data["status(1-over,0-under)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


n_features = X.shape[1]
parameters = np.zeros(n_features + 1)

epochs = 3000
learning_rate = 0.0008

for epoch in range(epochs):
    z = np.dot(X_train, parameters[1:]) + parameters[0]
    y_pred = sigmoid(z)

    gradients = np.zeros(n_features + 1)

    gradients[0] = (1 / len(y_train)) * np.sum(y_pred - y_train)

    for i in range(1, n_features + 1):
        gradients[i] = (1 / len(y_train)) * np.sum((y_pred - y_train) * X_train[:, i - 1])

    parameters -= learning_rate * gradients



intercept = parameters[0]
coefficients = parameters[1:]



test_linear_combination = np.dot(X_test, parameters[1:]) + parameters[0]
y_test_pred = sigmoid(test_linear_combination)

def calculate_training_loss(y, y_pred):
    loss = -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
    return loss

def calculate_testing_loss(y, y_pred):
    loss = -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
    return loss





predictions = [1 if p >= 0.5 else 0 for p in y_test_pred]

#for p, prediction in zip(y_test_pred, predictions):
   # print(f'p: {p}, Prediction: {prediction}')



p1 = np.mean(y_test_pred)
print("Average of p values (p1):", p1)








data2 = pd.read_csv("data2.csv")


data2 = data2.drop('bandwidth', axis=1)

cpu_threshold = 30.0
memory_threshold = 2.0

data2['cpu'] = data2['cpu'].astype(float)
data2['memory'] = data2['memory'].astype(float)

def compute_utilization(row):
    if row['cpu'] < cpu_threshold or row['memory'] < memory_threshold:
        return 0
    else:
        return 1

# Apply the function to create a new column 'status'
data2['status(1-over,0-under)'] = data2.apply(compute_utilization, axis=1)



def sigmoid(z):
    return 1 / (1 + np.exp(-z))

data2 = pd.get_dummies(data2)


X = data2.drop(columns=["status(1-over,0-under)","time","cpu"])

y=data2["status(1-over,0-under)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


n_features = X.shape[1]
parameters = np.zeros(n_features + 1)

epochs = 3000
learning_rate = 0.0008

for epoch in range(epochs):
    z = np.dot(X_train, parameters[1:]) + parameters[0]
    y_pred = sigmoid(z)

    gradients = np.zeros(n_features + 1)

    gradients[0] = (1 / len(y_train)) * np.sum(y_pred - y_train)

    for i in range(1, n_features + 1):
        gradients[i] = (1 / len(y_train)) * np.sum((y_pred - y_train) * X_train[:, i - 1])

    parameters -= learning_rate * gradients



intercept = parameters[0]
coefficients = parameters[1:]



test_linear_combination = np.dot(X_test, parameters[1:]) + parameters[0]
y_test_pred = sigmoid(test_linear_combination)

def calculate_training_loss(y, y_pred):
    loss = -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
    return loss

def calculate_testing_loss(y, y_pred):
    loss = -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
    return loss





predictions = [1 if p >= 0.5 else 0 for p in y_test_pred]

#for p, prediction in zip(y_test_pred, predictions):
   # print(f'p: {p}, Prediction: {prediction}')



p2 = np.mean(y_test_pred)
print("Average of p values (p2):", p2)

if p1 < p2:
    with open('node.txt', 'w') as file:
        file.write('compute01')
elif p1 > p2:
    with open('node.txt', 'w') as file:
        file.write('compute03')
