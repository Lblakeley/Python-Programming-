import pandas as pd
import sklearn 
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

#####This Python code's overall purpose is to perform Exploratory Data Analysis on insurance data downloaded from Kaggle, and then to generate
#####a multiple linear regression model to predict the charges.

df = pd.read_csv('insurance_members_data.csv')
print(df)

##EDA (Exploratory Data Analysis)
print(df.head())

print(df.dtypes)


##This section is a type of EDA known as categorical encoding. I am looking at the value counts of each category for an idea on 
##the quantity of data we have for each categorical point. As a side note, if I had three categories revealed for sex, such as;
##male, female, and woman, this could indicate further processing is required such that the 'woman' values are transformed to 'female'
##prior to the categorical coding done below.
print(df['region'].value_counts(dropna=False))
print(df['smoker'].value_counts(dropna=False))
print(df['sex'].value_counts(dropna=False))

##Looks at mean, standard deviation, minimum, maximum, and other IQR data (25%,50%,75%) by explanatory variable.
print(df.describe())

##Looks for null values in dataset.
print(df.isnull().sum()) ##There are no null values, the underlying dataset does not need to be cleaned further

##From EDA we discovered some variables need to be coded to be able to be processed in a multiple linear regression model.
##Sex, smoker status, and region were all non-numeric data types- specifically objects, that needed to be made categorical and coded.
##This is part of the process of cleaning data for use. 
df['sex'] = df['sex'].astype('category')
df['sex'] = df['sex'].cat.codes ##0 is female and 1 is male 
print(df)

df['smoker'] = df['smoker'].astype('category')
df['smoker'] = df['smoker'].cat.codes ##1 is yes and 0 is no 
df['region'] = df['region'].astype('category')
df['region'] = df['region'].cat.codes ##3 is southwest, 2 is southeast, 1 is northwest, 4 is northeast 
print(df)


x = df.drop(columns = 'charges')
print(x)

y = df['charges']
print(y)


##Generation of boxplot of explanatory variables as part of EDA- I'm interested in outliers and spread.

##x, shown above, has dropped the dependent variable and all columns needed for the boxplots exist in this variable.
##assigning these columns as 'numerical_col'
numerical_col = x.columns
print(numerical_col)


##Initialize figure with 6 subplots in a row
fig, ax = plt.subplots(1,6, figsize = (10, 6))

##Add space between subplots for visualization purposes.
plt.subplots_adjust(wspace =0.5)

##Define the variables for each subplot
variables = numerical_col
colors = ['r','g','y','b','purple','none']
x_labels = numerical_col

##Draw the boxplots for each explanatory variable in its corresponding subplot
for i, variable in enumerate(variables):
    sns.boxplot(data= x[variable], ax=ax[i], color=colors[i])
    ax[i].set_xlabel(x_labels[i])
##Remove X-tick labels for a cleaner, less cluttered visualization.
    ax[i].set_xticklabels([])


##Plot is shown- it is observed that there are a significant number of outliers associated with BMI. These outliers can cause skewing in the data. 
    ##skewed data reduces the statistical power of ML models. I am not going to remove or process these outliers as they indicate a large 
    ##number of obese individuals in the dataset, and I do not want to exclude these 
plt.show()



##Variable selection using wrapper method. Longer and more computationally expensive process (while loop reduces time spent). However,
##this method is more likely to perform better at feature selection, reducing error in the model produced. 
import statsmodels.api as sm
model = sm.OLS(y, x).fit()
print(model.pvalues) ##high p-values indicate that your evidence is not strong enough to suggest an effect between the explanatory variable
###and the dependent variable. The smaller the p-value, the stronger the evidence of a relationship.

selected_features = list(x.columns)
print(selected_features)

while (len(selected_features) > 0): ##while we have at least one selected feature
    model = sm.OLS(y, x).fit() ##fitting the model as we did above
    p = model.pvalues ##The p-values for each feature are being stored in variable 'p'
    pmax = max(p) ##gives the maximum p-values
    feature_pmax = p.idxmax() ##index of the highest p-value, row label of maximum value. Think row(over(partition by)) in SQL.
    if(pmax > 0.01): ##
        selected_features.remove(feature_pmax)
        x = x[selected_features]
    else:
        break
print(selected_features)
##at .01 significance, ['age', 'bmi', 'smoker', 'region'] are kept.
##at .10 significance, all features are kept. For this model, .1 is high
##at .075 significance, all features are kept.
##at .06 significance, ['age', 'sex', 'bmi', 'smoker', 'region'] are kept. Children is dropped
##at .05 significance, ['age', 'bmi', 'smoker', 'region'] are kept. Same as at .01. 

x.columns = ['age', 'bmi', 'smoker', 'region']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= .3, random_state= 0)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(x_train, y_train)

c= lr.intercept_
print(c)

m= lr.coef_
print(m)

y_pred_train = lr.predict(x_train)
print(y_pred_train)


plt.scatter(y_train, y_pred_train)
plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")
plt.show()

from sklearn.metrics import r2_score 
r2 = r2_score(y_train,y_pred_train)
print(r2) ##.7283 - how well the variance in the dependent variable (charges) can be explained by the independent variables or training features of the model

y_pred_test = lr.predict(x_test)

import matplotlib.pyplot as plt
plt.scatter(y_test, y_pred_test)
plt.xlabel ("Actual Charges")
plt.ylabel("Predicted Charges")
plt.show()

from sklearn.metrics import r2_score 
r2 = r2_score(y_test,y_pred_test)
print(r2) ##.7889 on testing data. However only 30% was used to test.
print(x)

from sklearn.metrics import mean_squared_error
Y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred_test)
print("MSE: ", mse) ##MSE is the average error amount squared. 
print("RMSE:", (mse**.5)) ##RMSE is the square root of the mean squared error. 

#Observation
##The RMSE for this model is 5801. That means the square root of the average of the squared differences between the predicted values and the actual values
##is $5801.  

