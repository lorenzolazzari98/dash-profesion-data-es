import csv
import requests
from bs4 import BeautifulSoup


def getNumberJobs(url):
    url = url
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    return soup.find('h1', {'class': 'hideHH css-zga872 e15r6eig0'}).text.split()[0]

import datetime

now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d")

def fill_job_count(df_urls_Area):
    job_count = {
    "id": datetime.datetime.now().strftime("%Y-%m-%d"),
    "data_engineer": getNumberJobs(df_urls_Area['Data Engineer']),
    "data_scientist": getNumberJobs(df_urls_Area['Data Scientist']),
    "data_analyst": getNumberJobs(df_urls_Area['Data Analyst']),
    "business_analyst": getNumberJobs(df_urls_Area['Business Analyst']),
    "area": df_urls_Area['Area']
    }
    return job_count

import urls #FIX THIS FUCKING PROBLEM!

urls.df_urls
a=fill_job_count(df_urls.loc['Espana'])