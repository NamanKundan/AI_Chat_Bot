import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Chat Bot",
    page_icon="🤖",
    layout="centered"
)

# Initialize the Gemini model
@st.cache_resource
def load_model():
    return ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp')

model = load_model()

# App title
st.title("🤖 AI Chat Bot")
st.caption("Powered by Google Gemini")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.invoke(prompt)
                st.markdown(response.content)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response.content})
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Sidebar with options
with st.sidebar:
    st.header("Settings")
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    st.subheader("About")
    st.info("""
    This chat bot uses Google's Gemini AI model to answer your questions.
    
    **Features:**
    - Natural conversation
    - Context-aware responses
    - Fast and accurate
    """)
    
    st.divider()
    
    st.caption(f"💬 Total messages: {len(st.session_state.messages)}")
