from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd

class GetDummies(BaseEstimator, TransformerMixin):
    def __init__(self, dummy_columns,pd):
        self.columns = None
        self.dummy_columns = dummy_columns
        self.pd = pd

    def fit_(self, X):
    	return self.pd.get_dummies(X, columns=self.dummy_columns).columns

    def fit(self, X, y=None):
        self.columns = self.fit_(X)
        return self

    def transform_(self, X):
    	return self.pd.get_dummies(X, columns=self.dummy_columns)

    def transform(self, X):
        X_new = transform_(X)
        return X_new.reindex(columns=self.columns, fill_value=0)