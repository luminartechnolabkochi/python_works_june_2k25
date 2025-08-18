
import google.generativeai as genai
import time
import os
from PIL import Image
GOOGLE_API_KEY="AIzaSyBwgMkk_DXW2iaLSpi1ZPgH70tP7uvx-ZQ" # not required in vscode
                                  #Directly assign the api key to GOOGLE_API_KEY in vscode
genai.configure(api_key=GOOGLE_API_KEY)
img_path= r"C:\Users\Luminar\Desktop\calorie_mamam\upma.jpeg"
img=Image.open(img_path)
model=genai.GenerativeModel('gemini-1.5-flash')
while True:
  prompt="You are a nutrition expert. Identify the food in the image and estimate calories."
  if prompt.lower() not in ['exit','quit','bye']:
    response=model.generate_content([prompt,img])
    print("")
    print("Bot:",response.text)
    print("-"*100)
  else:
    print("Exitting....")
    time.sleep(2)
    print("See you....")
    break


    """
    for model in genai.list_models():   #list_models()   genai.list_models()
  print(model.name)
    """