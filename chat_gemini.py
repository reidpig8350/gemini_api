#@title Configure Gemini API key

import google.generativeai as genai

with open('gemini_key.txt', 'r') as file:
  gemini_key = file.read()
genai.configure(api_key=gemini_key)

# 設定對話歷史記錄
history = []

# 連接 Gemini API
model = genai.GenerativeModel('gemini-1.5-pro')

# 開始對話
chat = model.start_chat(history=history)

while True:
  # 輸入使用者訊息
  user_message = input("輸入你的訊息: ")

  # 將使用者訊息加入對話歷史記錄
  history.append(user_message)

  # 傳送訊息給 AI 並獲得回應
  response = chat.send_message(user_message)
  print(str(response.text))

  # 限制對話歷史記錄為最近五則
  if len(history) > 5:
    history.pop(1)