from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd

# Un transformador para remover columnas indeseadas
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns, formato):
        self.columns = columns
        self.formato = formato

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primero realizamos la cópia del DataFrame 'X' de entrada
        data = X.copy()
        if "ALLOW" in data.columns:
            data.drop(labels=["ALLOW"], axis='columns',inplace=True)
        data = data[self.formato].copy()
        # Retornamos um nuevo dataframe sin las colunmas indeseadas
        return data.drop(labels=self.columns, axis='columns')