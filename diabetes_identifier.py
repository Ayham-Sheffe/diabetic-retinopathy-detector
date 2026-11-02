from diabetes_service import DiabetesService


class DiabetesIdentifier:
    def __init__(self):
        self.service = DiabetesService()

    def identify(self, features):
        return self.service.predict(features)