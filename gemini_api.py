import google.generativeai as genai
import pathlib
import textwrap
#from IPython.display import display
#from IPython.display import Markdown
import os
from dotenv import load_dotenv

load_dotenv()


GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

#for m in genai.list_models():
#  print(m)

#for m in genai.list_models():
#    if 'generateContent' in m.supported_generation_methods:
#        print(m.name)


model = genai.GenerativeModel('gemini-pro')

#response = model.generate_content("What is the meaning of life?")
#print(response.text)
#def to_markdown(text):
#  text = text.replace('•', '  *')
#  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
#to_markdown(response.text)


response = model.generate_content("What is the meaning of life?", stream=True)
for chunk in response:
  print(chunk.text)
  print("_"*80)


