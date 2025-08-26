


import google.generativeai as genai
import time
import os
from PIL import Image



def process_food_image(image):
    
    # Configure the API with your key.
  genai.configure(api_key="AIzaSyBwgMkk_DXW2iaLSpi1ZPgH70tP7uvx-ZQ") 

  # Specify the path to your image file.
  img_path = image

  # Open the image file using the Pillow library.
  img = Image.open(img_path) 

  # Load the Gemini 1.5 Flash model.
  model = genai.GenerativeModel('gemini-1.5-flash',generation_config={'response_mime_type':'application/json'}) 

  # Define the prompt for the AI.
  prompt = "You are a nutrition expert. Identify the food in the image and estimate calories.get me response.txt with calorie_low, calorie_high, food name,and note as json."

  # Send the prompt and the image to the model and get a response.
  response = model.generate_content([prompt, img])

  # Print the response from the AI.
  # print("Bot:", response.text)
  import json

  data = json.loads(response.text) # json=> dictionary

  return data

data=process_food_image(r"C:\Users\Luminar\Desktop\calorie_mamam\upma.jpeg")

print(data)