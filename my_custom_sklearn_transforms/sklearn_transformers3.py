from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class GetDummies(BaseEstimator, TransformerMixin):
    def __init__(self, dummy_columns):
        self.columns = None
        self.dummy_columns = dummy_columns

    def fit_(self, X):
    	return pd.get_dummies(X, columns=self.dummy_columns).columns

    def fit(self, X, y=None):
        self.columns = self.fit_(X)
        return self

    def transform_(self, X):
    	return pd.get_dummies(X, columns=self.dummy_columns)

    def transform(self, X):
        X_new = transform_(X)
        return X_new.reindex(columns=self.columns, fill_value=0)