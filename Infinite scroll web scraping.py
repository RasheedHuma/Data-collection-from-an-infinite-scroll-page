#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import packages

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import pandas as pd


# In[14]:


# Extract a list of all links on a webpage with infinite scroll

# Initialize WebDriver
driver = webdriver.Chrome()  # Replace this with the appropriate web driver you're using (Chrome, Firefox, etc.)

# Open the URL of the webpage
url = "https://ogjre.com/transcripts"  # I'm using this webpage as an example.
driver.get(url)

# Automatically scroll to the page to the bottom
scroll_pause_time = 1 # Pause between each scroll to allow time for the page to load new tabs
screen_height = driver.execute_script("return window.screen.height;")  # Browser window height
i = 1
while True:
    # Scroll down
    driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
    i += 1
    time.sleep(scroll_pause_time)

    # Check if you have reached the end of the page (if there is an end!)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if screen_height * i > scroll_height:
        break

# Fetch the data using BeautifulSoup after all data is loaded
soup = BeautifulSoup(driver.page_source, "html.parser")

# Close the WebDriver session
driver.quit()

# Create a list of all the links on the webpage
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))
links

