from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd


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




# Un transformador para remover columnas indeseadas
class Transform_data(BaseEstimator, TransformerMixin):
    def __init__(self, dummies_transformar,PAYMENT_TERM_transformer,LOAN_AMOUNT_transformer,CHECKING_BALANCE_transformer,EXISTING_SAVINGS_transformer,AGE_transformer,EMPLOYMENT_DURATION_transformer):
        self.dummies_transformar = dummies_transformar
        self.PAYMENT_TERM_transformer = PAYMENT_TERM_transformer
        self.LOAN_AMOUNT_transformer = LOAN_AMOUNT_transformer
        self.CHECKING_BALANCE_transformer = CHECKING_BALANCE_transformer
        self.EXISTING_SAVINGS_transformer = EXISTING_SAVINGS_transformer
        self.AGE_transformer = AGE_transformer
        self.EMPLOYMENT_DURATION_transformer = EMPLOYMENT_DURATION_transformer

        
    def powertransformer(self,dataframe,col,transformers):
        c = dataframe[col].copy()
        c = np.array(c).reshape(-1,1)
        c = transformers["1"].transform(c)
        c = transformers["2"].transform(c)
        c = transformers["3"].transform(c)
        c = np.float32(c)
        dataframe[col] = c
        
    def powertransformer_sqrt(self,dataframe,col,transformers):
        c = dataframe[col].copy()
        c = np.sqrt(c)
        c = np.array(c).reshape(-1,1)
        c = transformers["1"].transform(c)
        c = transformers["2"].transform(c)
        c = transformers["3"].transform(c)
        c = np.float32(c)
        dataframe[col] = c
        
    def powertransformer_log(self,dataframe,col,transformers):
        c = dataframe[col].copy()
        c = np.log(c)
        c = np.float32(c)
        c = np.array(c).reshape(-1,1)
        c = transformers["1"].transform(c)
        c = transformers["2"].transform(c)
        c = transformers["3"].transform(c)
        c = np.float32(c)
        dataframe[col] = c
    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primero realizamos la cópia del DataFrame 'X' de entrada
        data = X.copy()
        
        self.powertransformer_log(data,"PAYMENT_TERM",self.PAYMENT_TERM_transformer)
        self.powertransformer_log(data,"LOAN_AMOUNT",self.LOAN_AMOUNT_transformer)
        self.powertransformer(data,"CHECKING_BALANCE",self.CHECKING_BALANCE_transformer)
        self.powertransformer_sqrt(data,"EXISTING_SAVINGS",self.EXISTING_SAVINGS_transformer)
        self.powertransformer_sqrt(data,"AGE",self.AGE_transformer)
        self.powertransformer(data,"EMPLOYMENT_DURATION",self.EMPLOYMENT_DURATION_transformer)
        
        data = self.dummies_transformar.transform(data)
        
        # Retornamos um nuevo dataframe sin las colunmas indeseadas
        return data