import google.generativeai as genai
from google.protobuf import json_format
import time

# Google Sheets API 設定
SCOPE = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
CREDS_FILE = 'gcp_key.json'  # 將你的credentials.json檔案放到同一個資料夾
SPREADSHEET_ID = '1Y9CjrctN9YHrKHG2P_9n85VNn8_8B-OgY6xdYvdkXwM'
SHEET_NAME = 'fintech_lesson'

# Gemini API 設定
# with open('gemini_key.txt', 'r') as file:
#   gemini_key = file.read()
# genai.configure(api_key=gemini_key)

# 連接 Gemini API
import gemini_response
model = genai.GenerativeModel('gemini-1.5-pro')

# 驗證 Google Sheets API
import gspread
from oauth2client.service_account import ServiceAccountCredentials

creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
client = gspread.authorize(creds)

# 開啟 Google Sheets
sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

# 取得所有prompt
prompts = sheet.col_values(1)[1:]  # 假設第一列是標題列

# 呼叫 Gemini API 並將結果寫入 Google Sheets
for i, prompt in enumerate(prompts):
  if prompt:
    if i > 0:
        time.sleep(0.7)

    # 呼叫 Gemini API
    response = gemini_response.gemini_response(prompt)

    # 處理 API 回應
    response_text = response.text

    # 將結果寫入 Google Sheets
    sheet.update_cell(i+2, 2, response_text)  # 從第二列開始寫入

print("Gemini API 呼叫完成，結果已寫入 Google Sheets!")