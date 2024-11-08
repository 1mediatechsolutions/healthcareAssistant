"""
Author  : RaviTeja Manda
Time    : Fri Aug 30 16:14:29 EDT 2024

Logic   : This should hold information on processing data using streamlit and will be the landing page for the healthcare companion
"""
import streamlit


streamlit.set_page_config(
    page_title="Landing Page"
)
streamlit.sidebar.success(" Pick one of my capabilities from above ...")

streamlit.markdown(
    """
    ### Hi
    ### I am your **healthcare companion** ...
    - I will be with you to help **store** all your healthcare data at one place ...
    - I can also help set reminders for you ...
    - I intend to only sieve through **healthcare data (that you provide)** to help find any **anamolies and recommend** you for necessary actions ...
    ### Do you want to know more about me?
    - Check out [my creator' page](https://google.com)
    - Check out [my documentation](https://google.com)
    - Ill ask my creator to create a community forum for enquiring about me and have them at [community
        forums](https://google.com)
    ### I would like to get better and be able to do the following things for you
    - Provide better visualized presentations of your data
    - Standardize healthcare data movement
    - Provide suggestions for
        - Physician networks
        - Literature review for anamolies
"""
)

