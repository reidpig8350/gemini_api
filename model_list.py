import google.generativeai as genai
import pprint

with open('gemini_key.txt', 'r') as file:
  gemini_key = file.read()
genai.configure(api_key=gemini_key)

for model in genai.list_models():
    pprint.pprint(model)