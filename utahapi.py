import requests
import os
from dotenv import load_dotenv

load_dotenv()
utah_key = os.getenv('API_KEY')

def get_bill_list():
    url = f"https://glen.le.utah.gov/bills/2024GS/billlist/{utah_key}"
    response = requests.get(url)

    print(response.text)

def get_bill_info():
    ...