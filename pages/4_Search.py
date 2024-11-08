"""
Author  : RaviTeja Manda
Time    : Fri Aug 30 20:46:26 EDT 2024

Logic   : This should hold information on searching through your Notes using streamlit and will be the operational page for searching healthcare data by the healthcare companion
"""
import streamlit
from streamlit_local_storage import LocalStorage
import time

streamlit.session_state.data_type = "Search"

myLocalStorage = LocalStorage()

streamlit.set_page_config(
    page_title="Search"
)
streamlit.sidebar.header("Search")

streamlit.markdown(
    """
    ### I can help search through your healthcare data
    """
)

reminders = 0
notes = 0
localData = myLocalStorage.getAll()

for key in localData:
    if localData[key]["data_type"] == "Notes":
        notes+=1
    if localData[key]["data_type"] == "Reminders":
        reminders+=1



streamlit.write(" What do you want to search about ?")
prompt = streamlit.chat_input(" What do you want to search about?")
if prompt:
    with streamlit.status(" Let me traverse through your data"):
        streamlit.write(" Searching for your data in the local storage")
        time.sleep(2)
        streamlit.write("You have ", notes, " notes and ", reminders, " reminders")
        time.sleep(1)
        streamlit.write("I can try to find about - ", prompt)
        streamlit.write(" Let me look through your past data and pull up relevant data about - ", prompt)

    streamlit.write("Do you want me to search in the internet as well?")
