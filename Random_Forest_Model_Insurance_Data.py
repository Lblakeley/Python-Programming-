import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt

#####This Python code's overall purpose is to perform Exploratory Data Analysis on insurance data downloaded from Kaggle, and then to generate
#####a multiple linear regression model to predict the charges.

df = pd.read_csv('insurance_members_data.csv')
print(df)

##From EDA performed in the multiple_linear_regression file, we discovered some variables need to be coded to be able to be processed in a multiple linear regression model.
##Sex, smoker status, and region were all non-numeric data types- specifically objects, that needed to be made categorical and coded.
##This is part of the process of cleaning data for use. 
df['sex'] = df['sex'].astype('category')
df['sex'] = df['sex'].cat.codes ##0 is female and 1 is male 
df['smoker'] = df['smoker'].astype('category')
df['smoker'] = df['smoker'].cat.codes ##1 is yes and 0 is no 
df['region'] = df['region'].astype('category')
df['region'] = df['region'].cat.codes ##3 is southwest, 2 is southeast, 1 is northwest, 4 is northeast 
print(df)

##We drop 'charges' from our set of x variables and denote y as 'charges' since it is our dependent variable.
X = df.drop('charges', axis=1)
Y = df['charges']

print(df.describe())

##Split the data into tain and test populations.
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= .2, random_state=42)

##Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

##Evaluate the model.
Y_pred = model.predict(X_test)
mse = mean_squared_error(Y_test, Y_pred)
print("MSE: ", mse) ##MSE is the average error amount squared. 
print("RMSE:", (mse**.5)) ##RMSE is the square root of the MSE. Both MSE and RMSE put heavier importance on larger errors between actual and predicted values,.




feature_importance = pd.Series(model.feature_importances_, index=X.columns)
print(feature_importance)
sns.barplot(x=feature_importance, y=feature_importance.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features")
plt.show()


###training the model on n_estimators = 500 this time to attempt to improve the accuracy of the model. N_estimators corresponds to the number of 
###decision trees to be used in the Random Forest enemble. Each tree is trained on a bootstrap sampling of the training data. The greater the 
###number of decision trees, the more accurate a model tends to be. However, the greater the n-value, the greater the computational time of the model. 


##Train the model
model = RandomForestRegressor(n_estimators=500, random_state=42)
model.fit(X_train, Y_train)

##Evaluate the model.
Y_pred = model.predict(X_test)
mse = mean_squared_error(Y_test, Y_pred)
print("MSE: ", mse) ##MSE is the average error amount squared. 
print("RMSE:", (mse**.5)) ##RMSE is the square root of the MSE. Both MSE and RMSE put heavier importance on larger errors between actual and predicted values,.




feature_importance = pd.Series(model.feature_importances_, index=X.columns)
print(feature_importance)
sns.barplot(x=feature_importance, y=feature_importance.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features")
plt.show()

#Observation
##The RMSE of the first model w/ n_estimators=100 was 4590. However, the RMSE of the second model with n_estimators was 4559. This change is not very 
##significant. However, the RMSE of our multiple linear regression model was 5801. Compared to our multiple linear regression model, 
##it appears there are less significant errors, or variances between the actual and predicted values in the random forest models than 
##our multiple linear regression model.