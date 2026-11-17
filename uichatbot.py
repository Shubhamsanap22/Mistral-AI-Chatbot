import streamlit as st
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Mistral AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_dotenv()

# -----------------------------
# Custom CSS
# -----------------------------

st.markdown("""
<style>

/* Google Font */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family: 'Inter', sans-serif;
}

/* Background */
.stApp{
    background:#0F172A;
}

/* Hide Streamlit Branding */
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* DO NOT HIDE HEADER */
/* header{visibility:hidden;} */

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#111827;
    border-right:1px solid #334155;
}

/* Header */
.title{
    text-align:center;
    color:white;
    font-size:42px;
    font-weight:700;
    margin-top:10px;
}

.subtitle{
    text-align:center;
    color:#94A3B8;
    margin-bottom:35px;
}

/* Chat Messages */
[data-testid="stChatMessage"]{

    background:#1E293B;

    border:1px solid #334155;

    border-radius:16px;

    padding:18px;

    margin-bottom:18px;

}

/* Sidebar Text */
section[data-testid="stSidebar"] *{
    color:white;
}

/* Scrollbar */
::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-thumb{
    background:#4F46E5;
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------

col1, col2 = st.columns([9,1])

with col1:
    st.markdown(
        "<div class='title'>🤖 Mistral AI Assistant</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Powered by LangChain & Mistral AI</div>",
        unsafe_allow_html=True
    )

with col2:
    st.success("🟢 Online")

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("⚙ Assistant")

choice = st.sidebar.radio(
    "Choose Personality",
    (
        "😡 Angry",
        "😂 Funny",
        "😢 Sad",
    )
)

st.sidebar.divider()

st.sidebar.markdown("### Model")
st.sidebar.info("mistral-small-2506")

st.sidebar.markdown("### Framework")
st.sidebar.write("• LangChain")
st.sidebar.write("• Streamlit")
st.sidebar.write("• Mistral AI")

# -----------------------------
# Personality
# -----------------------------

if choice == "😡 Angry":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."

elif choice == "😂 Funny":
    mode = "You are a very funny AI agent. You respond with humor and jokes."

else:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."

# -----------------------------
# Model
# -----------------------------

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

# -----------------------------
# Session State
# -----------------------------

if "mode" not in st.session_state:
    st.session_state.mode = mode

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# Reset chat when personality changes

if st.session_state.mode != mode:

    st.session_state.mode = mode

    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# -----------------------------
# Display Chat History
# -----------------------------

for msg in st.session_state.messages[1:]:

    if isinstance(msg, HumanMessage):

        with st.chat_message("user", avatar="👤"):
            st.markdown(msg.content)

    elif isinstance(msg, AIMessage):

        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(msg.content)

# -----------------------------
# Chat Input
# -----------------------------

prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(response.content)