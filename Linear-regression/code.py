# --------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# code starts here
df = pd.read_csv(path)
# Display top 5 
df.head(5)
# Store all the features(independent values) in a variable called X
X = df[['ages','num_reviews','piece_count','play_star_rating','review_difficulty','star_rating','theme_name','val_star_rating','country']]
#We can simply use "X = df.drop('list_price',axis=1)"

#Store the target variable list_price (dependent value) in a variable called y
y = df['list_price']

# Test train split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 6)

# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here        
cols = X_train.columns
fig, axes = plt.subplots(nrows = 3, ncols = 3,figsize=(20,20))
for i in range (0,3):
    for j in range(0,3):
        col = cols[i*3 + j]
        axes[i,j].set_title(col)
        axes[i,j].scatter(X_train[col],y_train)
        axes[i,j].set_xlabel(col)
        axes[i,j].set_ylabel('list_price')

plt.show


# code ends here



# --------------
# Code starts here
corr = X_train.corr()
print(corr)

# drop columns from X_train
X_train.drop(['play_star_rating','val_star_rating'],axis = 1 ,inplace=True)

# drop columns from X_test
X_test.drop(['play_star_rating','val_star_rating'], axis = 1 ,inplace=True)

# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
print(mse)
r2 = r2_score(y_test,y_pred)
print(r2)


# Code ends here


# --------------
# Code starts here
residual = y_test - y_pred
plt.hist(residual)

# Code ends here

