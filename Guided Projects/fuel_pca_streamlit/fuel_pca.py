# holds the pca and graph
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def generate_pca(data):
    """
    creates a pca from a given data_source
    seperates numerics
    accepts csv files
    """
    ## Separating data by type
    # seperating the columns into numerics and catergories series
    numerical_cols_list = []
    categorical_cols_list = []

    for i in data.columns:
        if data[i].dtype == np.dtype("float64") or data[i].dtype == np.dtype("int64"):
            numerical_cols_list.append(data[i])
        else:
            categorical_cols_list.append(data[i])


    # ## Numerical
    numerical_data = pd.concat(numerical_cols_list, axis=1)

    # ## Categorical
    categorical_data = pd.concat(categorical_cols_list, axis=1)

    # ## Cleaning numercial_data NaNs
    # applies a function to every row/col of a df
    # for every cell in x, fill in NanN with the mean of the column
    numerical_data = numerical_data.apply(lambda x: x.fillna(np.mean(x)))


    # ## Numerical Scaling
    scaler = StandardScaler()

    # creates a 2d nparray of scales from our dataset
    # configure and transform/scale
    scaled_values = scaler.fit_transform(numerical_data)

    # ## Creating a PCA using our scaled values
    pca = PCA()
    pca_data = pca.fit_transform(scaled_values)
    pca_data = pd.DataFrame(pca_data)

    # one list from a for loop
    new_col_names = ["PCA_" + str(i) for i in range(1, len(pca_data.columns) + 1)]


    # key pair for renaming
    col_mapper = dict(zip(list(pca_data.columns), new_col_names))


    pca_data = pca_data.rename(columns=col_mapper)

    ## Attaching our PCA to our original data
    # This allows us to plot everything on the same graph

    output = pd.concat([data, pca_data], axis=1)

    return output, list(categorical_data.columns), new_col_names
