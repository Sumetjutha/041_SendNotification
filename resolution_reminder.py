from pushbullet import Pushbullet
import os
from dotenv import load_dotenv

load_dotenv()  # โหลดไฟล์ .env

API_KEY = os.getenv('API_KEY')

file = "resolution.txt"

with open(file, mode='rb') as f:
    # อ่านไฟล์เป็น binary และแปลงเป็น Unicode
    text = f.read().decode('utf-8')
    
pb = Pushbullet(API_KEY)
push = pb.push_note('!เตือนความจำ...', text)