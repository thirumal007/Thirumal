import pandas as pd
data = pd.read_csv("E:\python program\python_book_program\ML_program\stock_data.csv")
d=data.head()
##print(d)
import warnings
warnings.filterwarnings("ignore")

##print("trainging days =",data.shape)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.figure(figsize=(10, 4))
plt.title("Stock Price")
plt.xlabel("Days")
plt.ylabel("Close Price USD ($)")
plt.plot(data["Close Price"])
plt.show()
####
data = data[["Close Price"]]
##print(data.head())

futureDays = 25

futureDays = 25
## create a new target column shifted 'X' units/days up
data["Prediction"] = data[["Close Price"]].shift(-futureDays)
##print(data.head())
##print(data.tail())
####
import numpy as np
x = np.array(data.drop(["Prediction"], 1))[:-futureDays]# independent variable
print(x)

y = np.array(data["Prediction"])[:-futureDays]# dependent variable
print(y)
######
#To split the data into 75% tarining and 25% testing
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.25)
######
##Creating the Linear Regression model
from sklearn.linear_model import LinearRegression
linear = LinearRegression().fit(xtrain, ytrain)
####
######Getting the last ‘x’ rows/days of the feature data set
####
xfuture = data.drop(["Prediction"], 1)[:-futureDays]
xfuture = xfuture.tail(futureDays)
xfuture = np.array(xfuture)
print(xfuture)
########
##To show the linear regression model prediction
linearPrediction = linear.predict(xfuture)
print("Linear regression Prediction =",linearPrediction)
####
##Visualize the Linear Model Prediction
predictions = linearPrediction
valid = data[x.shape[0]:]
valid["Predictions"] = predictions
plt.figure(figsize=(10, 6))
plt.title(" Stock Price Prediction Model(Linear Regression Model)")
plt.xlabel("Days")
plt.ylabel("Close Price USD ($)")
plt.plot(data["Close Price"])
plt.plot(valid[["Close Price", "Predictions"]])
plt.legend(["Original", "Valid", "Predictions"])
plt.show()

