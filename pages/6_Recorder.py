"""
Author  : RaviTeja Manda
Time    : Tue Oct  1 19:52:50 EDT 2024

Logic   : This should hold information on driving the capability to record messages through voice and allow for integration of this through the other available services
"""
import streamlit
from audio_recorder_streamlit import audio_recorder

streamlit.set_page_config(
    page_title="Voice Recorder"
)
streamlit.sidebar.header("Voice Recorder")

streamlit.markdown(
    """
    ### I can help save messages that are either recorded or uploaded from a different medium
    """
)


audioData = audio_recorder(auto_start=True)
if audioData:
    streamlit.audio(audioData, format="audio/wav")
    sttreamlit.markdown(
        """
        ### Tis is thi vioce recording;w
        :w

        """
    )
