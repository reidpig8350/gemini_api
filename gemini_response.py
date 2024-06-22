import google.generativeai as genai

with open('gemini_key.txt', 'r') as file:
  gemini_key = file.read()
genai.configure(api_key=gemini_key)

def gemini_response(user_message):

    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])
    response = chat.send_message(user_message)
    return response
