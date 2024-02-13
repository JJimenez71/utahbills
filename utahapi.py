import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
utah_key = os.getenv('API_KEY')

def get_bill_list():
    url = f"https://glen.le.utah.gov/bills/2024GS/billlist/{utah_key}"
    response = requests.get(url)
    return response.json()
    

def get_bill_info(bill_name: str):
    url = f"https://glen.le.utah.gov/bills/2024GS/{bill_name}/{utah_key}"
    response = requests.get(url)
    return response.json()