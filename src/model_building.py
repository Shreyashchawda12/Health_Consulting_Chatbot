from dotenv import load_dotenv
import os
import sys
import google.generativeai as genai
from PIL import Image
from exception import CustomException
from logger import logging

load_dotenv() 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_response(input, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response_text = model.generate_content([input, prompt])
        logging.info('Model gemini-pro selected')
        return response_text
    except Exception as e:
        logging.error(f"Error in get_response: {e}")
        raise CustomException(e,sys)
    
def get_geminiqa_response(question):
    model=genai.GenerativeModel("gemini-pro") 
    chat = model.start_chat(history=[])
    response=chat.send_message(question,stream=True)
    return response

def get_gemini_response(input, image, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([input, image[0], prompt])
        logging.info('Model gemini-pro-vision selected')
        return response.text
    except Exception as e:
        logging.error(f"Error in get_response: {e}")
        raise CustomException(e,sys)

def input_image_setup(uploaded_file):
    try:
        # Check if a file has been uploaded
        if uploaded_file is not None:
            # Read the file into bytes
            bytes_data = uploaded_file.getvalue()

            image_parts = [
                {
                    "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                    "data": bytes_data
                }
            ]
            return image_parts
        else:
            raise FileNotFoundError("No file uploaded")
    except Exception as e:
        logging.error(f"Error in get_response: {e}")
        raise CustomException(e,sys)
