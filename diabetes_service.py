import joblib
import pandas as pd
from pathlib import Path


class DiabetesService:
    def __init__(self):
        model_path = Path(__file__).parent / "diabetes_model.joblib"
        bundle = joblib.load(model_path)
        self.model = bundle["model"]
        self.features = bundle["feature_columns"]
        self.threshold = bundle["threshold"]

    def preprocess(self, data):
        return pd.DataFrame([data], columns=self.features)

    def predict(self, data):
        features = self.preprocess(data)

        probabilities = self.model.predict_proba(features)[0]
        prediction = int(probabilities[1] >= self.threshold)

        return {
            "prediction": prediction,
            "confidence": float(probabilities[prediction])
        }