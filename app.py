import streamlit as st
from src.model_building import *
from src.raw_prompt import *

##initialize our streamlit app

# Initialize Streamlit app
st.set_page_config(page_title="Health Consulting Application")
st.header("Health Care Application")

# Allow user to input text or upload an image
user_input = st.text_input("Tell me about your problem: ", key="input1")

submit1 = st.button("Tell me the diet plan")
if submit1:
    # If "Tell me the diet plan" button is clicked  
    response = get_response(user_input, input_prompt1)
    st.subheader("The Response is")
    st.write(response.text)
    
submit2 = st.button("Tell me the Fitness plan")
if submit2:
    # If "Tell me the fitness plan" button is clicked
    response = get_response(user_input, input_prompt2)
    st.subheader("The Response is")
    st.write(response.text)

uploaded_file = st.file_uploader("Upload your food items image", type=["jpg", "jpeg", "png"])
image = ""

# Check which button is clicked
submit3 = st.button("Tell me the total calories")
    
if submit3:
    # If "Tell me the total calories" button is clicked
    if uploaded_file is not None:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(user_input, image_data, input_prompt3)
        st.subheader("The Response is")
        st.write(response)
        
        
# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Chat with Fitness & Nutrition Expert: ",key="input2")
submit4=st.button("Ask the question")

## If submit button is clicked
if submit4 and input:
    response=get_geminiqa_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
        
st.subheader("\n \n The Chat History:")
submit5 = st.button("Chat History")
if submit5 and input:  
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")
    
