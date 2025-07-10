import joblib
import pandas as pd

def predict_leads(data: pd.DataFrame):
    model = joblib.load("models/model.pkl")
    X = pd.get_dummies(data)
    model_features = model.feature_names_in_
    for col in model_features:
        if col not in X:
            X[col] = 0
    X = X[model_features]
    return model.predict_proba(X)[:, 1]
