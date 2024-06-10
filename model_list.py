import google.generativeai as genai
import pprint

api_key = "AIzaSyCltdPSPhXW9gTJSTy4j-jMWHt7sg76ESA"
genai.configure(api_key=api_key)

for model in genai.list_models():
    pprint.pprint(model)