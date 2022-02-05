'''
Takes any csv file and generates a Principal Component Analysis
Use: streamlit run fuel_app
'''
import streamlit as st
import pandas as pd
import plotly.express as px
from fuel_pca import generate_pca # imported from file

# create two columns and set width units
st.set_page_config(layout="wide")

scatter_column, settings_column = st.columns((4, 1))
scatter_column.title("Multi-Dimensional Analysis")

settings_column.title("Settings")
user_file = settings_column.file_uploader("Choose File")

if user_file is not None:
    data = pd.read_csv(user_file)
    pca_data, cat_cols, pca_cols, = generate_pca(data)

    # pick color setting
    categorical_variable = settings_column.selectbox("Variable Select", options=cat_cols)
    categorical_variable_2 = settings_column.selectbox("Second Variable Select", options = cat_cols)


    # reruns application, sets pca_1 based on selection
    pca_1 = settings_column.selectbox("First Principle Component", options=pca_cols, index=0)

    # removes value selecting above
    # pca_cols.remove(pca_1)
    # not working, workaround: starts on pca_2
    pca_2 = settings_column.selectbox("Second Principle Component", options=pca_cols, index=1)


    # create a scatter plot
    scatter_column.plotly_chart(px.scatter(data_frame=pca_data, x=pca_1, y=pca_2, color=categorical_variable, template="simple_white", height=800, hover_data = [categorical_variable_2]), height=800, use_container_width=True)
else:
    # adds a header
    scatter_column.header("Please choose a file")
