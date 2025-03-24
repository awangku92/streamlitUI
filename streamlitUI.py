import streamlit as st
import requests

# FastAPI Backend URL
API_URL = "http://localhost:7860/chat/"

# Basic Streamlit app setup
st.set_page_config(page_title="Dr. Pokok", page_icon="🌱", layout="centered")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! Apa yg boleh saya bantu hari ini?"}]

# Sidebar for instructions or settings
st.sidebar.header("🌱 Dr. Pokok")
st.sidebar.write('''Dr. Pokok adalah chatbot kederdasan buatan (AI) yang menggunakan Penjanaan Dipertingkatkan Semula (RAG).''')
st.sidebar.write("Dr. Pokok adalah pakar dalam sayur-sayuran taman & tumbuhan dalam rumah.")
st.sidebar.write('''Dr. Pokok mempunyai pengetahuan dalam:\n
* Nama saintifik & biasa bagi tumbuhan
* Nasihat penjagaan & penanaman
* Cadangan tanaman pengiring
* Panduan penjagaan harian''')


st.title("🌱 Dr. Pokok - Pakar Pokok Anda")

# Display chat messages history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").markdown(msg["content"])

# Input box for user input
if user_input := st.chat_input("Tanya Dr. Pokok..."):
    # Add user message to the session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    # Simulate a backend API call
    with st.spinner("Sedang berfikir...", show_time=True):
        try:
            response = requests.post(API_URL, headers={"text": user_input})
            # print(response.json())
            bot_response = response.json().get("response", "Maaf, saya tidak faham.")
        except Exception as e:
            print(e)
            bot_response = "⚠️ Ralat: Tidak dapat berhubung dengan API. " + str(e)  

    # Add simulated assistant message to the session state
    st.session_state.messages.append(bot_response)
    st.chat_message("assistant").markdown(bot_response)
