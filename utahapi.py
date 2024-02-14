import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
utah_key = os.getenv('UTAH_API_KEY')

def get_bill_list():
    url = f"https://glen.le.utah.gov/bills/2024GS/billlist/{utah_key}"
    response = requests.get(url)
    return response.json()
    

def get_bill_info(bill_name: str):
    url = f"https://glen.le.utah.gov/bills/2024GS/{bill_name}/{utah_key}"
    response = requests.get(url)
    return response.json()

def download_pdf(url: str, bill_name: str):
    base_url = 'https://le.utah.gov'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all('a')
    for link in links:
        full_link = link.get('href')
        if full_link:
            split_link = full_link.split('/')
            if split_link[-1] == f'{bill_name}.pdf':
                bill_response = requests.get(base_url+full_link) 
                pdf = open(bill_name+".pdf", 'wb')
                pdf.write(bill_response.content)
                pdf.close()


