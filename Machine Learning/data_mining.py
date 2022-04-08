import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
	accuracy_score,
    precision_score,
    recall_score
)
from sklearn.model_selection import train_test_split
import time

# import into a dataframe
df = pd.read_csv('data_mining_processed.csv',sep=",")

# split into X and Y
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# different models 
randomforest = RandomForestClassifier()
gradientboosting = GradientBoostingClassifier()
decisiontree = DecisionTreeClassifier()

# split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train the different models on the training set and time the training
start_rf = time.time()
randomforest.fit(X_train,y_train)
end_rf = time.time()
rf_time = end_rf - start_rf

start_gb = time.time()
gradientboosting.fit(X_train,y_train)
end_gb = time.time()
gb_time = end_gb - start_gb

start_dt = time.time()
decisiontree.fit(X_train,y_train)
end_dt = time.time()
dt_time = end_dt - start_dt


# Evaluate the performance of the models
randomforest_predictions = randomforest.predict(X_test)
gradientboosting_predictions = gradientboosting.predict(X_test)
decisiontree_predictions = decisiontree.predict(X_test)


#accuracy
rf_accuracy = accuracy_score(y_test,randomforest_predictions)
gb_accuracy = accuracy_score(y_test,gradientboosting_predictions)
dt_accuracy = accuracy_score(y_test,decisiontree_predictions)

# recall
rf_recall = recall_score(y_test,randomforest_predictions)
gb_recall = recall_score(y_test,gradientboosting_predictions)
dt_recall = recall_score(y_test,decisiontree_predictions)

# precision
rf_precision = precision_score(y_test,randomforest_predictions)
gb_precision = precision_score(y_test,gradientboosting_predictions)
dt_precision = precision_score(y_test,decisiontree_predictions)


# Print out the metrics for comparison
print("Random forest metrics:\n")
print("Accuracy: ",rf_accuracy)
print("Precision: ",rf_precision)
print("Recall: ", rf_recall)
print("Fit time: ", rf_time)

print("\nGradient boosting metrics:\n")
print("Accuracy: ",gb_accuracy)
print("Precision: ",gb_precision)
print("Recall: ", gb_recall)
print("Fit time: ", gb_time)

print("\nDecision tree metrics:\n")
print("Accuracy: ",dt_accuracy)
print("Precision: ",dt_precision)
print("Recall: ", dt_recall)
print("Fit time: ", dt_time)




