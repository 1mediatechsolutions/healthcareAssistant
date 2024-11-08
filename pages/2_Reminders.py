"""
Author  : RaviTeja Manda
Time    : Fri Aug 30 20:44:26 EDT 2024

Logic   : This should hold information on writing and viewing Notes using streamlit and will be the operational page for storing healthcare data by the healthcare companion
"""
import streamlit
import datetime
import json
from streamlit_local_storage import LocalStorage

streamlit.set_page_config(
    page_title="Reminders"
)
streamlit.sidebar.header("Reminders")

streamlit.markdown(
    """
    ### I can help set reminders to save your healthcare data and also retreive your past reminders
    """
)

streamlit.session_state.data_types = ["Notes", "Reminders", "Search", "Anamolies", "Recommendations", "Default"]
streamlit.session_state.data_type = "Reminders"

myLocalStorage = LocalStorage()

if "reminder_id" not in streamlit.session_state:
    streamlit.session_state.reminder_id = 1

if "reminder_date" not in streamlit.session_state:
    streamlit.session_state.reminder_date = None

if "reminder_time" not in streamlit.session_state:
    streamlit.session_state.reminder_time = None

if "reminder_text" not in streamlit.session_state:
    streamlit.session_state.reminder_text = None

def form_callback():
    localReminder = streamlit.session_state.to_dict()
    localReminder.pop('storage_init', None)

    #streamlit.write(localReminder)
    localReminder["reminder_date"] = localReminder["reminder_date"].strftime('%Y-%m-%d')
    localReminder["reminder_time"] = str(localReminder["reminder_time"])
    localReminder["reminder_text"] = streamlit.session_state.reminder_text
    #streamlit.write(streamlit.session_state)
    localReminder.pop("data_types")
    #streamlit.write(localReminder)
    storageId = "My_Reminder_" + str(streamlit.session_state.reminder_id)
    streamlit.write(streamlit.session_state.reminder_text)
    streamlit.write(localReminder["reminder_text"])
    myLocalStorage.setItem(storageId, localReminder)
    streamlit.session_state.reminder_id = streamlit.session_state.reminder_id + 1


remindersOperation = streamlit.selectbox("What operation do you want to do ",
                    ["Add Reminder", "View Reminder(s)", "Update Reminder"],
                    index=None,
                                         placeholder="select an operation")

if remindersOperation == 'View Reminder(s)':
    localData = myLocalStorage.getAll()
    for key in localData:
        if localData[key]["data_type"]  == streamlit.session_state.data_type:
            streamlit.write(localData[key])
    #streamlit.write(reminders)

if remindersOperation == 'Add Reminder':
    streamlit.write(" I can definitely add a reminder for you ... ")
    date = streamlit.date_input("When do you want to set a reminder for ...", value=None, key="reminder_date")
    streamlit.write("Setting reminder for ", date)
    time = streamlit.time_input("What time do you want me to set this for ...", value=None, key="reminder_time")
    streamlit.session_state.reminder_text = streamlit.text_input("Add_Reminder")
    streamlit.write(streamlit.session_state.reminder_text)
    if date is not None:
        if time is not None:
            streamlit.write("Setting reminder for ", str(date), str(time))

    with streamlit.form(key='reminder_form'):
        submit_button = streamlit.form_submit_button(label='Submit', on_click=form_callback)
