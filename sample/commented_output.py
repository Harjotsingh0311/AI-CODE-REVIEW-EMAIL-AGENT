# Import the pandas library for data manipulation and analysis
import pandas as pd

# Import tools for splitting the data into training and testing sets
from sklearn.model_selection import train_test_split

# Import the Random Forest classifier algorithm
from sklearn.ensemble import RandomForestClassifier

# Import metrics for evaluating the model's performance
from sklearn.metrics import (
    accuracy_score,          # Calculates the ratio of correct predictions
    classification_report,   # Provides precision, recall, f1-score for each class
    confusion_matrix         # Shows the counts of true vs predicted classes
)

# Load the dataset from a CSV file into a DataFrame
df = pd.read_csv("data.csv")   # Replace with your dataset

# Separate the features (X) from the target variable (y)
X = df.drop("target", axis=1)  # Drop the target column to get input features
y = df["target"]               # Target variable (labels)

# Split the data into training and testing subsets
X_train, X_test, y_train, y_test = train_test_split(
    X,                         # Feature matrix
    y,                         # Target vector
    test_size=0.2,             # 20% of data reserved for testing
    random_state=42,           # Seed for reproducibility
    stratify=y                 # Keep class proportions the same in splits
)

# Instantiate a Random Forest classifier with specified hyperparameters
rf = RandomForestClassifier(
    n_estimators=100,          # Number of trees in the forest
    max_depth=None,            # Trees grow until all leaves are pure or contain <min_samples_split samples
    random_state=42,           # Seed for reproducibility
    n_jobs=-1                  # Use all available CPU cores
)

# Train the Random Forest model on the training data
rf.fit(X_train, y_train)

# Generate predictions for the test set
y_pred = rf.predict(X_test)

# Evaluate the model's accuracy on the test set
print("Accuracy:", accuracy_score(y_test, y_pred))

# Print a detailed classification report (precision, recall, f1-score)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Print the confusion matrix to see how predictions are distributed across classes
print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# Compute feature importance scores from the trained model
importance = pd.DataFrame({
    "Feature": X.columns,                  # Feature names
    "Importance": rf.feature_importances_  # Corresponding importance values
}).sort_values(by="Importance", ascending=False)

# Display the feature importance ranking
print("\nFeature Importance:")
print(importance)