#Importing necessary Libraries
from selenium import webdriver
import time

#maximize function
def seleniumMaximize():
    #creating a webdriver object
    driver = webdriver.Chrome(executable_path='')
    driver.minimize_window() #maximize window size
    # driver.get("https://www.codespeedy.com/author/varunbhattacharya/") #opening the url
    # time.sleep(10) #waiting for 10 seconds

#driver
if __name__ == "__main__":
    seleniumMaximize() #call the function