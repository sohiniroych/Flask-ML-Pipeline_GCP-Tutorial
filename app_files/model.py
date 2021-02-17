# Importing the libraries
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

dataset = pd.read_csv('50_Startup.csv')

#Importing data set
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values

from sklearn.tree import DecisionTreeRegressor
reg=DecisionTreeRegressor(max_depth=5)
reg.fit(X,y)
y_pred=reg.predict(X)
print(reg.score)


# Loading the model to compare results
model=pickle.load(open('treemodel.pkl','rb'))
x_test=np.array([[16000, 135000, 450000]])
print(x_test)
print(model.predict(x_test))

#To generate a best fit model
X_range=np.zeros((50,3))
y_range=np.zeros((50,))
for i in range(3):
    Xi=X[:,i]
    vals=plt.hist(Xi,49)
    plt.xlabel("Feature")
    plt.ylabel("Frequency")
    X_range[:,i]=np.transpose(vals[1])
y_range=model.predict(X_range)    


# Plot the results
plt.figure()
plt.scatter(X[:,0], y, s=20, edgecolor="black", c="darkorange", label="train data")
plt.scatter(x_test[:,0], model.predict(x_test), s=30, color="yellowgreen", label="test data", linewidth=2)
plt.plot(X_range[:,0], y_range, color="cornflowerblue",
         label="Regression_model", linewidth=2)
plt.xlabel("R&D Cost")
plt.ylabel("Profit")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()


plt.figure()
plt.scatter(X[:,1], y, s=20, edgecolor="black", c="darkorange", label="train data")
plt.scatter(x_test[:,1], model.predict(x_test), s=30, color="yellowgreen", label="test data", linewidth=2)
plt.plot(X_range[:,1], y_range, color="cornflowerblue",
         label="Regression_model", linewidth=2)
plt.xlabel("Admin Cost")
plt.ylabel("Profit")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()



plt.figure()
plt.scatter(X[:,2], y, s=20, edgecolor="black", c="darkorange", label="train data")
plt.scatter(x_test[:,2], model.predict(x_test), s=30, color="yellowgreen", label="test data", linewidth=2)
plt.plot(X_range[:,2], y_range, color="cornflowerblue",
         label="Regression_model", linewidth=2)
plt.xlabel("Marketing Cost")
plt.ylabel("Profit")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()

#Save the model
pickle.dump(reg,open('treemodel.pkl','wb'))


