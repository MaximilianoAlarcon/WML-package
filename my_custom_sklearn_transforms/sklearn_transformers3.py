from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd

class GetDummies(BaseEstimator, TransformerMixin):
    def __init__(self, dummy_columns):
        self.columns = None
        self.dummy_columns = dummy_columns

    def fit(self, X, y=None):
    	import pandas as pd
        self.columns = pd.get_dummies(X, columns=self.dummy_columns).columns
        return self

    def transform(self, X):
    	import pandas as pd
        X_new = pd.get_dummies(X, columns=self.dummy_columns)
        return X_new.reindex(columns=self.columns, fill_value=0)