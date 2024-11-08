"""
Author  : RaviTeja Manda
Time    : Fri Aug 30 20:47:26 EDT 2024

Logic   : This should hold information on detecting anamolies from within your healthcare data and will be the operational page for running AI models on your healthcare data by the healthcare companion
"""
import streamlit


streamlit.set_page_config(
    page_title="Anamoly Detector"
)
streamlit.sidebar.header("Anamoly Detector")

streamlit.markdown(
    """
    ### I can help detect and identify anamolies within your healthcare data and also retreive your information whenever you want
    """
)

