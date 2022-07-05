#Import neccesary libraries

from selenium import webdriver              # driver to control chrome browser
import pyautogui                            
from bs4 import BeautifulSoup          # to parse the html code
import threading                       # to do multi threding
import time 
import pandas as pd# to store data in csv file

#from seleniumwire import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pyautogui
import numpy as np
#enter the filename

df=pd.DataFrame()
df2=pd.DataFrame()
df3=pd.DataFrame()
df4=pd.DataFrame()
#intiate the chrome webdriver instance
query=[]
searchTerms=["Bangalore Indiranagar", "Bangalore koramangala"]
for i in searchTerms:
    #for j in shops:
    #string="https://www.google.com/maps/search/"+i
    string="https://www.google.com/maps/search/"+i+" "+"Library"
    #string1="https://www.google.com/maps/search/"+i+" "+"Book Store"
    query.append(string)
    #query.append(string1)

    
lists=set()
test=["https://www.google.com/maps/search/10th M V Garden ulsoor Company"]#uc.install(executable_path='c:/users/agney/desktop/chromedriver.exe',)
driver = webdriver.Chrome(executable_path='c:/users/agney/desktop/chromedriver.exe')
name=[]
link=[]

a=0

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)
for x in query:
    driver.get(x)
    i=1
    print(len(link))
    while True:
        try:
            time.sleep(5)
            pyautogui.moveTo(300, 500)
            pyautogui.scroll(-1000)
            time.sleep(1)
            pyautogui.scroll(-1000)
            pyautogui.scroll(-1000)
            time.sleep(1)
            pyautogui.scroll(-1000)
            time.sleep(1)
            pyautogui.scroll(-1000)
            time.sleep(1)
            pyautogui.scroll(-1000)
            time.sleep(3)
                
                
            soup = BeautifulSoup(driver.page_source, 'lxml')
                    
            try:
                for v in soup.find_all("a", {"class": "hfpxzc"}):
                    df4.at[a,"HREF"]=[v['href']]
                    a=a+1
                    df4.to_csv("OnlyHREF-BLR-Library.csv", index=False)
                        
                    
            except(KeyError, ElementClickInterceptedException) as e:
                print(e)
                    
                pass
            
            driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/button[2]/img").click()
                ##df['Link'] = pd.Series(link)
            print("Navigating to Next Page")
                
        except (TimeoutException, WebDriverException) as e:
            print(e)
            print("Last page reached")
                

            break

    
