from altair.vegalite.v4.schema.core import Step
from pandas._config.config import options
from plotly.missing_ipywidgets import FigureWidget
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

header = st.beta_container()
dataset = st.beta_container()

features = st.beta_container()
modelTraining = st.beta_container()


with header:
    st.title("Welcome to quick data analysis project")
    st.text("under the title some sample text")

with dataset:
    st.header("Data set which is contain super market sales and profit data")
    st.text("Here some header of dataset")
    # column1, column2 = st.beta_columns(2)
    data = pd.read_csv("supermarket_sales - Sheet1.csv")
    st.text(data.columns)
    if data is not None:
        st.write(data.head(20))
        
        column1, column2, column3 = st.beta_columns(3)
        max_depth = column1.slider("Select depth value", min_value=10, max_value = 100, value = 20, step = 10)
        getXvalue = column2.selectbox("Select X value", options = data.columns)
        getYvalue = column3.selectbox("Select Y value", options = data.columns)
        
        # st.write(data[getXvalue])
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x = data[getXvalue], y = data[getYvalue],
                                    # barmode='group',
                                    name = 'Formerly_Smoked'))
        st.plotly_chart(fig, use_container_width=True)
        # st.area_chart(getXvalue, getYvalue)
        # st.bar_chart(data["cogs"].head(max_depth))
        # fig = go.Figure(data=go.Bar(y=data["cogs"].head(50)))
        # fig.show()
    # st.beta_expander()    
    

with features:
    st.header("simple feature system")
    st.text("this area for simple feature system")

with modelTraining:
    st.header("simplr model training")
    st.text("this area for imple model section")