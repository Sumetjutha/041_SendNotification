from pushbullet import Pushbullet
import os
from dotenv import load_dotenv

load_dotenv()  # โหลดไฟล์ .env

API_KEY = os.getenv('API_KEY')

file = "resolution.txt"

with open(file, mode='r') as f:
    # print(f.read())
    text = f.read()
    
pb = Pushbullet(API_KEY)
push = pb.push_note('Please remember', text)