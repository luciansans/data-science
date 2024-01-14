# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:59:55 2023

@author: Xray
"""

import requests
from bs4 import BeautifulSoup

def get_word_count(url, target_word):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')  # Fix: 'htl.parser' to 'html.parser'

        title = soup.find('title').text  # Fix: Remove () after text
        print(f'Title: {title}')  # Fix: Correct the print statement

        body_text = soup.get_text()  # Fix: 'get_Text' to 'get_text'
        word_count = body_text.lower().count(target_word.lower())  # Fix: 'counter' to 'count'
        print(f'The word "{target_word}" appears {word_count} times in the webpage.')

    except Exception as e:
        print(f"An error occurred: {e}")

url = 'https://www.richfield.ac.za/'
word_to_find = 'education'

get_word_count(url, word_to_find)
