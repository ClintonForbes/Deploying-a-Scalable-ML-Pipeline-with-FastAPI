import pytest
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.data import process_data
from ml.model import train_model, compute_model_metrics

# Load a small sample dataset for testing purposes
data = pd.DataFrame({
    "age": [39, 50, 38, 53],
    "workclass": ["State-gov", "Self-emp-not-inc", "Private", "Private"],
    "fnlwgt": [77516, 83311, 215646, 234721],
    "education": ["Bachelors", "Bachelors", "HS-grad", "11th"],
    "education-num": [13, 13, 9, 7],
    "marital-status": ["Never-married", "Married-civ-spouse", "Divorced", "Married-civ-spouse"],
    "occupation": ["Adm-clerical", "Exec-managerial", "Handlers-cleaners", "Handlers-cleaners"],
    "relationship": ["Not-in-family", "Husband", "Not-in-family", "Husband"],
    "race": ["White", "White", "White", "Black"],
    "sex": ["Male", "Male", "Male", "Male"],
    "capital-gain": [2174, 0, 0, 0],
    "capital-loss": [0, 0, 0, 0],
    "hours-per-week": [40, 13, 40, 40],
    "native-country": ["United-States", "United-States", "United-States", "United-States"],
    "salary": ["<=50K", ">50K", "<=50K", "<=50K"]
})

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

# implement the first test. Change the function name and input as needed
def test_process_data_types():
    """
    Test if the process_data function returns the expected types.
    """
    X, y, encoder, lb = process_data(data, categorical_features=cat_features, label="salary", training=True)
    assert isinstance(X, np.ndarray), "Expected X to be a numpy array"
    assert isinstance(y, np.ndarray), "Expected y to be a numpy array"
    assert len(X) == len(data), "Expected X to have the same number of rows as the input data"
    assert len(y) == len(data), "Expected y to have the same number of rows as the input data"

# implement the second test. Change the function name and input as needed
def test_train_model_type():
    """
    Test if the train_model function returns a RandomForestClassifier.
    """
    X, y, encoder, lb = process_data(data, categorical_features=cat_features, label="salary", training=True)
    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier), "Expected the model to be an instance of RandomForestClassifier"

# implement the third test. Change the function name and input as needed
def test_train_test_split():
    """
    Test if the training and test datasets have the expected size or data type.
    """
    from sklearn.model_selection import train_test_split
    train, test = train_test_split(data, test_size=0.20, random_state=42)
    assert isinstance(train, pd.DataFrame), "Expected train to be a pandas DataFrame"
    assert isinstance(test, pd.DataFrame), "Expected test to be a pandas DataFrame"
    assert len(train) == 3, "Expected train to have 3 rows"
    assert len(test) == 1, "Expected test to have 1 row"
