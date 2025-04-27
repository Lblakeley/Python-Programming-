##Import Libraries
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import numpy as np
from sklearn.feature_selection import RFE
from sklearn.metrics import mean_squared_error, r2_score

##Load dataset
df = pd.read_csv('C:/Users/Lauren/OneDrive/Python_Tutorials/Social_Media/Student_performance_data.csv')

##Check data shape and completeness
print(df.shape)
print(df.isnull().sum())

##Only return columns for which the number of null values in the column are greater than 0
null_counts = df.isnull().sum()
for col, count in null_counts.items():
    if count > 0:
        print(f"{col}: {count} null values")

##Print data types
print(df.dtypes)

##View general statistics for all variables
print(df.describe(include='all'))

##Preparing to generate boxplots for nummeric columns so that there are columns of plots and the number of rows
# is determined by how many numeric columns there are
numeric_cols = df.select_dtypes(include='number').columns
num_plots = len(numeric_cols)
cols = 3
rows = math.ceil(num_plots / cols)

##Generating the boxplots so they are all plotted based on the layout established using the above code.
plt.figure(figsize=(cols * 5, rows * 4))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(rows, cols, i)
    sns.boxplot(x=df[col])
    plt.title(f"{col}")
    plt.xticks([])
plt.tight_layout()
plt.show()

##Identifying the target column(dependent variable)
target_column = 'GPA'

##Dropping GradeClass as it is assigned based on GPA (not a valid predictor) and dropping
# StudentID as, even if it did have some signficiance based on p-value, that is completely
# due to chace since StudentIDs are randomly assigned.
df = df.drop(columns=['GradeClass', 'StudentID'])

##Now, I am re-coding all categorical variables from numerical data types to categorical so 
# I can use one-hot encoding to remove the sense of ordinality that a machine learning 
# model may imply from keeping these columns as numeric data types.
categorical_cols = ['Gender', 'Ethnicity', 'ParentalEducation', 'Tutoring', 
                    'ParentalSupport', 'Extracurricular', 'Sports', 
                    'Music', 'Volunteering']

df[categorical_cols] = df[categorical_cols].astype('category')

##Here I am completing one-hot-encording for my categorical variables.
df_encoded = pd.get_dummies(df, drop_first=True)

##Now I am separating the data based on target variable (y) and explanatory features (x)
y = df_encoded[target_column]
X = df_encoded.drop(target_column, axis=1)

## Next, I am defining a helper function to sanitize inputs for OLS
def sanitize_for_ols(X, y=None):
    X_sanitized = X.astype(float)
    if y is not None:
        y_sanitized = pd.to_numeric(y, errors='coerce').astype(float)
        return X_sanitized, y_sanitized
    return X_sanitized


##First, I am splitting the data into train and temp datasets because I want to split the 
# data into train, test, and evaluation datasets and we can only split the data into two sets
# each time we use train_test_split.
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=15)

##Taking the inputs as X_temp and y_temp and splitting the data into test and evaluation
# dataset so 20% of the data is used to test and 10% to evaluate.
X_test, X_eval, y_test, y_eval = train_test_split(X_temp, y_temp, test_size=1/3, random_state=15)

##Printing the shapes of the three datasets
train_shape = X_train.shape
test_shape = X_test.shape
eval_shape = X_eval.shape

print(f"The shape of the training dataset is: {train_shape}.")
print(f"The shape of the test dataset is: {test_shape}.")
print(f"The shape of the evaluation dataset is: {eval_shape}.")

##Here I am training the model for linear regression on the train data.
lr = LinearRegression()
lr.fit(X_train, y_train)

##Now I am sanitizing and fitting the model
X_ols, y_ols = sanitize_for_ols(X, y)
X2 = sm.add_constant(X_ols)  
model = sm.OLS(y_ols, X2).fit() 
print(model.summary())

##Here I am using recursive feature elimination to refine my linear regression model
# to automatically drop the least important features based on their coefficient values.
# Since I input 10 for n_features_to_select, the process repeats until 10 features remain.
rfe = RFE(lr, n_features_to_select=10)
rfe.fit(X_train, y_train)
selected_features = X_train.columns[rfe.support_]
print("Selected Features:\n", selected_features)

##Now that RFE has selected the top 10 features that contribute the most to predicting the 
# target variable, I am retaining the model using only those features.
lr_selected = LinearRegression()
lr_selected.fit(X_train[selected_features], y_train)

##This next section of code runs the retained linear regression model on the test data
# and prints the results.
y_test_pred = lr_selected.predict(X_test[selected_features])
rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
r2_test = r2_score(y_test, y_test_pred)

##The following section of code runs the retained linear regression model on the 
# test data and prints the results.
print(f"\n Test Set Performance:")
print(f"RMSE (Test): {rmse_test:.3f}")
print(f"R² (Test): {r2_test:.3f}")

##The following section of code runs the retained linear regression model on the 
# evaluation data and prints the results.
y_eval_pred = lr_selected.predict(X_eval[selected_features])
rmse_eval = np.sqrt(mean_squared_error(y_eval, y_eval_pred))
r2_eval = r2_score(y_eval, y_eval_pred)

print(f"\n Evaluation Set Performance:")
print(f"RMSE (Eval): {rmse_eval:.3f}")
print(f"R² (Eval): {r2_eval:.3f}")