from selenium import webdriver
import time
import pandas as pd
import os
from selenium.webdriver.common.by import By


def get_info(driver):

    i=1
    while True:
        info_dict = {}

        time.sleep(2)
        try:
            title = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[3]/div['+str(i)+']/div/div[2]/a/span').text
            content = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[3]/div['+str(i)+']/div/div[3]/div[1]').text
        except:
            i+=1
            title = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[3]/div['+str(i)+']/div/div[2]/a/span').text
            content = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[3]/div['+str(i)+']/div/div[3]/div[1]').text


        i+=1
            
        info_dict['title'] = title
        info_dict['content'] = content

        df = pd.DataFrame([info_dict])
        if os.stat("data.csv").st_size == 0:
            df.to_csv('data.csv',  mode='a', index=False, header="data")
        else:
            df.to_csv('data.csv',  mode='a', index=False, header=False)
        
        if(i%10==0):
            button = driver.find_element(By.XPATH,'//*[@id="load-more-btn"]')
            button.click()



def startpy():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')

    driver.get('https://inshorts.com/en/read/')
    driver.maximize_window()
    
    time.sleep(3)

    get_info(driver)

if __name__ == "__main__":
    startpy()




