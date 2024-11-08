"""
Author  : RaviTeja Manda
Time    : Fri Aug 30 20:45:26 EDT 2024

Logic   : This should hold information on writing and viewing Notes using streamlit and will be the operational page for storing healthcare data by the healthcare companion
"""
import streamlit

_ = """
Title : Name of the page (on the tab)
Look in to adding an icon as well
"""
streamlit.set_page_config(
    page_title="Recommendations"
)

streamlit.sidebar.header("Recommendations")

streamlit.markdown(
    """
    ### I can help look through your healthcare data and retrieve meaningful insights to recommend necessary course of actions
    """
)

