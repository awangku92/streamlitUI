import streamlit as st

# Basic Streamlit app setup
st.set_page_config(page_title="Chatbot", page_icon="💬", layout="wide")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! How can I assist you today?"}]

# Sidebar for instructions or settings
st.sidebar.header("Chatbot App")
st.sidebar.write("This is a sample chatbot app using Streamlit. The backend service is simulated for now.")

# Display chat messages
st.title("Chatbot 💬")
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").markdown(msg["content"])

# Input box for user input
if user_input := st.chat_input("Type your message"):
    # Add user message to the session state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Simulate a backend API call
    with st.spinner("Thinking..."):
        # Mock API response (replace this later with your FastAPI + Ollama integration)
        mock_response = {
            "role": "assistant",
            "content": f"Simulated response to: '{user_input}'"
        }

    # Add simulated assistant message to the session state
    st.session_state.messages.append(mock_response)
    st.chat_message("assistant").markdown(mock_response["content"])
