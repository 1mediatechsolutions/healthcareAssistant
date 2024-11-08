"""
Author  : RaviTeja Manda
Time    : Fri Aug 30 20:43:26 EDT 2024

Logic   : This should hold information on writing and viewing Notes using streamlit and will be the operational page for storing healthcare data by the healthcare companion
"""
import streamlit
import json
from streamlit_javascript import st_javascript
from streamlit_local_storage import LocalStorage

streamlit.set_page_config(
    page_title="Notes"
)
streamlit.sidebar.header("Notes")

streamlit.markdown(
    """
    ### I can help save your healthcare data and also retreive your information whenever you want
    """
)

notesOperation = streamlit.selectbox(
    " How do you want me to help with your information today ... ",
    ("View Notes", "Save a Note", "Update a Note", "Import Data"),
    index=None,
    placeholder="select an operation"
)

if notesOperation is not None:
    streamlit.write(" I can definitely help you to ", notesOperation)

#if 'Notes_Data' not in streamlit.session_state:
#    streamlit.session_state["Notes_Data"] = None

#if 'Temp_Data' not in streamlit.session_state:
#    streamlit.session_state["Temp_Data"] = None

def noteDataUpdate():
    if "Notes" in streamlit.session_state:
        streamlit.write(streamlit.session_state["Notes_Data"])
    else:
        streamlit.write(streamlit.session_state["Temp_Data"])


#_ = """
#def local_storage_get(key):
#    return st_javascript(f"localStorage.getItem('{key}');")

#def local_storage_set(key, value):
#    value = json.dumps(value, ensure_ascii=False)
#    return st_javascript(f"localStorage.setItem('{key}', JSON.stringify('{value}')")
#"""


if "note_id" not in streamlit.session_state:
    streamlit.session_state.note_id = 1
streamlit.session_state.save_to_database = False
streamlit.session_state.data_types = ["Notes", "Reminders", "Search", "Anamolies", "Recommendations", "Default"]
streamlit.session_state.data_type = "Notes"


_ = """ Local Storage Endpoints """
myLocalStorage = LocalStorage()

def form_callback():
    #streamlit.write(" Saving this note to your log : ",
    #                streamlit.session_state)

    #streamlit.write(" Type : ", type(streamlit.session_state))

    localNote = streamlit.session_state.to_dict()
    localNote.pop('storage_init', None)
    #streamlit.write(localNote)
    for key in streamlit.session_state.data_types:
        if key != "Notes":
            localNote.pop(key, None)
    localNote.pop("data_types", None)

    storageId = "My_Note_" + str(streamlit.session_state.note_id)

    #streamlit.session_state[streamlit.session_state.data_type] = {storageId : localNote}#.update({storageId : "123"})
    myLocalStorage.setItem(storageId, localNote)
    _ = """myLocalStorage.setItem(storageId, streamlit.session_state)"""
    streamlit.session_state.note_id = streamlit.session_state.note_id + 1



if notesOperation == "View Notes":
    streamlit.write(" I am trying to fetch all the notes ... ")
    localData = myLocalStorage.getAll()
    for key in localData:
        if localData[key]["data_type"]  == streamlit.session_state.data_type:
            streamlit.write(localData[key])
     #streamlit.write(localData)

if notesOperation == "Save a Note":
    streamlit.write(" Do you think it is ... ")
    organData = streamlit.selectbox(
        "Is it a generic note or ...",
        ("General Note", "Internal Medicine", "Orthopedic", "Dental", "Cardiac", "Dermatology", "Mental illness"),
        index=0,
        placeholder="Select an area",
        key='note_type'
    )
    noteData = streamlit.text_area("Notes", key='notes_data')
    _ = """
    streamlit.session_state["Notes_Data"] = streamlit.text_area("Notes Data", noteData, on_change=noteDataUpdate())
    """
    if noteData is not None :
        streamlit.write("Character count : ", len(noteData))
        _ = """streamlit.write("I will try to save the following data to your repository ... ", noteData)"""
        streamlit.write("Do you want to save your pain level along with the note?")

        with streamlit.form(key='my_form'):
            slider_input = streamlit.slider('My slider', 0, 10, 5, key='pain_scale')
            checkbox_input = streamlit.checkbox('Yes or No', key='save_to_database')
            subjective_input = streamlit.multiselect("Do you feel anything else",
                                  ["Headache", "Stomach-ache", "Fever", "Nausea", "Diarrhea", "Bleeding", "Swelling", "Light-headed", "Insomnia"],
                                  ["Headache"],
                                  key='subjective_data')
            submit_button = streamlit.form_submit_button(label='Submit', on_click=form_callback)


