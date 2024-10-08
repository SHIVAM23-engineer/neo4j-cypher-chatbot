import streamlit as st
from utils import write_message
from agent import generate_response
# Page Config
st.set_page_config("movie_chatter", page_icon=":movie_camera:")

# Set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm the Chatbot!  How can I help you?"},
    ]

# Submit handler
def handle_submit(message):
    """
    Submit handler:

    You will modify this method to talk with an LLM and provide
    context using data from Neo4j.
    """

    # Handle the response
    with st.spinner('Thinking...'):
       response = generate_response(message)
       write_message('assistant',response)


# Display messages in Session State
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# Handle any user input
#Uses the walrus operator (:=) to assign the user's input to the variable question and simultaneously check if it's not empty. If the user submits a message, the following block executes.
if question := st.chat_input("What is up?"):
    # Display user message in chat message container
    write_message('user', question)

    # Generate a response
    handle_submit(question)