'''MIT License

Copyright (c) 2019 Jellohunter7

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

plate = ""

state = ""

color = ""

def alpr():

    global plate

    global state

    global color

    cap = cv2.VideoCapture(0)

    options = Options()

    options.add_argument("--headless")

    options.add_argument("--window-size=1920x1080")

    chrome_driver = os.getcwd() +"\\chromedriver.exe"

    browser = webdriver.Chrome(options=options, executable_path=chrome_driver)

    while cap.isOpened():

        _, frame = cap.read()

        browser.get(('https://www.openalpr.com/cloud-api.html'))

        cv2.imwrite('alpr.jpg', frame)
        
        upload = browser.find_element_by_xpath('/html/body/div[7]/input').send_keys(os.getcwd()+"/alpr.jpg")

        time.sleep(1)

        try:
            plate =  browser.find_element_by_xpath('//*[@id="cloud_api_demo"]/div[2]/div[2]/span[1]')

            state = browser.find_element_by_xpath('//*[@id="cloud_api_demo"]/div[2]/div[2]/span[2]')

            color = browser.find_element_by_xpath('//*[@id="cloud_api_demo"]/div[2]/div[2]/span[3]')

            plate = plate.text

            state = state.text

            color = color.text

            print('Working', plate, state, color)

        except:
            plate = ""

            state = ""

            color = ""
            
            print('Failed')
            
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        
    browser.close()

alpr()
