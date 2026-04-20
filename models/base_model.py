from abc import ABC, abstractmethod


class BaseModel(ABC):
    @abstractmethod
    def train(self, X_train, y_train):
        raise NotImplementedError

    @abstractmethod
    def predict(self, X_test):
        raise NotImplementedError

    @abstractmethod
    def predict_proba(self, X_test):
        raise NotImplementedError
