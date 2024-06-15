#@title Configure Gemini API key

import google.generativeai as genai

with open('gemini_key.txt', 'r') as file:
  gemini_key = file.read()
genai.configure(api_key=gemini_key)

# 設定對話歷史記錄
history = []

# 連接 Gemini API
model = genai.GenerativeModel('gemini-1.5-flash')

# 開始對話
chat = model.start_chat(history=history)

while True:
  # 輸入使用者訊息
  user_message = input("You: ")

  if user_message=='cool':
    response = chat.send_message('幫我總結我們這一次的對話內容, 字數在100字以內')
    print('Gemini:', response._result.usage_metadata.total_token_count, '\n', str(response.text), )
    break

  # 傳送訊息給 AI 並獲得回應
  response = chat.send_message(user_message)
  print('Gemini:', response._result.usage_metadata.total_token_count, '\n', str(response.text), )

  # 將使用者訊息加入對話歷史記錄
  history.append(user_message)

  # 限制對話歷史記錄為最近五則
  if len(history) > 5:
    history.pop(0)