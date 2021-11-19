from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import pandas

class GetDummies(BaseEstimator, TransformerMixin):
    def __init__(self, dummy_columns):
        self.columns = None
        self.dummy_columns = dummy_columns

    def fit(self, X, y=None):
        #self.columns = pandas.get_dummies(X, columns=self.dummy_columns).columns
        return self

    def transform(self, X):
        #X_new = pandas.get_dummies(X)
        #return X_new.reindex(columns=self.columns, fill_value=0)
        return self