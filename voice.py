from gtts import gTTS 
import streamlit as st # type: ignore
   

def speak(text):
    

    tts = gTTS(text)
    tts.save("output.mp3")

    audio_file = open("output.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3") 

